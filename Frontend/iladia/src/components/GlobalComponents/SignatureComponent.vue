<template>
  <Vue3Signature
    ref="signature1"
    :sigOption="state.option"
    :w="'1280px'"
    :h="'400px'"
    class="example"
  ></Vue3Signature>
  <button @click="save('image/jpeg')">Save</button>
  <button @click="clear">Clear</button>
</template>

<script setup>
import Vue3Signature from "vue3-signature";

import { reactive, ref } from "vue";

const state = reactive({
  count: 0,
  option: {
    penColor: "rgb(0, 0, 0)",
    backgroundColor: "rgb(255,255,255)",
  },
  disabled: false,
});

const signature1 = ref(null);

const save = (t) => {
  console.log(signature1.value.save(t));
};

const clear = () => {
  signature1.value.clear();
};

const undo = () => {
  signature1.value.undo();
};
</script>

<style scoped>
.example {
  margin: 0 auto;
}
</style>
