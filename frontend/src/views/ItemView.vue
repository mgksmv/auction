<template>
  <b-button @click="disconnect()" variant="danger" pill>Выйти</b-button>

  <div class="row">
    <div v-if="auction.is_finished">
      <h2 v-if="winner" class="text-success text-center mb-3">
        <font-awesome-icon icon="fa-solid fa-gavel" />
        Победитель - {{ winner.get_full_name }}! Поздравляем!
      </h2>
      <h2 v-else class="text-center mb-3">
        <font-awesome-icon icon="fa-solid fa-gavel" />
        Ни одной ставки, победителя нет...
      </h2>
    </div>

    <h1 class="text-center mt-2">{{ auction.price }} ₽</h1>
    <h4 class="text-center mb-5">Выигрышная цена: {{ auction.winning_price }}</h4>

    <div class="col-6">
      <b-card
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

        <h5>Цена - {{ auction.price }} ₽</h5>

        <div v-if="isLoggedIn">
          <div v-if="!auction.is_finished">
            <input v-model="userBid" type="text" class="form-control" :class="incorrectUserBid">
            <div v-if="incorrectUserBid" id="validationServer03Feedback" class="invalid-feedback">
              Ставка не может быть меньше текущей цены!
            </div>
            <b-button @click="placeBid()" variant="primary" class="mt-3" pill>Участвовать</b-button>
          </div>
        </div>
        <div v-else>
          <p class="text-danger">Войдите или зарегистрируйтесь для ставок</p>
        </div>
      </b-card>
    </div>

    <div class="col-6">
      <div class="row pb-4">
        <h2>До окончания аукциона:</h2>
        <div class="col-2 card m-1 p-1 text-center">
          <h3 class="days">{{ timer.days }}</h3>
          <div class="smalltext">Дней</div>
        </div>
        <div class="col-2 card m-1 p-1 text-center">
          <h3 class="hours">{{ timer.hours }}</h3>
          <div class="smalltext">Часов</div>
        </div>
        <div class="col-2 card m-1 p-1 text-center">
          <h3 class="minutes">{{ timer.minutes }}</h3>
          <div class="smalltext">Минут</div>
        </div>
        <div class="col-2 card m-1 p-1 text-center">
          <h3 class="seconds">{{ timer.seconds }}</h3>
          <div class="smalltext">Секунд</div>
        </div>
      </div>

      <h5 class="text-success" v-if="newBidMessage">Новая ставка!</h5>
      <div>
        <h2>История ставок:</h2>
        <ul>
          <li v-for="bid in auction.bids" :key="bid">
            <h5>{{ bid.price }} ₽</h5>
            <p>{{ bid.user.get_full_name }} ({{ bid.bid_placed_at }})</p>
          </li>
          <li v-for="bid in bidsHistory" :key="bid">
            <h5>{{ bid.price }} ₽</h5>
            <p>{{ bid.user }} ({{ bid.bid_placed_at }})</p>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import {mapGetters} from 'vuex';

export default {
  name: 'ItemView',
  data() {
    return {
      isLoaded: false,
      newBidMessage: false,
      biddingSocket: '',
      auction: '',
      bidsHistory: [],
      userBid: '',
      incorrectUserBid: '',
      winner: false,
      timer: {
        days: 0,
        hours: 0,
        minutes: 0,
        seconds: 0,
      }
    }
  },
  computed: {
    ...mapGetters({
      isLoggedIn: 'isLoggedIn',
    }),
    bidsHistory() {
      return this.bidsHistory.slice(Math.max(this.bidsHistory.length - 5, 0))
    },
  },
  methods: {
    connect() {
      this.biddingSocket = new WebSocket(
          `ws://127.0.0.1:8000/ws/${this.$route.params.id}/?token=${localStorage.getItem('token')}`
      )
      this.biddingSocket.onopen = () => {
        this.biddingSocket.send(JSON.stringify({command: 'get_bids'}))
        this.biddingSocket.onmessage = ({data}) => {
          const parsedData = JSON.parse(data)
          console.log(data)
          console.log(parsedData)
          if (parsedData.command === 'get_bids') {
            this.auction.price = parsedData.bid.price
            this.bidsHistory.push(parsedData.bid)
          }
        }
      }
    },
    disconnect() {
      this.biddingSocket.close()
      this.$router.push({name: 'index'})
    },
    getBiddingItem() {
      axios.get(`/bidding/auctions/${this.$route.params.id}`).then(response => {
        this.auction = response.data
      })
    },
    placeBid() {
      if (this.userBid >= this.auction.price) {
        this.incorrectUserBid = ''
        this.biddingSocket.send(JSON.stringify({
          'command': 'place_new_bid',
          'bid': this.userBid,
          'current_price': this.auction.price,
        }))
      } else {
        this.incorrectUserBid = 'is-invalid'
      }
    },
    countdown() {
      const auctionEndsAt = this.auction.ends_at
      const endingDate = new Date(auctionEndsAt).getTime()

      let timer = setInterval(() => {
        const now = new Date().getTime()
        const difference = endingDate - now

        this.timer.days = Math.floor(difference / (1000 * 60 * 60 * 24))
        this.timer.hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
        this.timer.minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60))
        this.timer.seconds = Math.floor((difference % (1000 * 60)) / 1000)

        if (this.auction.price >= this.auction.winning_price) {
          this.resetCountdown(timer)
          this.finishAuction()
          this.winner = this.auction.winner
        }

        if (difference < 0) {
          this.resetCountdown(timer)
          this.finishAuction()
          if (this.auction.winner) {
            this.winner = this.auction.winner
          }
        }
      })
    },
    resetCountdown(timer) {
      clearInterval(timer)
      this.timer.days = 0
      this.timer.hours = 0
      this.timer.minutes = 0
      this.timer.seconds = 0
    },
    showNewBidMessage() {
      this.newBidMessage = true
      setTimeout(() => this.newBidMessage = false, 3000)
    },
    finishAuction() {
      axios.put(`/bidding/auctions/${this.$route.params.id}/`, {
        'is_finished': true,
      }).then(response => {
        console.log(response.data)
        this.auction = response.data
      })
    },
  },
  watch: {
    bidsHistory: {
      handler(new_value) {
        this.showNewBidMessage()
      },
      deep: true
    },
  },
  created() {
    this.getBiddingItem()
    this.connect()
  },
  mounted() {
    this.countdown()
  }
}
</script>

<style scoped>

</style>