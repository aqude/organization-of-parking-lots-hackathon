<script setup>
const focused = useState("global_marker", () => {})
</script>

<template>
    <Transition name="frame">
        <div class="__location-info" v-show="focused">
            <p>Тут немного инфы о парковочном месте и кнопка на страницу "бронирование"</p>
            <br>
            <a href="https://nuxt.com/docs/guide/directory-structure/pages" class="text-blue-400">Инфа по страницам в nuxt</a>
            <br>
            <a href="https://vue-map.netlify.app/" class="text-blue-400">Библиотка для Google карт</a>
            <br>
            <br>
            <p>{{ focused }}</p>
        </div>
    </Transition>
</template>

<style lang="scss" scoped>
.__location-info {
    position: fixed;
    left: 50%;
    bottom: 0;
    z-index: 10;
    margin-bottom: 2rem;
    border-radius: 1rem;
    background-color: rgba(15,15,15);
    padding: 1rem;
    width: 30rem;
    max-width: calc(100% - 5rem);
    translate: -50% 0;
    top: unset;
}

.frame-enter-from, .frame-leave-to {
    top: 100%;
}

@media (max-width: 800px) {
    .__location-info {
        left: 1rem;
        translate: unset;
    }
}
</style>
