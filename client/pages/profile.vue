<script setup>
import { useStorage } from "@vueuse/core";
const auth_token = useStorage("key", () => undefined);
const me = ref();
const loading = ref(true);
const router = useRouter();

const logout = () => {
    auth_token.value = undefined;
    router.push("/auth/login");
};

onMounted(() => {
    setTimeout(async () => {
        if (!auth_token.value || auth_token.value === "undefined") {
          loading.value = false
          return
        }
        const { data, status } = await useAPI("/api/v1/user/me", {
            headers: {
                Authorization: `Bearer ${auth_token.value}`,
            },
        });
        watchEffect((stop) => {
            if (status.value === "success") {
                stop();
                loading.value = false;
                me.value = data.value;
            }
        });
    }, 1000);
});
</script>

<template>
    <div class="__profile">
        <template v-if="loading">
            <Icon class="text-3xl" name="i-svg-spinners-ring-resize" />
        </template>
        <template v-else-if="me">
            <h1 class="text-3xl">{{ me.second_name }} {{ me.first_name }}</h1>
            <hr class="border-white w-full opacity-50" />
            <h2 class="text-2xl text-semibold">Методы оплаты</h2>
            <ClientPaymentMethods />
            <UButton color="red" variant="soft" size="xl" @click="logout">
                Выйти
            </UButton>
        </template>
        <template v-else>
            <h1 class="text-3xl">Вы не автроизованы</h1>
            <hr class="border-white w-full opacity-50" />
            <UButton variant="soft" size="xl" to="/auth/login">
                Авторизоваться
            </UButton>
            <UDivider label="ИЛИ" />
            <UButton variant="soft" size="xl" to="/auth/signup">
                Зарегестрироваться
            </UButton>
        </template>
    </div>
</template>

<style scoped lang="scss">
.__profile {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    align-items: center;
    padding: 0 1rem;
    padding-top: 5rem;
    max-width: 20rem;
    margin: 0 auto;
    overflow-y: auto;
    max-height: 100vh;
}
</style>
