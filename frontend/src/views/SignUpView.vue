<template>
  <h2 class="text-center">Зарегистрироваться</h2>
  <div class="row">
    <div class="col-3"></div>
    <div class="col-6">
      <b-form @submit.prevent="submitForm">
        <b-form-group
            id="input-group-1"
            label="Email *"
            label-for="input-1"
        >
          <b-form-input
              id="input-1"
              v-model="form.email"
              type="email"
              :class="errors.email ? 'is-invalid' : ''"
              placeholder="Введите Email"
              required
          ></b-form-input>
          <div v-if="errors.email" id="validationServer03Feedback" class="invalid-feedback">
            <p v-for="error in errors.email" :key="error">{{ error }}</p>
          </div>
        </b-form-group>

        <b-form-group
            id="input-group-2"
            label="Имя *"
            label-for="input-2"
        >
          <b-form-input
              id="input-2"
              v-model="form.first_name"
              type="text"
              :class="errors.first_name ? 'is-invalid' : ''"
              placeholder="Введите ваше имя"
          ></b-form-input>
          <div v-if="errors.first_name" id="validationServer03Feedback" class="invalid-feedback">
            <p v-for="error in errors.first_name" :key="error">{{ error }}</p>
          </div>
        </b-form-group>

        <b-form-group
            id="input-group-3"
            label="Фамилия *"
            label-for="input-3"
        >
          <b-form-input
              id="input-3"
              v-model="form.last_name"
              type="text"
              :class="errors.last_name ? 'is-invalid' : ''"
              placeholder="Введите вашу фамилию"
          ></b-form-input>
          <div v-if="errors.last_name" id="validationServer03Feedback" class="invalid-feedback">
            <p v-for="error in errors.last_name" :key="error">{{ error }}</p>
          </div>
        </b-form-group>

        <b-form-group
            id="input-group-4"
            label="День рождения"
            label-for="input-4"
        >
          <b-form-input
              id="input-4"
              v-model="form.birthday"
              type="date"
              :class="errors.birthday ? 'is-invalid' : ''"
              placeholder="Введите ваш день рождения"
          ></b-form-input>
          <div v-if="errors.birthday" id="validationServer03Feedback" class="invalid-feedback">
            <p v-for="error in errors.birthday" :key="error">{{ error }}</p>
          </div>
        </b-form-group>

        <input @change="getPhoto" type="file" class="py-3">

        <b-form-group
            id="input-group-5"
            label="Номер телефона"
            label-for="input-5"
        >
          <b-form-input
              id="input-5"
              v-model="form.phone"
              type="tel"
              :class="errors.phone ? 'is-invalid' : ''"
              placeholder="Введите номер телефона"
          ></b-form-input>
          <div v-if="errors.phone" id="validationServer03Feedback" class="invalid-feedback">
            <p v-for="error in errors.phone" :key="error">{{ error }}</p>
          </div>
        </b-form-group>

        <b-form-group id="input-group-6" label="Пароль *" label-for="input-6">
          <b-form-input
              id="input-6"
              v-model="form.password"
              type="password"
              placeholder="Введите пароль"
              required
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary" size="lg" pill>Подтвердить</b-button>
      </b-form>
    </div>
    <div class="col-3"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SignUpView',
  data() {
    return {
      form: {
        email: '',
        password: '',
        first_name: '',
        last_name: '',
        birthday: '',
        phone: '',
      },
      selectedPhoto: null,
      errors: '',
    }
  },
  methods: {
    submitForm() {
      const formData = new FormData()
      for (let [key, val] of Object.entries(this.form)) {
        formData.append(key, val)
      }
      formData.append('photo', this.selectedPhoto, this.selectedPhoto.name)
      axios
          .post('/accounts/users/', formData)
          .then(() => {
            const successMessage = true
            this.$router.push({name: 'login', query: { successMessage }})
          })
          .catch((errors) => {
            this.errors = errors.response.data
          })
    },
    getPhoto(event) {
      this.selectedPhoto = event.target.files[0]
    }
  }
}
</script>

<style scoped>

</style>