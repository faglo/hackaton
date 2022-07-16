<template>
  <div>
    <div class="overflowed">
      <div class="overflowed__container">
        <div v-for="i in 6" :key="i" class="overflowed__block">
          <v-list id="menu" flat>
            <v-list-item id="mainItem">
              <v-list-item-subtitle
                id="menu-item-text"
                style="font-size: 16px; font-weight: 600; color: #0f1e34"
                >Фильтры</v-list-item-subtitle
              >
              <v-list-item-subtitle style="font-size: 12px"
                >250 сделок</v-list-item-subtitle
              >
              <v-list-item-subtitle style="font-size: 12px"
                >На сумму 1 250 000 000 ₽
              </v-list-item-subtitle>
            </v-list-item>

            <v-list-item style="margin-bottom: 8px" v-for="i in 4" :key="i">
              <v-card id="cont" @click="pushOrder()">
                <p
                  style="
                    display: flex;
                    justify-content: space-between;
                    font-size: 1rem;
                  "
                >
                  Сделка #6 <span>21.06.22</span>
                </p>
                <p>Двухкомнатная квартира в центре</p>
                <p>8 200 450 ₽</p>
              </v-card>
            </v-list-item>
            <!-- <v-btn color="#5790FF">Конструктор предложений</v-btn> -->
          </v-list>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  layout: "whitdefault",
  methods: {
    pushOrder() {
      let id = 4;
    //   this.$router.push(id);
    },
  },
};
</script>

<style lang="scss" scoped>
#menu {
  width: 300px;
}
p {
  margin-bottom: 0;
}
#mainItem {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  hr {
    width: fit-content;
    // max-width: fit-content;
  }
}

#cont {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 4px 8px;
}
.overflowed {
  &__container {
    overflow-x: scroll;
    display: flex;
    gap: 25px;
  }
}
</style>