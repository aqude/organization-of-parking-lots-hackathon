<script lang="ts" setup></script>

<template>
    <div class="__methods">
        <div class="method">
            <hr style="width: 80vw; border-color: white" />
        </div>
        <div class="add">
            <h2 class="text-3xl">Добавить метод</h2>
            <UButton size="xl" variant="soft">
                <Icon name="i-fluent-emoji-credit-card" />
                Банковская карта
            </UButton>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.__methods {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 1rem;
    border: 1px solid rgb(var(--color-primary-DEFAULT));
    background-color: rgba(0, 0, 0, 0.5);
    padding: 1rem;
    .add {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }
}
</style>
