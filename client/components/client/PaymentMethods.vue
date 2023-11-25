<script lang="ts" setup>
const add_method = () => {
    const { data: { value } } = useAPI("/api/v1/user/payment/method/add")
    console.log(value)
}
</script>

<template>
    <div class="__methods">
        <div class="method">
            <h2></h2>
            <hr style="width: 95%; opacity: 0.25; border-color: white;" />
        </div>
        <div class="add">
            <h2 class="text-3xl">Добавить метод</h2>
            <UButton size="xl" variant="soft" @click="add_method">
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
    gap: 1rem;

    .method {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
        width: 100%;
    }
    .add {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }
}
</style>
