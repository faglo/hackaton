<template>
  <v-app>
    <v-overlay :value="menu" color="white" opacity="1">
      <v-list id="menu" flat>
        <v-list-item
          v-for="(item, i) in items"
          id="menu-item"
          :key="i"
          :to="item.to"
          router
          :ripple="false"
          @click="menu = false"
        >
          <v-list-item-content>
            <v-list-item-title id="menu-item-text" v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
        <v-btn color="#5790FF">Конструктор предложений</v-btn>
      </v-list>
    </v-overlay>
    <v-app-bar id="header" fixed app>
      <v-toolbar-title v-text="title" />
      <v-spacer />
      <v-btn icon @click.stop="menu = !menu">
        <v-icon id="header__but"> mdi-menu </v-icon>
      </v-btn>
    </v-app-bar>
    <v-main id="main">
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <!-- <v-footer
      :absolute="!fixed"
      app
    >
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer> -->
  </v-app>
</template>

<script>
import "../assets/global.scss";
export default {
  name: "DefaultLayout",
  data() {
    return {
      items: [
        {
          title: "Задачи",
          to: "/",
        },
        {
          title: "Клиенты",
          to: "/",
        },
        {
          title: "Объекты",
          to: "/create_object",
        },
        {
          title: "Аналитика",
          to: "/",
        },
        {
          title: "Вознаграждения",
          to: "/",
        },
      ],
      menu: false,
      title: "Поребрик",
    };
  },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Manrope:wght@500&display=swap");

#main {
  background-color: #FFFFFF;
}

#header {
  background: #0f1e34;
  box-shadow: 0px 4px 8px 0px #0511321a;
  color: white;
  &__but {
    color: #edf0f4;
  }
}

#menu {
  background-color: rgba(149, 149, 149, 0);
  // font-family: 'Manrope', sans-serif;
}

#menu-item {
  height: 66px;
  text-align: center;
  color: black;
}

#menu-item-text {
  font-size: 1rem;
}
</style>
