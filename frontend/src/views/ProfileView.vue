<template>
  <div v-if="isLoggedIn">
    <router-link class="btn btn-danger rounded-pill" :to="{name: 'index'}">
      <font-awesome-icon icon="fa-solid fa-arrow-left"/>
      Назад
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

      <h1 class="text-center mb-4">Предметы</h1>

      <div v-if="items.length > 0" class="row">
        <b-card-group deck>
          <b-card
              v-for="item in items" key="item.id"
              :title="item.name"
              :img-src="item.image"
              img-alt="Image"
              tag="item"
              style="max-width: 20rem;"
              class="m-2"
          >
            <p>{{ item.description }}</p>
          </b-card>
        </b-card-group>
      </div>

      <div v-else>
        <h4 class="text-center text-danger">У вас нет предметов</h4>
      </div>
    </div>
  </div>
  <div v-else>
    <h4 class="text-center">
      Чтобы посмотреть профиль, нужно <router-link :to="{name: 'login'}">войти</router-link>
    </h4>
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
      items: null,
    }
  },
  computed: {
    ...mapGetters({
      isLoggedIn: 'isLoggedIn',
      user: 'user',
    }),
    items() {
      let filteredItems = []
      for (let item of this.items) {
        if (item.owner == this.user.meta.id) {
          filteredItems.push(item)
        }
      }
      return filteredItems
    }
  },
  methods: {
    getUserItems() {
      axios.get('/bidding/items/').then(response => {
        this.items = response.data
      })
    }
  },
  created() {
    this.getUserItems()
  },
}
</script>

<style scoped>

</style>