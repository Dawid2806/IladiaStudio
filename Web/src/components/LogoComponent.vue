<template>


    <div class="logo-wrapper">
      <div class="logo-container">
        <div class="first atteron" :style="{color:textColor}">Iladia</div>
        <div class="secondery beauty " :style="{color:textColor} ">Studio</div>
      </div>
    </div>
  <div class="avatar">
  </div>
</template>

<script setup>

const props = defineProps({
  textColor: {
    type: String,
    default: "black",
  },
});

</script>

<style scoped lang="scss">



.logo-wrapper {
  position: relative;
  z-index: 0;
  width: 300px;
  height: 300px;
}

.logo-wrapper:before {
  width: 300px;
  height: 300px;
  aspect-ratio: 1;
  content: "";
  position: absolute;
  z-index: -1;
  inset: 0;
  padding: 8px;
  border-radius: 100%;
  background:  conic-gradient(
      from 0deg,
      #D4AF37,
      #F3E5AB 20%,
      #D4AF37 40%,
      #000000 60%,
      #D4AF37 80%,
      #F3E5AB 100%
  );
  -webkit-mask: linear-gradient(#fff 0 0) content-box,
  linear-gradient(#fff 0 0);
  mask: linear-gradient(#fff 0 0) content-box,
  linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: rotate 3s linear infinite;
}



.logo-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: black;

  div.first {
    font-size: 6rem;
    margin-right: 4rem;
    margin-bottom: 2rem;
  }

  div.secondery {
    font-size: 8rem;
    position: absolute;
    top: 50%;
    transform: translate(20%, -50%);
    margin-top: 3rem;
    right: 0;
  }
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
