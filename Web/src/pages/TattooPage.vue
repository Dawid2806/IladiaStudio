<template>
  <q-page class="container">
    <HeaderComponent/>
    <section>
     <LogoComponent text-color="white" />
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate et id pariatur quibusdam rem sunt suscipit tenetur? Minus, nam, quia!</p>
    </section>
    <section>
      <q-img src="public/TattosImages/tatuatorka.jpg" />
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate et id pariatur quibusdam rem sunt suscipit tenetur? Minus, nam, quia!</p>
    </section>

    <section>
      <div>
        <q-icon name="app:money" size="150px" />
        <p>Atrakcyne ceny</p>
      </div>
      <div>
        <q-icon name="app:hygiene" size="150px" />
        <p>Czyszczość i bezpieczęstwo</p>
      </div>
      <div>
        <q-icon name="app:design" size="150px" />
        <p>Kreatywny Design</p>
      </div>
    </section>

<carousel-component/>

    <section>
      <div>
        <h3> Tatto Gutschein als geschenk ! ?</h3>
        <p>Kein problem wir bitten Gutscheine in Wert von 50 bis 200 mit ein jahr gunstig  </p>
      </div>
        <div>
          <q-img src="public/TattosImages/gutschein.jpg" width="300px"   height="300px"         :ratio="16/9"/>
        </div>
    </section>

    <section>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate et id pariatur quibusdam rem sunt suscipit tenetur? Minus, nam, quia!</p>
    </section>

    <section>
          <h3>Addres i informacje </h3>
          <map-component/>
        <contact-form/>

    </section>

  </q-page>
</template>
<script setup>
import HeaderComponent from "components/HeaderComponent.vue";
import LogoComponent from "components/LogoComponent.vue";
import CarouselComponent from "components/CarouselComponent.vue";
import MapComponent from "components/MapComponent.vue";
import ContactForm from "src/ContactForm.vue";
</script>

<style scoped>

section {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 16px 0;
  padding: 16px;
  gap: 16px;
  text-align: center;

}
</style>
