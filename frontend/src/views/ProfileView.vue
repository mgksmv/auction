<template>
  <router-link class="btn btn-danger rounded-pill" :to="{name: 'index'}">
    <font-awesome-icon icon="fa-solid fa-arrow-left" /> Назад
  </router-link>
  <div>
    <h1 class="text-center mb-4">Профиль</h1>
    <div class="row">
      <div class="col-4">
        <img :src="baseUrl + user.meta.photo" alt="Фото" height="250" width="250">
      </div>
      <div class="col-8">
        <h2 v-if="user.meta.first_name && user.meta.last_name">
          {{ user.meta.first_name }} {{ user.meta.last_name }}
        </h2>
        <h4>{{ user.meta.email }}</h4>
        <h4 v-if="user.meta.phone">{{ user.meta.phone }}</h4>
        <h4 v-if="user.meta.birthday">{{ user.meta.birthday }}</h4>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex';
import axios from 'axios';

export default {
  name: 'ProfileView',
  data() {
    return {
      baseUrl: axios.defaults.baseURL,
    }
  },
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