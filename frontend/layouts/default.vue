<template>
  <v-app>
    <v-overlay :value="menu">
      <v-list id="menu" flat>
        <v-list-item
          v-for="(item, i) in items"
          id="menu-item"
          :key="i"
          :to="item.to"
          router
          :ripple="false"
        >
          <v-list-item-content>
            <v-list-item-title id="menu-item-text" v-text="item.title"  />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-overlay>
    <v-app-bar
      fixed
      app
    >
      <v-toolbar-title v-text="title" />
      <v-spacer />
      <v-btn
        icon
        @click.stop="menu = !menu"
      >
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer
      :absolute="!fixed"
      app
    >
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data () {
    return {
      items: [
        {
          title: 'Задачи',
          to: '/'
        },
        {
          title: 'Клиенты',
          to: '/'
        },
        {
          title: 'Объекты',
          to: '/'
        },
        {
          title: 'Аналитика',
          to: '/'
        },
        {
          title: 'Вознаграждения',
          to: '/'
        }
      ],
      menu: false,
      title: 'Vuetify.js'
    }
  }
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@500&display=swap');

#menu {
  background-color: rgba(193, 66, 66, 0.0);
  font-family: 'Manrope', sans-serif;
}

#menu-item{
  height: 66px;
  text-align: center;
}

#menu-item-text{
  font-size: 2rem;
}
</style>
