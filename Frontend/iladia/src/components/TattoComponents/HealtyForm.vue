<template>
  <div>
    <q-form>
      <div v-for="(question, index) in questions" :key="index" class="q-mb-md">
        <q-card>
          <q-card-section>
            <div class="text-subtitle1">{{ question.text }}</div>
            <q-option-group
              v-model="form[question.model]"
              :options="options"
              option-type="radio"
              inline
              @change="emitData"
              class="q-mt-sm"
            />
            <q-input
              v-if="question.hasDetails"
              v-model="form[question.detailsModel]"
              :label="question.detailsLabel"
              filled
              dense
              class="q-mt-sm"
              @input="emitData"
            />
          </q-card-section>
        </q-card>
      </div>
      <div class="q-mb-md">
        <q-card>
          <q-card-section>
            <div class="text-h6 text-bold text-primary">
              Für weibliche Kunden:
            </div>
            <div class="q-mt-sm">
              <div class="text-subtitle1">Besteht eine Schwangerschaft?</div>
              <q-option-group
                v-model="form.schwangeren"
                :options="options"
                option-type="radio"
                inline
                @change="emitData"
                class="q-mt-sm"
              />
            </div>
            <div class="q-mt-sm">
              <div class="text-subtitle1">Wird gestillt?</div>
              <q-option-group
                v-model="form.gestillt"
                :options="options"
                option-type="radio"
                inline
                @change="emitData"
                class="q-mt-sm"
              />
            </div>
          </q-card-section>
        </q-card>
      </div>
    </q-form>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";

const emit = defineEmits(["update-health-data"]);

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
  medikamenteEingenommen: null,
  medikamenteEingenommenDetails: "",
  krankheiten: null,
  krankheitenDetails: "",
  alkohol: null,
  anasthesie: null,
  beeintrachtigung: null,
  eingriffe: null,
  keloid: null,
  uvStrahlung: null,
  schwangeren: null,
  gestillt: null,
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
  {
    text: "Wurden heute oder in den letzten 7 Tagen Medikamente eingenommen?",
    model: "medikamenteEingenommen",
    hasDetails: true,
    detailsModel: "medikamenteEingenommenDetails",
    detailsLabel: "Falls ja, welche?",
  },
  {
    text: "Bestehen sonstige chronische oder akute Krankheiten?",
    model: "krankheiten",
    hasDetails: true,
    detailsModel: "krankheitenDetails",
    detailsLabel: "Falls ja, welche?",
  },
  {
    text: "Wurden in den letzten 24 Stunden Alkohol und/oder andere Betäubungsmittel konsumiert?",
    model: "alkohol",
  },
  {
    text: "Wurden in den letzten 24 Stunden Oberflächenanästhetika appliziert?",
    model: "anasthesie",
  },
  {
    text: "Bestehen Beeinträchtigungen der Willensbildungs- oder Willensausübungsfähigkeit?",
    model: "beeintrachtigung",
  },
  {
    text: "Wurden in dem zu tätowierenden Bereich chirurgische Eingriffe oder Strahlenbehandlungen vorgenommen?",
    model: "eingriffe",
  },
  {
    text: "Besteht eine Neigung zu Keloidbildung oder eine Sarkoidose?",
    model: "keloid",
  },
  {
    text: "Wurde die Haut in den vergangenen 4 Monaten in einem mehr als alltäglich vorkommenden Maß UV-Strahlungen ausgesetzt?",
    model: "uvStrahlung",
  },
];

const emitData = () => {
  emit("update-health-data", form.value);
};

watch(form, emitData, { deep: true });
</script>

<style scoped>
.q-card {
  padding: 16px;
}
.text-bold {
  font-weight: bold;
}
.text-primary {
  color: red;
}
</style>
