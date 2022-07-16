<template>
  <div>
    <p>Новые объекты</p>
    <div class="cards">
      <div class="cards__grid">
        <Card v-for="i in 6" :key="i">
          <v-card-text>121</v-card-text>
        </Card>
      </div>
    </div>
  </div>
</template>

<script>
import Card from "../components/Card.vue";
export default {
  components: { Card },
};
</script>

<style lang="scss" scoped>
.cards{
  &__grid{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
}
</style>