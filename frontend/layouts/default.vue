<template>
  <v-app>
    <v-overlay :value="menu" color="#0f1e34" opacity="1">
      <v-row justify="center">
        <v-col cols="3">
          <v-avatar color="primary" size="50">AP</v-avatar>
        </v-col>
        <v-col id="my_profile_text"> Мой профиль </v-col>
      </v-row>

      <v-row>
        <v-divider class="m-0" />
      </v-row>

      <v-list id="menu" flat>
        <v-list-item
          v-for="(item, i) in items"
          id="menu-item"
          :key="i"
          :to="item.to"
          router
          :ripple="false"
          @click="chg"
        >
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title id="menu-item-text" v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-overlay>
    <v-app-bar id="header" fixed app>
      <v-toolbar-title v-text="title" @click="$router.push('/')" />
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
  </v-app>
</template>

<script>
import "../assets/global.scss";
export default {
  name: "DefaultLayout",
  created() {
    let param = this.$route.fullPath;
    console.log(param);
    if (param == "/clients") {
      this.title = "Клиенты";
    } else if (param == "/create_object") {
      this.title = "Объекты недвижимости";
    } else if (param == "/constructor") {
      this.title = "Конструктор предложений";
    } else if (param == "/calculator") {
      this.title = "Кредитный калькулятор";
    } else if (param == "/money") {
      this.title = "Вознаграждения";
    } else if (param == "/tasks") {
      this.title = "Задачи";
    } else if (param == "/booking") {
      this.title = "Бронирование просмотра";
    }
  },
  data() {
    return {
      items: [
        {
          icon: "mdi-cash-multiple",
          title: "Вознаграждения",
          to: "/money",
        },
        {
          icon: "mdi-account-multiple",
          title: "Клиенты",
          to: "/clients",
        },
        {
          icon: "mdi-clock-outline",
          title: "Задачи",
          to: "/tasks",
        },
        {
          icon: "mdi-home-city",
          title: "Объекты недвижимости",
          to: "/create_object",
        },
        {
          icon: "mdi-plus-box",
          title: "Конструктор предложений",
          to: "/constructor",
        },
        {
          icon: "mdi-timer-sand-full",
          title: "Бронирование просмотра",
          to: "/booking",
        },
        {
          icon: "mdi-calculator",
          title: "Кредитный калькулятор",
          to: "/calculator",
        },
        {
          icon: "mdi-signal-cellular-1",
          title: "Аналитика",
          to: "/",
        },
        {
          icon: "mdi-school",
          title: "Обучение",
          to: "/",
        },
        {
          icon: "mdi-cog",
          title: "Настройки",
          to: "/settings",
        },
      ],
      menu: false,
      title: "Поребрик",
    };
  },
  methods: {
    chg() {
      this.menu = false;
      let param = this.$route.fullPath;
      console.log(param);
      if (param == "/clients") {
        this.title = "Клиенты";
      } else if (param == "/create_object") {
        this.title = "Объекты недвижимости";
      } else if (param == "/constructor") {
        this.title = "Конструктор предложений";
      } else if (param == "/calculator") {
        this.title = "Кредитный калькулятор";
      } else if (param == "/money") {
        this.title = "Вознаграждения";
      } else if (param == "/tasks") {
        this.title = "Задачи";
      } else if (param == "/booking") {
        this.title = "Бронирование просмотра";
      }
    },
  },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Manrope:wght@500&display=swap");

#main {
  background-color: #edf0f4;
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
  max-height: 20px;
  text-align: left;
  justify-content: center;
  align-items: center;
  justify-items: center;
  color: white;
}

#menu-item-text {
  font-size: 1rem;
  font-weight: bold;
  color: white;
}

#my_profile_text {
  padding-top: 1.5rem;
}
</style>
