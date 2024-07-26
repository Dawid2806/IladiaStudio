<template>
  <q-layout view="lHh lpR fff">
    <q-header v-if="router.currentRoute.value.path !== '/'" class="bg-black">
      <q-toolbar class="container">
        <q-btn dense flat round icon="menu" class="mobile-menu"
               @click="toggleLeftDrawer"
               v-show="isSmallScreen"/>
        <q-btn :icon="`app:${locale}`" >
          <q-menu
            transition-show="flip-right"
            transition-hide="flip-left"
          >
            <q-list style="min-width: 100px">
              <q-item v-for="lang in languageIcons" :key="lang">
                <q-item-section @click="changeLang(lang.code)"><q-icon :name="`app:${lang.code}`" />{{lang.name}}</q-item-section>
              </q-item>

            </q-list>
          </q-menu>
        </q-btn>
        <q-list v-show="!isSmallScreen" class="flex  container">
          <q-item v-for="item in links" :key="item" clickable v-ripple>
            <router-link :to="item.path">


              <q-item-section>
                {{ item.name }}
              </q-item-section>
            </router-link>
          </q-item>

        </q-list>
        <q-btn v-if="router.currentRoute.value.path === '/tattoo'" v-show="!isSmallScreen" to="/nails">Go To Nails
        </q-btn>
        <q-btn v-if="router.currentRoute.value.path === '/nails'" v-show="!isSmallScreen" to="/tattoo">Go To Tattoo
        </q-btn>

      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" side="left" bordered>

    </q-drawer>

    <q-page-container>
      <router-view/>
    </q-page-container>

    <q-footer v-if="router.currentRoute.value.path !== '/'" class="bg-black text-white">
      <q-toolbar class="container">
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup>
import {ref, computed} from 'vue'
import {useQuasar} from 'quasar'
import {useRouter} from "vue-router";
import {appIcons} from "assets/castom-icons.js";
import {useI18n} from "vue-i18n";

const router = useRouter()
const $q = useQuasar()
const leftDrawerOpen = ref(false)
const isSmallScreen = computed(() => $q.screen.width < 1024)

const { locale } = useI18n({ useScope: 'global' })

console.log(locale.value)

$q.iconMapFn = (iconName) => {
  const icon = appIcons[iconName]
  if (icon !== void 0) {
    return {icon: icon}
  }
}


function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value
}

const lang = [
  {
    name: 'Deutsch',
    code: 'de'
  },
  {
    name: 'English',
    code: 'en'
  },
  {
    name: 'Polski',
    code: 'pl'
  }
]

const changeLang = (code) => {
  locale.value = code;
};

const languageIcons = computed(()=>{
  return lang.filter(item => item.code !== locale.value)

})

const links = [
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
