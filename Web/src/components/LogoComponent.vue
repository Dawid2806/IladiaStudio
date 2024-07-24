<template>
  <div class="logo-wrapper">
    <div class="logo-container">
      <div class="first atteron">Iladia</div>
      <div class="secondery beauty">Studio</div>
    </div>
  </div>
</template>

<script setup></script>

<style scoped lang="scss">
.logo-wrapper {
  position: relative;
  width: 300px;
  height: 300px;
  background: white;
  border-radius: 50%;
  border: 5px solid transparent;
}

.logo-wrapper::before {
  content: "";
  position: absolute;
  top: -10px;
  left: -10px;
  right: -10px;
  bottom: -10px;
  border-radius: 50%;
  animation: rotate 3s forwards infinite;
  background: conic-gradient(
    from 0deg,
    #d4af37,
    #f3e5ab 20%,
    #d4af37 40%,
    #000000 60%,
    #d4af37 80%,
    #f3e5ab 100%
  );
  z-index: -1;
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
