<template>
  <div class="cards">
    <div>
      <v-text-field outlined :value="slug" readonly> </v-text-field>
    </div>
    <!-- <p>По вашим запросам нашло {{ copied.length }} варианта !</p> -->
    <div class="cards__grid">
      <div v-for="(res, id) in copied" :key="id">
        <div>
          <div class="block">
            <p class="subtitle">Фотографии</p>
            <v-slide-group>
              <v-slide-item v-for="img in res.photo_links" :key="img">
                <img
                  :src="img"
                  height="160px"
                  style="margin-right: 8px; border-radius: 4px"
                  alt=""
                />
                <!-- {{ img }} -->
              </v-slide-item>
            </v-slide-group>
          </div>
          <div class="block">
            <p class="subtitle">Описание жилого комплекса</p>
            <p class="title">{{ res.description }}</p>
          </div>
          <div class="block" style="margin-top: 8px">
            <p class="subtitle">Тип объекта</p>
            <p class="title">Квартира</p>
          </div>
          <div class="block">
            <p class="subtitle">Жилой комплекс</p>
            <p class="title">{{ res.residential_complex }}</p>
          </div>
          <div class="block">
            <p class="subtitle">Стоимость</p>
            <p class="title">{{ res.price }} ₽</p>
          </div>
          <div class="block" style="gap: 50px; flex-direction: row">
            <div>
              <p class="subtitle">Площадь</p>
              <p class="title">{{ res.area }} м2</p>
            </div>
            <div>
              <p class="subtitle">Количество комнат</p>
              <p class="title">{{ res.rooms }}</p>
            </div>
          </div>
          <div class="block" style="gap: 30px; flex-direction: row">
            <div>
              <p class="subtitle">Этажей в доме</p>
              <p class="title">30</p>
            </div>
            <div>
              <p class="subtitle">Этаж квартиры</p>
              <p class="title">{{ res.floor }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- <Card
        :key="id"
        :flat-name="res.building"
        :flat-area="res.area"
        :flat-price="res.price"
        :flat-addr="res.address"
        :flat-img="res.photo_links[0]"
      /> -->
    </div>
  </div>
</template>

<script>
import OffersAPI from "~/API/OffersAPI";
import Card from "~/components/Card.vue";
export default {
  components: { Card },
  data() {
    return {
      copied: {},
      fullParam: "",
    };
  },
  computed: {
    slug: function () {
      let param = this.$route.query.id;
      return (this.fullParam = `http://92.63.105.59/constructed/?id=${param}`);
    },
  },
  mounted() {
    OffersAPI.getById(this.$route.query.id).then((r) => {
      console.log(r.data);
      this.copied = r.data;
    });
  },
};
</script>

<style lang="scss" scoped>
.cards {
  &__grid {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
}
.subtitle {
  font-size: 12px;
}
.title {
  font-size: 14px;
}
.block {
  display: flex;
  flex-direction: column;
}
#slider {
  // gap: 20px;
}
</style>