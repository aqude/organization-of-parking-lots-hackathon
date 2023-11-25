<script lang="ts" setup>
import { object, string, type InferType } from "yup";
import type { FormError, FormSubmitEvent } from "#ui/types";

const schema = object({
    username : string().email("Неверный Email").required("Обязательное поле"),
    password: string()
        .min(8, "Слишком короткий пароль")
        .required("Обязательное поле"),
});

type Schema = InferType<typeof schema>;

const state = reactive({
  username : undefined,
  password: undefined,
});

const globalError = ref();
const successfulResponse = ref();

async function onSubmit(event: FormSubmitEvent<Schema>) {
  const { username, password } = event.data;
  const { data, error } = useAPI("/api/v1/user/authentication", {
    body: JSON.stringify({
      username: username,
      password: password,
    }),
    method: "post",
  });

  if (data.value) {
    successfulResponse.value = "successfulResponse";
    console.log(data.value);
    console.log(successfulResponse.value);
  } else {
    switch (error.value?.statusCode) {
      case 422:
        globalError.value = "Неверный логин или пароль";
        break;
      default:
        globalError.value = "Произошла неизвестная ошибка...";
    }
    console.log(globalError.value);
  }
}

watch(state, () => globalError.value = undefined)
</script>

<template>
    <div class="__login">
        <UForm
            :schema="schema"
            :state="state"
            class="flex flex-col space-y-4 w-80"
            @submit="onSubmit"
        >
          <div class="flex flex-row justify-between text-xl pt-10">
            <h1 class="">Вход</h1>
            <nuxt-link to="/auth/signup">
              <h1 style="color: #22C55E" class="">Регистрация</h1>
            </nuxt-link>
          </div>
          <h2>Пожалуйста, заполните нижеприведённые поля для входа в приложение</h2>
            <UFormGroup label="E-mail" name="email">
                <UInput placeholder="example@mail.ru" v-model="state.username"/>
            </UFormGroup>

            <UFormGroup label="Пароль" name="password">
                <UInput v-model="state.password" type="password" />
            </UFormGroup>
			<Transition name="error">
				<p v-show="globalError" class="h-6 text-red-300 mt-4">{{ globalError }}</p>
			</Transition>
            <UButton type="submit" class="grid justify-items-center w-80 mx-auto h-10 text-lg">Войти</UButton>
        </UForm>
    </div>
</template>

<style lang="scss" scoped>
.__login {
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