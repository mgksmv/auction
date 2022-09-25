import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios';

// BootstrapVue 3
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

// Font Awesome
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)
app.use(router, axios)
app.use(store)
app.use(BootstrapVue3)

app.component('font-awesome-icon', FontAwesomeIcon)
library.add(fas)

// Local styles
import './assets/style.css'

app.mount('#app')
