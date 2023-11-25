export default defineNuxtConfig({
    devtools: {
        enabled: true
    },
    modules: ["@nuxt/ui"],
plugins: [
        { src: '../plugins/vue-google-maps.ts', ssr: false }
    ],
})