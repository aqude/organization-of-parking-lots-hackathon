import { defineNuxtPlugin } from "nuxt/app";
import VueGoogleMaps from '@fawmi/vue-google-maps'

const settings = {
    load: {
        key: 'AIzaSyChk3DaZJFpAA2NEq4zWHfB7xENBYiY34M',
        language: 'ru',
    },
}

export default defineNuxtPlugin((nuxtApp) => {
    nuxtApp.vueApp.use(VueGoogleMaps, settings)
})
