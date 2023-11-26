<script lang="ts" setup>
import { useStorage } from "@vueuse/core";
const auth_token = useStorage("key", () => undefined);
const parking_space = useStorage("parking_space_in_proccess", () => undefined);
const parking_space_picked = useState("global_marker", () => {});
const payment_id = useStorage("payment_id_in_proccess", () => undefined);
const add_method = async () => {
    const { data } = await useAPI("/api/v1/user/payment/method/add", {
        headers: {
            Authorization: `Bearer ${auth_token.value}` as unknown as string,
        },
        body: {
            type: "bank_card",
        },
        method: "post",
    });
    if (parking_space_picked.value) parking_space.value = (parking_space_picked.value as any).id;
    const { payment_url } = data.value as any;
    window.location.replace(payment_url);
};

const { data: methods_data } = await useAPI(
    "/api/v1/user/payment/method/list",
    {
        headers: {
            Authorization: `Bearer ${auth_token.value}` as unknown as string,
        },
    }
);

let methods = methods_data.value as any[];

const picked = useStorage("picked_payment_method", () => undefined, undefined, {
  serializer: {
    read: (v) => (v ? JSON.parse(v) : null),
    write: (v) => JSON.stringify(v),
  },
});
</script>

<template>
    <div class="__methods">
        <template v-for="method in methods">
            <div class="method">
                <Icon class="text-xl" name="i-fluent-emoji-credit-card" />
                <h2 class="font-semibold text-lg">{{ method.title }}</h2>
                <UButton
                    @click="picked = method"
                    style="margin-left: auto"
                    :variant="picked && (picked.id === method.id) ? 'soft' : 'solid'"
                    :disabled="picked && (picked.id === method.id)"
                    >{{ picked && (picked.id === method.id) ? 'Выбранный метод' : 'Выбрать' }}</UButton
                >
            </div>
            <hr style="width: 95%; opacity: 0.25; border-color: white" />
        </template>
        <div class="add">
            <h2 class="text-2xl">Добавить метод</h2>
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
        align-items: center;
        gap: 1rem;
        width: 100%;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
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
