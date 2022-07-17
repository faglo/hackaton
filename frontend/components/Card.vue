<template>
  <div>
    <v-card rounded="8px" id="card" elevation="2">
      <v-img width="104" height="104" id="card__img" :src="flatImg"></v-img>
      <div id="card__info">
        <div id="card__info-main">
          <span style="font-size: 1rem; font-weight: 600"
            >Квартира, {{ flatArea }} м2
          </span>
          <!-- <v-rating
            :value="4.5"
            color="blue"
            dense
            half-increments
            readonly
            size="14"
          ></v-rating> -->
          <span style="max-width: 120px; font-size: 0.8rem; font-weight: 400">{{
            flatAddr
          }}</span>
        </div>
        <div id="card__rout">
          <span>{{ flatPrice }} ₽</span>
          <!-- <v-container fluid class="px-0"> -->
          <div v-if="showBox">
            <v-checkbox
              v-if="boxState === false"
              v-model="boxState"
              @click="$emit('addFlat')"
            ></v-checkbox>
            <v-checkbox
              v-else
              v-model="boxState"
              true-value
              @click="$emit('removeFlat')"
            ></v-checkbox>
          </div>
          <!-- </v-container> -->
        </div>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    flatName: {
      type: String,
      required: true,
    },
    showBox: {
      type: Boolean,
      required: false,
    },
    flatPrice: {
      required: true,
    },
    flatAddr: {
      type: String,
      required: true,
    },
    flatImg: {
      required: true,
    },
    flatArea: {
      required: true,
    },
    boxState: {
      type: Boolean,
      default: false,
    },
  },
  // data() {
  //   return {
  //     boxState: false,
  //   };
  // },
};
</script>

<style lang="scss" scoped>
#card {
  padding: 8px;
  box-shadow: 2px 2px 8px 0px #08122f1f;
  // border-radius: 8px;
  display: grid;
  grid-template-columns: 104px 1fr;
  gap: 12px;
  // align-items: center;
  &__img {
    border-radius: 4px;
  }
  &__info {
    display: flex;
    flex-direction: column;
    // padding: 0;
    justify-content: space-between;
    &-main {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
  }
  &__rout {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 30px;
  }
}
</style>