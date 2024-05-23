<template>
  <q-page class="q-px-lg">
    <h5 class="h3">Persönliche Daten</h5>

    <q-form class="grid-form">
      <div>
        <span> Vorname </span>
        <q-input v-model="inputs.firstname" outlined />
      </div>
      <div>
        <span> Nachname </span>
        <q-input v-model="inputs.lastname" outlined />
      </div>
      <div>
        <span> Handy nummer </span>
        <q-input v-model="inputs.phone" outlined />
      </div>
      <div>
        <span> Geburstag Datum </span>
        <q-input v-model="inputs.birthdate" outlined />
      </div>
    </q-form>

    <h5>Addresse</h5>
    <q-form class="grid-form">
      <div>
        <span>Straße und Hausnummer </span>
        <q-input v-model="inputs.streetAndNumber" outlined />
      </div>
      <div>
        <span>Stadt</span>
        <q-input v-model="inputs.city" outlined />
      </div>
      <div>
        <span>Postleitzahl</span>
        <q-input v-model="inputs.postcode" outlined />
      </div>
    </q-form>

    <h5>Einwilligung zur Verarbeitung personenbezogener Daten:</h5>
    <q-form>
      <q-checkbox v-model="inputs.personalData">
        <p>
          Wir werden von dem fer! ggestellten Werk Lichtbildaufnahmen fer! gen.
          Der Kunde/die Kundin willigt hiermit ausdrücklich darin ein, dass
          diese Lichtbilder jenseits eines gemäß Art. 6 Absatz 1(f) EU-DSGVO
          zulässigen Zwecks zum Zwecke der Außendarstellung auf unserer Website,
          unseren Social Media Auftri" en (Facebook, Instagram, Twi" er usw.)
          oder auf Werbebannern verö# entlich werden.
        </p>
        <br />

        <p>
          Diese Einwilligung kann uns gegenüber jederzeit widerrufen werden
          (Art. 7 Abs. 3 EU-DSGVO). Hiernach dürfen wir die Verarbeitung der
          unter der Einwilligung erhobenen und/oder verwendeten Lichtbilder
          nicht mehr fortsetzen. Die erhobenen Gesundheitsdaten werden – da
          deren Verarbeitung bis zum Zeitpunkt des Widerrufs legi! m ist – bis
          zum Ablauf der Aufbewahrungsfrist verwahrt.
        </p>
      </q-checkbox>
    </q-form>

    <h5>Unterschrift :</h5>
    <MySignaturePad @update-signatur="updateSignatureData" />
    <div>
      <q-btn @click="submit" label="dodaj"></q-btn>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from "vue";
import HealtyForm from "components/TattoComponents/HealtyForm.vue";
import MySignaturePad from "components/GlobalComponents/SignatureComponent.vue";

const inputs = ref({
  firstname: "",
  lastname: "",
  phone: "",
  birthdate: "",
  streetAndNumber: "",
  city: "",
  postcode: "",
  personalData: false,
  healthData: {},
  signature: "",
});

const updateHealthData = (data) => {
  inputs.value.healthData = data;
};
const updateSignatureData = (data) => {
  inputs.value.signature = data;
};
const submit = () => {
  console.log(inputs.value);
};
</script>

<style scoped></style>
