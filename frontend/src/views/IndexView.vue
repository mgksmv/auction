<template>
  <h1 class="text-center mb-4">Главная</h1>

  <div class="row">
    <b-card
      v-for="auction in auctions" key="item.id"
      :title="auction.item.name"
      :img-src="auction.item.image"
      img-alt="Image"
      tag="item"
      style="max-width: 20rem;"
      class="m-2"
    >
      <b-card-text>
        {{ auction.item.description }}
      </b-card-text>

      <h3>{{ auction.item.price }}</h3>

      <router-link :to="{name: 'item', params: {id: auction.item.id}}" class="btn btn-primary">Участвовать</router-link>
    </b-card>
  </div>

</template>

<script>
import axios from 'axios'
import {mapGetters} from 'vuex';

export default {
  name: 'IndexView',
  data() {
    return {
      auctions: null,
    }
  },
  computed: {
    ...mapGetters({
      isLoggedIn: 'isLoggedIn',
    })
  },
  methods: {
    getBiddingItems() {
      axios.get('/bidding/auctions/').then(response => {
        this.auctions = response.data
      })
    },
  },
  created() {
    this.getBiddingItems()
  },
}
</script>

<style scoped>

</style>