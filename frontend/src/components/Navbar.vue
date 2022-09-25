<template>
  <div class="navbar">
    <div class="container">
      <b-navbar toggleable="lg" type="dark">
        <b-navbar-brand>
          <router-link :to="{'name': 'index'}" class="navbar-logo">Web <span>Auction</span></router-link>
        </b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <div v-if="isLoggedIn">
            <a>{{ user.meta.email }}</a>
            <router-link :to="{'name': 'logout'}">
              <font-awesome-icon icon="fa-solid fa-right-from-bracket"/>
              Выйти
            </router-link>
          </div>
          <div v-else>
            <router-link :to="{'name': 'login'}">
              <font-awesome-icon icon="fa-solid fa-key"/>
              Войти
            </router-link>
            <router-link :to="{'name': 'signup'}">
              <font-awesome-icon icon="fa-solid fa-user-plus"/>
              Зарегистрироваться
            </router-link>
          </div>
        </b-collapse>
      </b-navbar>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'Navbar',
  computed: {
    ...mapGetters({
      isLoggedIn: 'isLoggedIn',
      user: 'user',
    })
  },
}
</script>

<style scoped>

</style>