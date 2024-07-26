<template>
  <q-card class="q-card-contact-form">
    <q-card-section>
      <q-form @submit="submit">
        <q-input v-model="name" label="Name"/>
        <q-input v-model="email" label="Email"/>
        <q-input v-model="message" label="Message" type="textarea"/>
        <q-btn type="submit" label="Send"/>
      </q-form>
    </q-card-section>
  </q-card>
</template>


<script setup>

import {ref} from "vue";

const submit = (e) => {
  e.preventDefault()
  alert('Form submitted')
}
const name = ref('')
const email = ref('')
const message = ref('')


</script>


<style scoped>
.q-card-contact-form{
  width: 100%;
  margin: 0 auto;
  margin-top: 20px;
}
</style>
