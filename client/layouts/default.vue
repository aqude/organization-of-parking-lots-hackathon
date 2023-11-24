<script lang="ts" setup></script>

<template>
    <ClientHeader />
    <main class="__main">
        <slot />
    </main>
</template>

<style lang="scss" scoped>
main.__main {
    padding: 2rem 0;
}
</style>
