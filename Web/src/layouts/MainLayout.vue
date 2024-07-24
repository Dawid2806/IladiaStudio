<template>
  <q-layout view="lHh lpR fff">
    <q-header v-if="router.currentRoute.value.path !== '/'" class="bg-black">
      <q-toolbar class="container">
        <q-btn dense flat round icon="menu" class="mobile-menu"
               @click="toggleLeftDrawer"
               v-show="isSmallScreen" />
        <q-list v-show="!isSmallScreen"  class="flex  container">
          <q-item v-for="item in links" :key="item" clickable v-ripple>
            <router-link :to="item.path">


            <q-item-section>
              {{item.name}}
            </q-item-section>
            </router-link>
          </q-item>

        </q-list>
        <q-btn v-if="router.currentRoute.value.path === '/tattoo'" v-show="!isSmallScreen" to="/nails">Go To Nails</q-btn>
        <q-btn v-if="router.currentRoute.value.path === '/nails'" v-show="!isSmallScreen" to="/tattoo">Go To Tattoo</q-btn>

      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" side="left" bordered>
    </q-drawer>

    <q-page-container >
      <router-view />
    </q-page-container>

    <q-footer v-if="router.currentRoute.value.path !== '/'" class="bg-black text-white">
      <q-toolbar class="container">
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useQuasar } from 'quasar'
import {useRouter} from "vue-router";
const router = useRouter()
const $q = useQuasar()
const leftDrawerOpen = ref(false)
console.log(router.currentRoute.value.path)
const isSmallScreen = computed(() => $q.screen.width < 1024)

function toggleLeftDrawer () {
  leftDrawerOpen.value = !leftDrawerOpen.value
}



const links =[
  {
    name: 'Home',
    path: '/'
  },
  {
    name: 'Abaut',
    path: '#about'
  },
  {
    name: 'Gallery',
    path: '#gallery'
  },
  {
    name: 'Contact',
    path: '#contact'
  }
]


</script>
