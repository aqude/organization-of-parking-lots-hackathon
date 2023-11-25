<script lang="ts" setup>

</script>

<template>
    <div class="__home">
      <nuxt-link to="/profile">
        <Icon name="solar:user-bold" class="iconClient"/>
      </nuxt-link>
        <ClientLocationInfo />
        <ClientGoogleMaps />
    </div>
</template>

<style scoped>
.iconClient {
  position: absolute;
  width: 70px;
  height: 70px;
  padding: 10px;
  z-index: 2;
  right: 0;
}
</style>