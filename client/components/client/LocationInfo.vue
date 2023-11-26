<script setup>
import { useStorage } from "@vueuse/core";
import { routerKey } from "vue-router";
const auth_token = useStorage("key", () => undefined);
const focused = useState("global_marker", () => {});

const fullscreen = useState("fullscreen_mode", () => false);
const picked_payment_method = useStorage(
    "picked_payment_method",
    () => undefined,
    undefined,
    {
        serializer: {
            read: (v) => (v ? JSON.parse(v) : null),
            write: (v) => JSON.stringify(v),
        },
    }
);

watchEffect(() => {
    if (!focused.value) setTimeout(() => (fullscreen.value = false), 1000);
});

const reserving = ref(false);

const router = useRouter();

const createReservation = async () => {
    reserving.value = true;
    const { data, error } = await useAPI("/api/v1/reservations/create", {
        headers: {
            Authorization: `Bearer ${auth_token.value}`,
        },
        body: {
            parking_id: focused.value.id,
            payment_method_id: picked_payment_method.value.id,
        },
        method: "post",
    });
    await data.value;
    if (data.value) {
        window.location.replace(`/?space=${focused.value.id}`);
    }
};

const reservations = ref({});

onMounted(() => {
    setTimeout(async () => {
        const { data } = await useAPI("/api/v1/reservations/list", {
            headers: {
                Authorization: `Bearer ${auth_token.value}`,
            },
        });
        await data;
        data.value.forEach((reservation) => {
            let temp = JSON.parse(JSON.stringify(reservation));
            delete temp.parking_id;
            reservations.value[reservation.parking_id] = temp;
        });
    }, 1000);
});

const crv = computed(() => {
    if (!focused.value) return {};
    return reservations.value[focused.value.id];
});
const hours_crv = () => {
    return (Date.now() - Date.parse(crv.value.start_time)) / 1000 / 3600 - 3;
};

const refreshing_pay = ref(false);

const refresh_pay = () => {
    refreshing_pay.value = true;
    setTimeout(() => {
        refreshing_pay.value = false;
    }, 10);
};

const finishParking = async () => {
    const { status } = await useAPI("/api/v1/reservations/delete", {
        headers: {
            Authorization: `Bearer ${auth_token.value}`,
        },
        body: {
            id: crv.value.id
        },
        method: "delete"
    });
    watchEffect((cancel) => {
        if (status.value === "success") window.location.replace(`/?space=${focused.value.id}`);
    })
};
</script>

<template>
    <div
        class="__location-info"
        :class="{ details: fullscreen && !crv, reserved: !!crv, open: !!focused }"
    >
        <template v-if="!crv">
            <div class="flex w-full justify-between">
                <div class="flex flex-col">
                    <p class="text-xl font-semibold">Парковочная зона</p>
                    <p>{{ focused?.description }}</p>
                </div>
                <div class="flex flex-col justify-center items-center">
                    <p class="text-xl font-semibold">{{ focused?.price }}</p>
                    <p>руб/час</p>
                </div>
            </div>
            <hr class="border-white w-10/12 opacity-10" />
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
                <ClientPaymentMethods />
                <div class="options">
                    <UButton
                        :disabled="!picked_payment_method"
                        icon="i-heroicons-check-badge-20-solid"
                        size="xl"
                        class="w-full"
                        @click="createReservation"
                        :loading="reserving"
                        >Я припарковался(ась)</UButton
                    >
                </div>
            </template></template
        >
        <div class="reserved-options" v-else-if="focused">
            <h2 class="text-lg">
                Сумма оплаты -
                <span v-if="!refreshing_pay"
                    >{{ (focused.price * Math.ceil(hours_crv())).toFixed(2) }}₽ ({{ Math.ceil(hours_crv()).toFixed() }}ч.)</span
                >
                <span v-else>...</span>
                <UButton
                    @click="refresh_pay"
                    class="ml-4"
                    color="black"
                    variant="link"
                    size="sm"
                    icon="i-heroicons-arrow-path-solid"
                />
            </h2>
            <hr class="border-white w-10/12 opacity-10" />
            <h2 class="text-xl">Как только вы уедите, нажмите кнопку</h2>
            <div class="buttons flex justify-center gap-4">
                <UButton color="red" variant="soft" @click="finishParking"
                    >Завершить парковку</UButton
                >
            </div>
        </div>
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
    translate: -50% 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
    height: 12rem;
    transition: all 0.3s ease-in-out;
    padding-bottom: 0;
    &.details {
        padding-bottom: 85vh;
    }
    &.reserved {
        padding-bottom: 15rem;
    }
    &.open {
        translate: -50% 0;
    }
    .options {
        width: 15rem;
        max-width: 100%;
    }
    .reserved-options {
        width: 85%;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }
}
</style>
