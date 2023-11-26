<script setup lang="ts">
definePageMeta({
    layout: "empty",
});
import { useStorage } from "@vueuse/core";
const auth_token = useStorage("key", () => undefined);
const router = useRouter();
const {
    query: { id },
} = useRoute();
const payment_id = useStorage("payment_id_in_proccess", () => undefined);
const parking_space = useStorage("parking_space_in_proccess", () => undefined);
const res = await fetch(
    `http://localhost/api/v1/user/payment/method/check/${id}`,
    {
        headers: {
            Authorization: `Bearer ${auth_token.value}` as unknown as string,
        },
    }
);
payment_id.value = id as any;
setTimeout(() => {
    router.push(`/?space=${parking_space.value as any}`);
}, 2000);
</script>

<template>
    <div class="__loading">
        <Icon name="i-svg-spinners-ring-resize" />
    </div>
</template>

<style scoped lang="scss">
.__loading {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 90vh;
    font-size: 3rem;
}
</style>
