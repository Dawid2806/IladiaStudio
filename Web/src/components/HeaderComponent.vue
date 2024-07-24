

<template>
<div class="header-wrapper">
  <q-carousel
    v-model="slide"

    swipeable
    animated
    control-color="white"
    navigation
    padding
    infinite
    height="96vh"
  >
    <q-carousel-slide v-for="item in headers" :key="item.id" :name="item.id" class="column no-wrap flex-center custom-carusel">
      <q-img
        :src="item.url"
        spinner-color="white"
        class="carusel-img"

      />
    </q-carousel-slide>

  </q-carousel>
    <div class="carusel-info-wraper">
      <div class="carusel-info">
        <h1 class="lobster">Tworzymy sztukę na skórze, która opowiada Twoją historię.
        </h1>
      </div>
      <q-btn class="btn" label="contact" />
    </div>
</div>

</template>
<script setup>
import {ref} from "vue";

const slide = ref(1 )
const lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.'

const headers = [
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
<style scoped lang="scss">
.header-wrapper{
  position: relative;
  .carusel-img{
    width: 100%;
    height: 100%;
    position: relative;
  }
  .carusel-img::after{
    position: absolute;
    content: '';
    inset: 0;
    height: 100%;
    width: 100%;
    padding: 1rem;
    background: black;
    opacity: 0.5;
    z-index: 2;
  }
}
:deep(.q-carousel__control){
  z-index: 4;
}
:deep(.custom-carusel){
  padding: 0;
}
.q-carousel--navigation-bottom.q-carousel--with-padding .q-carousel__slide{
  padding: 0 !important;
}
.carusel-info-wraper{
  position: absolute;
  top: 50%;
  left: 50%;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  transform: translate(-50%, -50%);
  z-index: 3;
  color: white;
  width: 100%;

  .carusel-info {
    background: rgba(0,0,0,0.5);
    border-radius: 1rem;
    box-shadow: 0 0 10px 0 rgba(0,0,0,0.5);
  }
  h1 {
    font-size: 2rem;
    padding: 1rem;
    line-height: normal;
  }
  .btn{
    margin-top: 2rem;
    background-color: #f5f5f5;
    color: black;
    width: 300px;

  }
}
</style>
