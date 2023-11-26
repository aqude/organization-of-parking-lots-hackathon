<script lang="ts" setup>
import { useStorage } from "@vueuse/core";
const auth_token = useStorage("key", () => undefined);
const add_method = async () => {
    const { data, error } = await useAPI("/api/v1/user/payment/method/add", {
        headers: {
            Authorization: `Bearer ${auth_token.value}` as unknown as string
        },
        body: {
            type: "bank_card"
        },
        method: "post"
    })
    console.log(data.value)
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
