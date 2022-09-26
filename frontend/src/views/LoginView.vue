<template>
  <h2 class="text-center">Войти</h2>
  <div class="row">
    <div class="col-3"></div>
    <div class="col-6">
      <div v-if="successMessage">
        <b-alert show dismissible>
          Вы успешно зарегистрировались! Теперь можете войти.
        </b-alert>
      </div>
      <b-form @submit.prevent="submitForm">
        <b-form-group
            id="input-group-1"
            label="Email:"
            label-for="input-1"
        >
          <b-form-input
              id="input-1"
              v-model="email"
              type="email"
              :class="incorrectCredentials"
              placeholder="Введите Email"
              required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Пароль:" label-for="input-2">
          <b-form-input
              id="input-2"
              v-model="password"
              type="password"
              :class="incorrectCredentials"
              placeholder="Введите пароль"
              required
          ></b-form-input>
          <div v-if="incorrectCredentials" id="validationServer03Feedback" class="invalid-feedback">
            Неверные данные!
          </div>
        </b-form-group>

        <b-button type="submit" variant="primary" size="lg" pill>Войти</b-button>
      </b-form>
    </div>
    <div class="col-3"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginView',
  data() {
    return {
      email: '',
      password: '',
      incorrectCredentials: '',
      successMessage: this.$route.query.successMessage
    }
  },
  methods: {
    submitForm() {
      axios
          .post('/api-token-auth/', {'username': this.email, 'password': this.password})
          .then(response => {
            const data = response.data
            axios.defaults.headers.common['Authorization'] = `Token ${data.token}`
            this.$store.commit('setUserData', data)
            this.$router.push({name: 'index'})
          })
          .catch(error => {
            console.log(error)
            this.incorrectCredentials = 'is-invalid'
          })
    }
  }
}
</script>