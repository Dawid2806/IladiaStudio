<template>
  <q-page>
    <div class="startPage">
      <div class="startPageLeft" @click="goTo('tattoo')">
        <h2>Tatto</h2>
        <div class="logo_container">
          <img src="/images/logo2.png" alt="" />
        </div>
      </div>
      <div class="startPageRight" @click="goTo('nails')">
        <h2>Tatto</h2>

        <div class="logo_container">
          <img src="/images/logo2.png" alt="" />
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const goTo = (path) => {
  router.push(path);
};
</script>
