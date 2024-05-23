<template>
  <q-table
    title="Kunde"
    :rows="rows"
    :columns="columns"
    row-key="name"
    hide-bottom
  >
    <template v-slot:header>
      <q-input v-model="search" placeholder="Kunde suche" outlined />
    </template>
    <template v-slot:body="props">
      <q-tr :props="props">
        <q-td key="name" :props="props">
          {{ props.row.name }}
        </q-td>
        <q-td key="birthdate" :props="props">
          {{ props.row.birthdate }}
        </q-td>
        <q-td key="last_visit" :props="props">
          {{ props.row.last_visit }}
        </q-td>
        <q-td key="action" :props="props">
          <q-btn icon="person" :to="`/tatto/client/${props.row.name}`" />
          <q-btn icon="edit" :to="`/tatto/clients/edit-${props.row.name}`" />
        </q-td>
      </q-tr>
    </template>
  </q-table>
</template>
<script setup>
import { columns, rows } from "assets/dammy";
import { ref } from "vue";
const search = ref("");
</script>

<style scoped></style>
