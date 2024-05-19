<template>
  <q-page>
    <h5 class="h3">Persönliche Daten</h5>

    <q-form class="grid-form">
      <div>
        <span> Vorname </span>
        <q-input v-model="inputs.firstname" />
      </div>
      <div>
        <span> Nachname </span>
        <q-input v-model="inputs.lastname" />
      </div>
      <div>
        <span> Handy nummer </span>
        <q-input v-model="inputs.phone" />
      </div>
      <div>
        <span> Geburstag Datum </span>
        <q-input v-model="inputs.birthdate" />
      </div>
    </q-form>
    <h5>Addresse</h5>
    <q-form>
      <div>
        <span>Straße und Hausnummer </span>
        <q-input v-model="inputs.streetAndNumber" />
      </div>
      <div>
        <span>Stadt</span>
        <q-input v-model="inputs.city" />
      </div>
      <div>
        <span>Postleitzahl</span>
        <q-input v-model="inputs.postcode" />
      </div>
    </q-form>
    <h5>Einwilligung zur Verarbeitung personenbezogener Daten:</h5>
    <q-form>
      <q-checkbox v-model="inputs.personalData">
        <span
          >Wir werden von dem fer! ggestellten Werk Lichtbildaufnahmen fer! gen.
          Der Kunde/die Kundin willigt hiermit ausdrücklich darin ein, dass
          diese Lichtbilder jenseits eines gemäß Art. 6 Absatz 1(f) EU-DSGVO
          zulässigen Zwecks zum Zwecke der Außendarstellung auf unserer Website,
          unseren Social Media Auftri" en (Facebook, Instagram, Twi" er usw.)
          oder auf Werbebannern verö# entlich werden.
        </span>
        <br />
        <span
          >Zudem werden mit dieser Einwilligungserklärung Gesundheitsdaten
          erhoben, damit wir entscheiden können, ob die Durchführung des
          Vertrags ohne Gefahr für Eure Gesundheit und ohne Beeinträch! gung des
          Ergebnisses unserer Arbeit möglich ist. Daher kann ohne diese
          Datenerhebung der Vertrag von uns nicht durchgeführt werden. Bei
          diesen Daten handelt es sich um besondere Daten im Sinne des Art. 9
          EU-DSGVO. In deren Erhebung wird hiermit durch Dich ausdrücklich
          eingewilligt. Diese Daten werden von uns nicht an Dri" e weitergegeben
          und sie werden für die Dauer von 10 Jahren bei uns aufbewahrt.
          Hiernach werden die Einwilligungserklärung und diese Zus!
          mmungserklärung vernichtet
        </span>
        <br />

        <span
          >Diese Einwilligung kann uns gegenüber jederzeit widerrufen werden
          (Art. 7 Abs. 3 EU-DSGVO). Hiernach dürfen wir die Verarbeitung der
          unter der Einwilligung erhobenen und/oder verwendeten Lichtbilder
          nicht mehr fortsetzen. Die erhobenen Gesundheitsdaten werden – da
          deren Verarbeitung bis zum Zeitpunkt des Widerrufs legi! m ist – bis
          zum Ablauf der Aufbewahrungsfrist verwahrt.
        </span>
      </q-checkbox>
    </q-form>
    <h5>Gesundheitliche Einwilligungen:</h5>

    <q-form>
      <HealtyForm />
    </q-form>
    <MySignaturePad></MySignaturePad>
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
});
</script>

<style scoped></style>
