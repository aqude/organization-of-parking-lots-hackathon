import { defineNuxtPlugin} from "nuxt/app";
import YmapPlugin          from 'vue-yandex-maps'

const settings = {
    apiKey: '6525f186-e537-4763-b4eb-1aebaf1cd42e',
    lang: 'ru_RU',
    coordorder: 'latlong',
    version: '2.1'
}

export default defineNuxtPlugin((nuxtApp) => {
    nuxtApp.vueApp.use(YmapPlugin, settings)
})
