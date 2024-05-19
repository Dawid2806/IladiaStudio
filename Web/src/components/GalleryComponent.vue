<template>
  <q-scroll-area style="height: 500px">
    <div class="grid-wrapper">
      <q-img v-for="(img, index) in images" :key="index" :class="getImageClass(index)" @click="showImage(index)" :src="img.src" />
    </div>
    <q-btn label="Pokaż więcej" @click="loadMoreImages" class="q-mt-md" />

  </q-scroll-area>
    <q-dialog v-model="dialog" transition-show="slide-up" transition-hide="slide-down">
      <q-card>
        <q-card-section class="row items-center q-pa-none">
          <q-btn flat round icon="close" @click="dialog = false" />
          <q-img :src="currentImage.src" style="height: 500px; width: 500px;" />
        </q-card-section>
      </q-card>
    </q-dialog>
</template>


<script setup>
import {computed, ref} from "vue";

const images =ref(  [
  { src: 'https://cdn.quasar.dev/img/mountains.jpg' },
  { src: 'https://cdn.quasar.dev/img/mountains.jpg' },
  { src: 'https://cdn.quasar.dev/img/mountains.jpg' },
  { src: 'https://cdn.quasar.dev/img/mountains.jpg' },
  { src: 'https://cdn.quasar.dev/img/mountains.jpg' },
  { src: 'https://cdn.quasar.dev/img/mountains.jpg' },
  { src: 'https://cdn.quasar.dev/img/mountains.jpg' },
  { src: 'https://cdn.quasar.dev/img/mountains.jpg' },
  { src: 'https://cdn.quasar.dev/img/mountains.jpg' },
  { src: 'https://cdn.quasar.dev/img/mountains.jpg' },




])
const dialog = ref(false);
const currentImageIndex = ref(0);
const currentImage = computed(() => images.value[currentImageIndex.value]);

const showImage = (index) => {
  currentImageIndex.value = index;
  dialog.value = true;
}

const getImageClass = (index) => {
  return `item-${index % 15 + 1}`; // Przykład z cyklem 15 różnych stylów
}
const loadMoreImages = () => {
  const moreImages = [
    { src: 'https://cdn.quasar.dev/img/mountains.jpg' }, // przykład, powtórz obrazy
    // dodaj więcej obrazów
  ];
  images.value = [...images.value, ...moreImages];
}
</script>
<style >

.grid-wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
.item-1 { grid-row: span 3; }
.item-2 { grid-row: span 2; }
.item-3 { grid-row: span 1; }
.item-4 { grid-row: span 4; }
.item-5 { grid-row: span 3; }
.item-6 { grid-row: span 2; }
.item-7 { grid-row: span 5; }
.item-8 { grid-row: span 3; }
.item-9 { grid-row: span 4; }
.item-10 { grid-row: span 2; }
.item-11 { grid-row: span 3; }
.item-12 { grid-row: span 1; }
.item-13 { grid-row: span 2; }
.item-14 { grid-row: span 5; }
.item-15 { grid-row: span 3; }
</style>
