<template>
  <q-page class="q-pa-md">
    <q-form @submit.prevent="submitForm">
      <div v-for="(question, index) in questions" :key="index" class="q-mb-md">
        <q-card>
          <q-card-section>
            <div class="text-h6">{{ question.text }}</div>
            <q-option-group
              v-model="form[question.model]"
              :options="options"
              option-type="radio"
              inline
              class="q-mt-sm"
            />
            <q-input
              v-if="question.hasDetails"
              v-model="form[question.detailsModel]"
              :label="question.detailsLabel"
              filled
              dense
              class="q-mt-sm"
            />
          </q-card-section>
        </q-card>
      </div>
      <q-btn type="submit" label="Submit" color="primary" />
    </q-form>
  </q-page>
</template>

<script setup>
import { ref } from "vue";

const form = ref({
  bluterkrankung: null,
  hauterkrankungen: null,
  hauterkrankungenDetails: "",
  medikamente: null,
  allergien: null,
  allergienDetails: "",
  herzbeschwerden: null,
  infektionskrankheiten: null,
  infektionskrankheitenDetails: "",
});

const options = [
  { label: "Ja", value: "ja" },
  { label: "Nein", value: "nein" },
];

const questions = [
  {
    text: "Besteht eine Bluterkrankung, oder erhöhte Blutungsneigung?",
    model: "bluterkrankung",
  },
  {
    text: "Bestehen Hauterkrankungen (Neurodermitis etc.)?",
    model: "hauterkrankungen",
    hasDetails: true,
    detailsModel: "hauterkrankungenDetails",
    detailsLabel: "Falls ja, welche?",
  },
  {
    text: "Werden blutverdünnende Medikamente (Marcumar, Aspirin, Heparin etc.) eingenommen?",
    model: "medikamente",
  },
  {
    text: "Bestehen Allergien?",
    model: "allergien",
    hasDetails: true,
    detailsModel: "allergienDetails",
    detailsLabel: "Falls ja, gegen welche Allergene?",
  },
  {
    text: "Bestehen Herz- oder Kreislaufbeschwerden?",
    model: "herzbeschwerden",
  },
  {
    text: "Bestehen Infektionskrankheiten (Hep, MRSA etc)?",
    model: "infektionskrankheiten",
    hasDetails: true,
    detailsModel: "infektionskrankheitenDetails",
    detailsLabel: "Falls ja, welche?",
  },
];

const submitForm = () => {
  console.log("Form Data:", form.value);
};
</script>

<style scoped>
.q-card {
  padding: 16px;
}
</style>
