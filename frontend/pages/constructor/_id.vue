<template>
  <div class="cards">
    <div>
      <v-text-field outlined :value="slug" readonly> </v-text-field>
    </div>
    <p>По вашим запросам нашло {{ copied.length }} варианта !</p>
    <div class="cards__grid">
      <Card
        v-for="(res, id) in copied"
        :key="id"
        :flat-name="res.building"
        :flat-area="res.area"
        :flat-price="res.price"
        :flat-addr="res.address"
        :flat-img="res.photo_links[0]"
      />
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
      let param = this.$route.fullPath;
      return (this.fullParam = `http://92.63.105.59/${param}`);
    },
  },
  mounted() {
    OffersAPI.getById(this.$route.params.id).then((r) => {
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
</style>