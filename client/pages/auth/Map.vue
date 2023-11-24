<script setup>
import {YandexMap} from "vue-yandex-maps";
const coordinates = [55, 33];
const controls = ['fullscreenControl'];
const detailedControls = { zoomControl: { position: { right: 10, top: 50 } } };

</script>

<template>
  <client-only>
      <YandexMap
          :coordinates="coordinates"
          :detailed-controls="detailedControls"
          :controls="controls"
          map-type="hybrid"
      />
  </client-only>
</template>

<style>
.yandex-container {
  height: 400px;
}
</style>