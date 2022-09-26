<template>
  <h1 class="text-center mb-4">Вы точно хотите выйти?</h1>
  <div class="text-center">
    <b-button @click="logout" variant="danger" class="m-2" size="lg" pill>Да</b-button>
    <b-button @click="$router.go(-1)" variant="outline-dark" class="m-2" size="lg" pill>Отмена</b-button>
  </div>
</template>

<script>
export default {
  name: 'LogoutView',
  methods: {
    logout() {
      this.$store.commit('removeUserData')
      this.$router.push({name: 'index'})
    }
  },
}
</script>

<style scoped>

</style>