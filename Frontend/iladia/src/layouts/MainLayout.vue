<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="page-bg text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer"/>
        <q-toolbar-title>
          Iladia Studio
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" bordered>
      <q-list bordered class="rounded-borders">
        <q-expansion-item
          expand-separator
          label="Tatto"
        >
          <q-card>
            <q-card-section>
              <!--              TODO Dodać tutaj linki dla tatuazy-->
              <router-link to="/tatto/">Dashboard</router-link>

              <q-expansion-item
                expand-separator
                label="Clients"
              >
                <q-card>
                  <q-card-section class='column'>
                    <!--              TODO Dodać tutaj linki dla tatuazy-->
                  <router-link to="/tatto/clients">Lista clientów</router-link>
                    <router-link to="/tatto/clients/add-new">Add new</router-link>

                  </q-card-section>
                </q-card>
              </q-expansion-item>

            </q-card-section>
          </q-card>
        </q-expansion-item>

        <q-expansion-item
          expand-separator
          label="Nails"
        >
          <q-card>
            <q-card-section>
              <!--              TODO Dodać tutaj linki dla Paznokci-->
              <router-link to="/nails/">Dashboard</router-link>

              <q-expansion-item
                expand-separator
                label="Clients"
              >
                <q-card>
                  <q-card-section class='column'>
                    <!--              TODO Dodać tutaj linki dla tatuazy-->
                    <router-link to="/nails/clients">Lista clientów</router-link>
                    <router-link to="/nails/clients/add-new">Add new</router-link>

                  </q-card-section>
                </q-card>
              </q-expansion-item>
            </q-card-section>
          </q-card>
        </q-expansion-item>


      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view/>
    </q-page-container>

  </q-layout>
</template>

<script>
import {ref} from 'vue'

export default {
  setup() {
    const leftDrawerOpen = ref(false)

    return {
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
}
</script>
