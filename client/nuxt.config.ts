export default defineNuxtConfig({
    devtools: {
        enabled: false
    },
    modules: ["@nuxt/ui", "nuxt-icon"],
    css: [
        "@/assets/style.scss"
    ],
    app: {
        pageTransition: {
            name: "page",
            mode: "out-in"
        }
    },
    build: {
        transpile: ['@fawmi/vue-google-maps']
    },
    plugins: [
        { src: '../plugins/vue-google-maps.ts', ssr: false }
    ],
})