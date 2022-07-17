<template>
  <div>
    <v-btn
      v-if="chosenFlats.length > 0"
      fixed
      style="bottom: 23px; color: white; z-index: 999"
      color="#00A8F2"
      >Сформировать предложение</v-btn
    >
    <v-overlay :value="filter" color="#EDF0F4" opacity="0.5">
      <v-list id="menu" dense elevation>
        <!-- <v-list-title id="menu-item-text">Фильтры</v-list-item-title> -->
        <v-list-item id="list-item">
          <v-list-item-content>
            <v-list-item-title>Фильтры</v-list-item-title>
            <v-list-item-title>Выберите жилой комплекс</v-list-item-title>
            <v-select
              outlined
              :items="copied2.residential_complexes"
              hide-details
              v-model="residential_complex"
              label="Standard"
            ></v-select>
          </v-list-item-content>
        </v-list-item>

        <v-list-item id="list-item">
          <v-list-item-content>
            <v-list-item-title>Выберите дом</v-list-item-title>
            <v-select
              :items="copied2.buildings"
              v-model="building"
              outlined
              hide-details
              label="Standard"
            ></v-select>
          </v-list-item-content>
        </v-list-item>

        <v-list-item id="list-item">
          <v-list-item-content>
            <v-list-item-title> Выберите площадь </v-list-item-title>
            <div style="display: flex; gap: 8px">
              <v-text-field
                hide-details
                placeholder="От"
                v-model="area_from"
                outlined
              ></v-text-field>
              <v-text-field
                hide-details
                placeholder="До"
                v-model="area_to"
                outlined
              ></v-text-field>
            </div>
          </v-list-item-content>
        </v-list-item>

        <v-list-item>
          <v-card-text>
            <v-slider
              :tick-labels="ticksLabels"
              :max="6"
              step="1"
              ticks="always"
              tick-size="4"
            ></v-slider>
          </v-card-text>
        </v-list-item>
        <v-list-item id="list-item">
          <v-list-item-content>
            <v-list-item-title> Этаж </v-list-item-title>
            <div style="display: flex; gap: 8px">
              <v-text-field
                hide-details
                placeholder="От"
                v-model="floor_from"
                outlined
              ></v-text-field>
              <v-text-field
                hide-details
                v-model="floor_to"
                placeholder="До"
                outlined
              ></v-text-field>
            </div>
          </v-list-item-content>
        </v-list-item>

        <v-list-item id="list-item">
          <v-list-item-content>
            <v-list-item-title> Стоимость объекта </v-list-item-title>
            <div style="display: flex; gap: 8px">
              <v-text-field
                v-model="price_from"
                hide-details
                placeholder="От"
                outlined
              ></v-text-field>
              <v-text-field
                hide-details
                v-model="price_to"
                placeholder="До"
                outlined
              ></v-text-field>
            </div>
          </v-list-item-content>
        </v-list-item>

        <v-list-item id="list-item">
          <v-btn color="#5790FF" @click="findFlats">Применить</v-btn>
        </v-list-item>
      </v-list>
    </v-overlay>

    <div
      style="
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
      "
    >
      <p>Найдено {{ copied.length }} предложения</p>
      <img @click="toggleFilter" src="/icons/icon_filter.svg" alt="" />
    </div>
    <div class="cards">
      <div class="cards__grid">
        <Card
          v-for="(res, id) in copied"
          :key="id"
          @addFlat="addFlat"
          :flat-name="res.building"
          :flat-area="res.area"
          :flat-price="res.price"
          :flat-addr="res.address"
          :flat-img="res.photo_links[0]"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Card from "../components/Card.vue";
import BuildingsAPI from "~/API/BuildingsAPI";
export default {
  components: { Card },
  mounted() {
    try {
      BuildingsAPI.getByFilter(
        this.residential_complex,
        this.building,
        this.area_from,
        this.area_to,
        this.rooms,
        this.floor_from,
        this.floor_to,
        this.price_from,
        this.price_to
      ).then((res) => (this.copied = res.data));
      BuildingsAPI.getFilterProperties().then(
        (res2) => (this.copied2 = res2.data)
      );
      // console.log(res);
    } catch (error) {
      console.log(error);
    }
  },
  data() {
    return {
      filter: false,
      chosenFlats: [],
      copied: {},
      copied2: {},
      // Поля
      residential_complex: "",
      building: "",
      area_from: 0,
      area_to: 0,
      rooms: 0,
      floor_from: 0,
      floor_to: 0,
      price_from: 0,
      price_to: 0,
      // Поля
      ticksLabels: ["1", "2", "3", "4", "5", ">6"],
    };
  },
  methods: {
    toggleFilter() {
      this.filter = !this.filter;
    },
    addFlat() {
      this.chosenFlats.push("1");
    },
    findFlats() {
      try {
        BuildingsAPI.getByFilter(
          this.residential_complex,
          this.building,
          this.area_from,
          this.area_to,
          this.rooms,
          this.floor_from,
          this.floor_to,
          this.price_from,
          this.price_to
        ).then((res) => (this.copied = res.data));
        this.filter = false
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.cards {
  &__grid {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
}
#menu {
  // background: white;
  // color: black;
  width: 100%;
  border-radius: 8px;
  padding: 10px 17px;
  box-shadow: 2px 2px 8px 0px #08122f1f;
  max-width: 300px;
}
</style>