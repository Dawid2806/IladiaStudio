<template>
  <q-page class="flex justify-center items-center">
    <q-form>
      <div>
        <span>Login</span>
        <q-input v-model="inputs.login" outlined />
      </div>
      <div>
        <span>Password</span>
        <q-input v-model="inputs.password" outlined />
      </div>
      <q-btn label="Anmelden" @click="submit" />
    </q-form>
  </q-page>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const inputs = ref({
  login: "",
  password: "",
});
const submit = () => {
  router.push("/tatto");
};
</script>
