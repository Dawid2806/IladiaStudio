<template>
 <q-page >


   <div class="startPage" >
     <div class="startPageLeft" @click="goTo('tattoo')">
       <div class="logo_container">
       <img src="/images/logo2.png" alt="">
         <h2>tatto</h2>
       </div>
       </div>
     <div class="startPageRight" @click="goTo('nails')">
     <div class="logo_container">
       <img src="/images/logo2.png" alt="">
       <h2>nails</h2>

     </div>
     </div>
   </div>
 </q-page>
</template>

<script setup>
import {useRouter} from "vue-router";

const router = useRouter()

const goTo= (path) => {
  router.push(path)
}

</script>
