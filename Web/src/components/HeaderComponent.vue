

<template>
<header class="header">
  <div class="text-box">
    <h1 class="lobster">Studio Tatuażu Iladia </h1>
    <p>Profesionalne podjescie, bezpieczenstwo oraz komfort jest dla nas bardzo wazny ! </p>
  </div>

</header>

</template>
<script setup>
import {ref} from "vue";

const slide = ref(1 )
const lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.'



</script>
<style scoped lang="scss">
.header {
  position: relative;
  width: 100%;
  height: 500px;
  background: url("public/tattosImages/studio.png") no-repeat center center;
  background-size: cover;
  &::before{
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.7);

  }
  .text-box{
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    z-index: 2;

    h1{
      font-size: 3rem;
      margin: 0;

    }
  }
}

</style>
<!--<div class="carusel-info-wraper">-->
<!--<div class="carusel-info">-->
<!--  </h1>-->

<!--</div>-->
<!--<q-btn class="btn" label="contact" />-->
<!--</div>-->
