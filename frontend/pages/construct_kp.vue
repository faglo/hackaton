<template>
  <div>
    <v-overlay :value="filter" color="#EDF0F4" opacity="1">
      <v-list id="menu" flat>
        <!-- <v-list-title id="menu-item-text">Фильтры</v-list-item-title> -->
        <v-list-item>
          <v-list-item-content>
            <v-select outlined label="Standard"></v-select>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-subtitle>1</v-list-item-subtitle>
            <v-select outlined label="Standard"></v-select>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title> Выберите площадь </v-list-item-title>
            <div style="display: flex; gap: 8px">
              <v-text-field placeholder="От" outlined></v-text-field>
              <v-text-field placeholder="До" outlined></v-text-field>
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
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title> Выберите площадь </v-list-item-title>
            <div style="display: flex; gap: 8px">
              <v-text-field placeholder="От" outlined></v-text-field>
              <v-text-field placeholder="До" outlined></v-text-field>
            </div>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title> Выберите площадь </v-list-item-title>
            <div style="display: flex; gap: 8px">
              <v-text-field placeholder="От" outlined></v-text-field>
              <v-text-field placeholder="До" outlined></v-text-field>
            </div>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>

          <v-btn color="#5790FF">Применить</v-btn>
        </v-list-item>
      </v-list>
    </v-overlay>
    <div
      style="display: flex;justify-content: space-between;align-items: flex-start;
      "
    >
      <p>Найдено 4 предложения</p>
      <img @click="toggleFilter" src="/icons/icon_filter.svg" alt="" />
    </div>
    <div class="cards">
      <div class="cards__grid">
        <Card
          v-for="i in 6"
          :key="i"
          :flat-name="'Квартира, 67 м2'"
          :flat-price="20000"
          :flat-addr="'ул. Дзержинксого, 39 3 комнаты 17 этаж'"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Card from "../components/Card.vue";
export default {
  components: { Card },
  data() {
    return {
      filter: false,
      ticksLabels: [
          '1',
          '2',
          '3',
          '4',
          '5',
          '>6',
        ],
    };
  },
  methods: {
    toggleFilter() {
      this.filter = !this.filter;
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
#list {
  // background: black;
  display: flex;

}
</style>