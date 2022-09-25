import { createStore } from 'vuex';

export default createStore({
    state: {
        user: {
            token: null,
            meta: null,
        },
        isAuthenticated: false,
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('token')) {
                state.user.token = localStorage.getItem('token')
                state.user.meta = {
                    email: localStorage.getItem('email'),
                    first_name: localStorage.getItem('first_name'),
                    last_name: localStorage.getItem('last_name'),
                }
                state.isAuthenticated = true
            } else {
                state.user.token = null
                state.isAuthenticated = false
            }
        },
        setToken(state, token) {
            state.user.token = token
            state.isAuthenticated = true
        },
        setMeta(state, data) {
            state.user.meta = {
                email: data.email,
                first_name: data.first_name,
                last_name: data.last_name,
            }
        },
        removeToken(state) {
            state.user.token = null
            state.user.meta = null
            state.isAuthenticated = false
            localStorage.removeItem('token')
        }
    },
    getters: {
        isLoggedIn: state => state.isAuthenticated,
        user: state => state.user,
    }
})
