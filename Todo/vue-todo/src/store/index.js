import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state : {
        backendUrl: process.env.VUE_APP_BACKEND_HOST || 'http://127.0.0.1:8000/api/'
    },
    mutations: {},
    actions : {},
    modules : {},
    getters: {
        getBackendUrl: state => {
            return state.backendUrl;
        }
    }
})

export default store