<template>
  <h1 class="text-center mb-4">Главная</h1>

  <div v-if="auctions.length > 0" class="row">
    <b-card-group deck>
      <b-card
        v-for="auction in auctions" key="item.id"
        :border-variant="auction.is_finished && auction.winner ? 'success' : ''"
        :title="auction.item.name"
        :img-src="auction.item.image"
        img-alt="Image"
        tag="item"
        style="max-width: 20rem;"
        class="m-2"
      >

        <div v-if="!auction.is_finished">
          <b-badge pill variant="warning">• Live!</b-badge>
        </div>

        <h2 class="py-2">{{ auction.price }} ₽</h2>

        <div v-if="auction.is_finished">
          <div v-if="auction.winner">
            <h5 class="text-success">
              <font-awesome-icon icon="fa-solid fa-gavel" /> Победитель:
            </h5>
            <h4 class="text-success winner">{{ auction.winner.get_full_name }}</h4>
          </div>
          <h5 v-else>
            <font-awesome-icon icon="fa-solid fa-gavel" /> Победитель не объявлен
          </h5>
          <router-link :to="{name: 'item', params: {id: auction.item.id}}" class="btn btn-primary rounded-pill">
            Посмотреть итоги
          </router-link>
        </div>
        <div v-else>
          <router-link :to="{name: 'item', params: {id: auction.item.id}}" class="btn btn-success rounded-pill">
            Участвовать
          </router-link>
        </div>

        <template #footer v-if="!auction.is_finished">
          <small v-if="auction.bids.length > 0" class="text-muted">
            Последняя ставка - {{ auction.bids[auction.bids.length - 1].bid_placed_at }}
          </small>
          <small v-else class="text-muted">
            <span class="text-success">Ни одной ставки... Будьте первыми!</span>
          </small>
        </template>
      </b-card>
    </b-card-group>
  </div>
  <div v-else>
    <h4 class="text-center text-danger">Активных аукционов нет</h4>
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
    }),
  },
  methods: {
    getBiddingItems() {
      axios.get('/bidding/auctions/').then(response => {
        this.auctions = response.data
      }).catch(() => {
        this.$store.commit('removeUserData')
      })
    },
  },
  created() {
    this.getBiddingItems()
    setInterval(() => {
      this.getBiddingItems()
    }, 3000)
  },
}
</script>

<style scoped>

</style>