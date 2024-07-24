<template>
  <q-page>
    <div class="startPage">
      <div class="startPageLeft" @click="goTo('tattoo')">
        <h2 class="lobster">Tatto</h2>
        <div class="logo_container">
          <LogoComponent />
        </div>
      </div>
      <div class="startPageRight" @click="goTo('nails')">
        <h2 class="lobster text-black">Nails</h2>
        <div class="logo_container">
          <LogoComponent />
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { useRouter } from "vue-router";
import LogoComponent from "../components/LogoComponent.vue";
const router = useRouter();

const goTo = (path) => {
  router.push(path);
};
</script>
