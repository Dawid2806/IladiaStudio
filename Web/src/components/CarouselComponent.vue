

<template>
  <Carousel v-bind="settings" :breakpoints="breakpoints"  >
    <Slide class="slide-container" v-for="item in slide" :key="item">
        <q-img class="slide-img" :src="item.url" />
    </Slide>

    <template #addons>
      <Navigation />
    </template>
  </Carousel>
</template>


<script setup>
import { Carousel, Navigation, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'
const settings =  {
  itemsToShow: 1,
  snapAlign: 'center',
  infinite: true,
  wrapAround: true,
  navigation: true,
}
const breakpoints = {
  700: {
    itemsToShow: 2.5,
      snapAlign: 'center',
  },
  1024: {
    itemsToShow: 3,
      snapAlign: 'start',
  },
}

const slide = [
  {
    id: 1,
    url:'public/tattosImages/1.jpg'
  },
  {
    id: 2,
    url:'public/tattosImages/2.webp'
  },{
    id: 3,
    url:'public/tattosImages/3.jpg'
  }
  ,{
    id: 4,
    url:'public/tattosImages/4.jpg'
  }
]



</script>


<style scoped>
.slide-container{
  display: flex;
  gap: 20px;
}
.slide-img{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.5);
  margin: 0 8px;
}
</style>
