<script lang="ts" setup>
import { object, string, type InferType } from "yup";
import type { FormError, FormSubmitEvent } from "#ui/types";

const schema = object({
    email: string().email("Неверный Email").required("Обязательное поле"),
    password: string()
        .min(8, "Слишком короткий пароль")
        .required("Обязательное поле"),
});

type Schema = InferType<typeof schema>;

const state = reactive({
    email: undefined,
    password: undefined,
    phone: undefined,
});

const globalError = ref();

async function onSubmit(event: FormSubmitEvent<Schema>) {
    const { email, password, phone } = event.data;
    const { data, error } = useAPI("/api/v1/user/registration", {
        body: {
            phone: phone,
            email: email,
            password: password,
        },
        method: "post",
    });
	console.log(data.value)
    if (data.value) {
    } else {
        switch (error.value?.statusCode) {
            case 422:
                globalError.value = "Неверный логин или пароль";
            default:
                globalError.value = "Произошла неизвестная ошибка...";
        }
		console.log(globalError.value)
    }
}
watch(state, () => globalError.value = undefined)
</script>

<template>
    <div class="__signup">
        <UForm
            :schema="schema"
            :state="state"
            class="flex flex-col space-y-4 form-wrapper"
            @submit="onSubmit"
        >
            <h1 class="text-center text-3xl">Регистрация</h1>
            <hr style="border-color: rgb(var(--color-primary-DEFAULT) / 0.8);">
            <UFormGroup label="Email" name="email">
                <UInput placeholder="example@mail.ru" v-model="state.email" />
            </UFormGroup>

            <UFormGroup label="Пароль" name="password">
                <UInput v-model="state.password" type="password" />
            </UFormGroup>
			<Transition name="error">
				<p v-show="globalError" class="h-6 text-red-400 mt-4">{{ globalError }}</p>
			</Transition>

            <UButton type="submit" class="w-fit">Войти</UButton>
        </UForm>
    </div>
</template>

<style lang="scss" scoped>
.__signup {
    display: flex;
    flex-direction: column;
    align-items: center;
    .form-wrapper {
        width: 25rem;
        max-width: 90%;
        border-radius: 1rem;
        border: 1px solid rgb(var(--color-primary-DEFAULT) / 0.8);
        padding: 2rem;
    }
}

.error-enter-active, .error-leave-active {
	transition: all 0.3s;
}
.error-enter-from, .error-leave-to {
	opacity: 0;
	height: 0;
	width: fit-content;
	margin: 0 !important;
    overflow: hidden;
}
</style>