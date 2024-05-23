<template>
  <Vue3Signature
    ref="signature1"
    :sigOption="state.option"
    :w="'100%'"
    :h="'150px'"
    class="example"
  ></Vue3Signature>
</template>

<script setup>
import Vue3Signature from "vue3-signature";

import { reactive, ref, watch } from "vue";

const emit = defineEmits(["update-signatur"]);

const state = reactive({
  count: 0,
  option: {
    penColor: "rgb(0, 0, 0)",
    backgroundColor: "rgb(200,200,200, 0.5)",
  },
  disabled: false,
});

const signature1 = ref(null);

const save = (t) => {
  console.log(signature1.value.save(t));
};
const emitData = () => {
  emit("update-signatur", signature1.value.save("image/jpeg"));
};
const clear = () => {
  signature1.value.clear();
};
watch(signature1, emitData, {
  deep: true,
});
</script>

<style scoped>
.example {
  margin: 0 auto;
}
</style>
