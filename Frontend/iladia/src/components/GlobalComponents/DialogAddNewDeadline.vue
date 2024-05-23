<template>
  <q-dialog v-model="dialog" persistent>
    <q-card>
      <q-card-section>
        <div class="text-h6">Your Dialog Title</div>
      </q-card-section>
      <q-toggle
        :label="pinkModel"
        color="pink"
        false-value="Disagreed"
        true-value="Agreed"
        v-model="pinkModel"
      />
      <q-form>
        <q-card-section class="q-pt-none">
          <q-input v-model="inputs.title" type="text" />
          <q-input v-model="inputs.description" type="textarea" />
          <q-input v-model="inputs.with" />
          <q-input filled v-model="inputs.time.start">
            <template v-slot:prepend>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy
                  cover
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-date v-model="inputs.time.start" mask="YYYY-MM-DD HH:mm">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>

            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy
                  cover
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-time
                    v-model="inputs.time.start"
                    mask="YYYY-MM-DD HH:mm"
                    format24h
                  >
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
          <q-input filled v-model="inputs.time.end">
            <template v-slot:prepend>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy
                  cover
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-date v-model="inputs.time.end" mask="YYYY-MM-DD HH:mm">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>

            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy
                  cover
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-time
                    v-model="inputs.time.end"
                    mask="YYYY-MM-DD HH:mm"
                    format24h
                  >
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn
            @click="
              () => {
                submit();
                reset();
              }
            "
            flat
            label="Dodaj"
            color="primary"
          />
          <q-btn
            @click="
              () => {
                submit();
                reset();
              }
            "
            flat
            label="Cancel"
            color="primary"
          />
        </q-card-actions>
      </q-form>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { ref, watch } from "vue";

const dialog = ref(false);
const pinkModel = ref("Agreed");

const inputs = ref({
  title: "",
  time: {
    start: "",
    end: "",
  },
  with: "",
  typ: "",
  description: "",
});

const props = defineProps({
  addToCalendar: Function,
  addNewDialog: Boolean,
  close: Function,
});

watch(
  () => props.addNewDialog,
  (newVal) => {
    dialog.value = newVal;
  }
);

function closeDialog() {
  dialog.value = false;
  props.close();
}

function submit() {
  const newEvent = {
    title: inputs.value.title,
    with: inputs.value.with,
    time: { start: inputs.value.time.start, end: inputs.value.time.end },
    color: "green",
    id: Math.random(),
    description: inputs.value.description,
    isEditable: true,
  };
  props.addToCalendar(newEvent);
  closeDialog();
}

const reset = () => {
  inputs.value = {
    title: "",
    time: {
      start: "",
      end: "",
    },
    with: "",
    typ: "",
    description: "",
  };
};

const options = [
  {
    label: "Dawid Kaczmarek",
    value: "1",
  },
  {
    label: "Marcin Kaczmarek",
    value: "2",
  },
];
</script>

<style scoped></style>
