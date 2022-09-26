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
            if (localStorage.getItem('token') || state.user === undefined) {
                state.user.token = localStorage.getItem('token')
                state.user.meta = {
                    email: localStorage.getItem('email'),
                    first_name: localStorage.getItem('first_name'),
                    last_name: localStorage.getItem('last_name'),
                    photo: localStorage.getItem('photo'),
                    phone: localStorage.getItem('phone'),
                    birthday: localStorage.getItem('birthday'),
                }
                state.isAuthenticated = true
            } else {
                state.user.token = null
                state.user.meta = null
                state.isAuthenticated = false
            }
        },
        setUserData(state, data) {
            state.isAuthenticated = true
            state.user.token = data.token
            state.user.meta = {
                email: data.email,
                first_name: data.first_name,
                last_name: data.last_name,
                photo: data.photo,
                phone: data.phone,
                birthday: data.birthday,
            }
            localStorage.setItem('token', data.token)
            localStorage.setItem('email', data.email)
            localStorage.setItem('first_name', data.first_name)
            localStorage.setItem('last_name', data.last_name)
            localStorage.setItem('photo', data.photo)
            localStorage.setItem('phone', data.phone)
            localStorage.setItem('birthday', data.birthday)
        },
        removeUserData(state) {
            state.user.token = null
            state.user.meta = null
            state.isAuthenticated = false
            localStorage.clear()
        }
    },
    getters: {
        isLoggedIn: state => state.isAuthenticated,
        user: state => state.user,
    }
})
