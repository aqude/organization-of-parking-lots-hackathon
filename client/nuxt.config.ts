export default defineNuxtConfig({
    devtools: {
        enabled: true
    },
    modules: ["@nuxt/ui"],
    plugins: [
        { src: '../plugins/vue-yandex-maps.ts', ssr: false }
    ],
})