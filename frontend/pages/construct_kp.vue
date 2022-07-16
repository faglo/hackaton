<template>
  <div>
    <v-overlay :value="filter" color="#EDF0F4" opacity="1">
      <v-list id="menu" flat>
        <v-list-item-title id="menu-item-text">Фильтры</v-list-item-title>
        <v-list-item-content>
          <v-list-item>
            <v-list-item-content>
              <v-text-field></v-text-field>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-text-field></v-text-field>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-text-field></v-text-field>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-content>

        <!-- <v-btn color="#5790FF">Конструктор предложений</v-btn> -->
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
  background: white;
  color: black;
  width: 100%;
  border-radius: 8px;
  padding:  10px 17px;
  box-shadow: 2px 2px 8px 0px #08122F1F;
  max-width: 300px;

}
</style>