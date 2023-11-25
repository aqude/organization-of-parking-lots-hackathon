<script lang="ts" setup>
import { object, string, type InferType } from "yup";
import type { FormError, FormSubmitEvent } from "#ui/types";
let requiredField = "Обязательное поле";
const schema = object({
    email: string().email("Неверный Email").required(requiredField),
    password: string()
        .min(8, "Слишком короткий пароль")
        .required(requiredField),
  first_name: string().required(requiredField),
  second_name: string().required(requiredField),
  last_name: string().required(requiredField),
});

type Schema = InferType<typeof schema>;

const state = reactive({
  first_name: undefined,
  second_name: undefined,
  last_name: undefined,
  email: undefined,
  password: undefined,
});

const globalError = ref();
const successfulResponse = ref();

async function onSubmit(event: FormSubmitEvent<Schema>) {
    const { email, password, first_name, second_name, last_name } = event.data;
    const { data, error } = useAPI("/api/v1/user/registration", {
        body: JSON.stringify({
          first_name: first_name,
          second_name: second_name,
          last_name: last_name,
          email: email,
          password: password,
        }),
        method: "post",
    });

	console.log(event.data)
    if (data.value) {
      successfulResponse.value = "successfulResponse"
      console.log(data.value)
      console.log(successfulResponse.value)
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
            class="flex flex-col space-y-4 w-80"
            @submit="onSubmit"
        >
          <div class="flex flex-row justify-between text-xl pt-10">
            <h1 class="">Регистрация</h1>
            <nuxt-link to="/auth/login">
              <h1 style="color: #22C55E" class="">Вход</h1>
            </nuxt-link>
          </div>
          <h2>Пожалуйста, заполните нижеприведённые поля для входа в приложение</h2>
          <UFormGroup label="Имя" name="first_name">
            <UInput placeholder="Иван" v-model="state.first_name" />
          </UFormGroup>
          <UFormGroup label="Фамилия" name="second_name">
            <UInput placeholder="Иванов" v-model="state.second_name" />
          </UFormGroup>
          <UFormGroup label="Отчество" name="last_name">
            <UInput placeholder="Иванович" v-model="state.last_name" />
          </UFormGroup>
            <UFormGroup label="Email" name="email">
                <UInput placeholder="example@mail.ru" v-model="state.email" />
            </UFormGroup>

            <UFormGroup label="Пароль" name="password">
                <UInput v-model="state.password" type="password" />
            </UFormGroup>
			<Transition name="error">
				<p v-show="globalError" class="h-6 text-red-400 mt-4">{{ globalError }}</p>
			</Transition>
            <UButton type="submit" class="grid justify-items-center w-80 mx-auto h-10 text-lg">Зарегистрироваться</UButton>
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