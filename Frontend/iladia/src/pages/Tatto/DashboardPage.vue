<template>
  <q-page class="page-bg">
    <q-btn
      @click="addNewDialog = true"
      label="Nowy termin"
      class="bg-white"
    ></q-btn>
    <Qalendar
      :events="events"
      :config="config"
      @delete-event="handleDeleteClick"
    >
    </Qalendar>
  </q-page>

  <dialog-add-new-deadline
    :add-new-dialog="addNewDialog"
    :add-to-calendar="addToCalendar"
    :close="closeHandler"
  />
</template>

<script setup>
import { Qalendar } from "qalendar";
import { ref } from "vue";
import DialogAddNewDeadline from "components/GlobalComponents/DialogAddNewDeadline.vue";

const addNewDialog = ref(false);
const events = ref([
  {
    title: "Advanced algebra",
    with: "Chandler Bing",
    time: { start: "2024-05-17 12:05", end: "2024-05-17 13:35" },
    color: "yellow",
    isEditable: true,
    id: "753944708f0f",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores assumenda corporis doloremque et expedita molestias necessitatibus quam quas temporibus veritatis. Deserunt excepturi illum nobis perferendis praesentium repudiandae saepe sapiente voluptatem!",
  },
  {
    title: "Ralph on holiday",
    with: "Rachel Greene",
    time: { start: "2024-05-17 12:05", end: "2024-05-17 13:35" },
    color: "green",
    isEditable: true,
    id: "5602b6f589fc",
  },
]);

const config = {
  dayBoundaries: {
    start: 7,
    end: 20,
  },
  defaultMode: "month",
};

const handleDeleteClick = (event) => {
  console.log("Event to delete:", event);
  const newEvents = events.value.filter((e) => {
    return e.id !== event;
  });
  events.value = newEvents;
};

const addToCalendar = (newEvent) => {
  events.value = [...events.value, newEvent];
};

const closeHandler = () => {
  addNewDialog.value = false;
};
</script>

<style>
@import "qalendar/dist/style.css";
</style>
