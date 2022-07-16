<template>
  <div>
    <v-card id="card" elevation="2" outlined shaped tile>
      <v-img
        height="104"
        width="104"
        id="card__img"
        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
      ></v-img>
      <v-container id="card__info">
        <v-card-title>Квартира, 67 м2</v-card-title>
        <v-card-subtitle
          >ул. Дзержинксого, 39 3 комнаты 17 этаж</v-card-subtitle
        >
        <v-card-text>8 900 000 ₽</v-card-text>
      </v-container>
    </v-card>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
#card {
  padding: 8px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  &__img {
    border-radius: 4px;
  }
  &__info {
    display: flex;
    flex-direction: column;
    padding: 0;
  }
}
</style>