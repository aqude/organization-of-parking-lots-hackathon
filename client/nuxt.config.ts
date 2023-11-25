export default defineNuxtConfig({
    devtools: {
        enabled: true
    },
    modules: ["@nuxt/ui", "nuxt-icon"],
plugins: [
        { src: '../plugins/vue-google-maps.ts', ssr: false }
    ],
})