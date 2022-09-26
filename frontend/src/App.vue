<template>
  <Navbar />
  <div class="container my-5">
    <RouterView />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import axios from 'axios';
import {mapGetters} from 'vuex';

export default {
  components: {
    Navbar
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.user.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Token ${token}`
    }
    else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>
