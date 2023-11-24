import Vue from 'vue'
import YmapPlugin from 'vue-yandex-maps'

const settings = {
    apiKey: '6525f186-e537-4763-b4eb-1aebaf1cd42e', // Укажите свой API-ключ от Yandex Maps
    lang: 'ru_RU',
    coordorder: 'latlong',
    version: '2.1'
}

Vue.use(YmapPlugin, settings)

export default {}