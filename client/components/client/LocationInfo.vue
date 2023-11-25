<script setup>
const focused = useState("global_marker", () => {});

const fullscreen = ref(false);
</script>

<template>
    <div class="__location-info" v-if="focused" :style="{ height: fullscreen ? '90%' : 'unset'}">
        <!-- <div class="rounded-full bg-white opacity-30 w-10 h-1"/> -->
        <div class="flex w-full justify-between">
            <div class="flex flex-col">
                <p class="text-xl font-semibold">Зона {{ focused.id }}</p>
                <p>{{ focused.address }}</p>
            </div>
            <div class="flex flex-col justify-center items-center">
                <p class="text-xl font-semibold">{{ focused.price }}</p>
                <p>руб/час</p>
            </div>
        </div>
        <hr class="border-white w-10/12">
        <template v-if="!fullscreen">
            <UButton
                class="grid justify-items-center w-80 mx-auto text-lg"
                @click="fullscreen = true"
                >Забронировать</UButton
            >
        </template>
        <template v-else>
            <UButton
                class="grid justify-items-center w-80 mx-auto text-lg"
                @click="fullscreen = false"
                color="black"
                variant="outline"
                >Отмена</UButton
            >
        </template>
    </div>
</template>

<style lang="scss" scoped>
.__location-info {
    position: fixed;
    z-index: 2;
    bottom: 0;
    background-color: rgba(15, 15, 15, 0.9);
    max-width: 800px;
    width: 100%;
    padding: 20px;
    border-radius: 1rem 1rem 0 0;
    left: 50%;
    translate: -50% 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
    height: 10rem;
    transition: all 0.3s;
}
</style>
