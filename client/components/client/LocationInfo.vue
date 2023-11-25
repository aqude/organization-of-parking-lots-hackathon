<script setup>
const focused = useState("global_marker", () => {})
</script>

<template>
    <Transition name="frame">
      <div class="flex items-center justify-center" v-show="focused">
        <div class="__location-info">
          <div class="row flex flex-row justify-between">
            <div class="half-column flex flex-col">
              <a class="text-xl font-semibold">Зона {{ focused.id }}</a>
              <a>ул. Высоковольтная, 123</a>
            </div>
            <div class="half-column flex flex-col justify-center items-center">
              <a class="text-xl font-semibold">45</a>
              <a>руб/час</a>
            </div>
          </div>
          <UButton class="grid justify-items-center w-80 mx-auto text-lg mt-5">Забронировать</UButton>
        </div>
      </div>
    </Transition>
</template>

<style lang="scss" scoped>
.__location-info {
  position: absolute;
  z-index: 2;
  bottom: 0;
  background-color: rgba(15, 15, 15);
  max-width: 800px;
  width: 100%;
  padding: 20px;
}


.frame-enter-from, .frame-leave-to {
    top: 100%;
}

@media (max-width: 800px) {
    .__location-info {
        translate: unset;
    }
}
</style>
