<script lang="ts" setup>
const route = useRoute()
</script>

<template>
    <header class="h-16">
        <UButton
            icon="i-heroicons-arrow-left-20-solid"
            variant="soft"
            class="back btn"
            to="/"
            :style="{ opacity: route.path === '/' ? 0 : 1 }"
        />
        <UButton
            icon="i-heroicons-user-solid"
            variant="soft"
            class="profile btn"
            to="/profile"
            :style="{ opacity: route.path === '/profile' ? 0 : 1 }"
        />
    </header>
</template>

<style lang="scss" scoped>
header {
    position: fixed;
    z-index: 2;
    width: 100%;
    display: flex;
    gap: 1rem;
    justify-content: space-between;
    .btn {
        aspect-ratio: 1;
        display: flex;
        justify-content: center;
        transition: opacity 0.3s;
        &.back {
            border-radius: 0 0 1rem 0;
        }
        &.profile {
            border-radius: 0 0 0 1rem;
        }
    }
}
</style>
