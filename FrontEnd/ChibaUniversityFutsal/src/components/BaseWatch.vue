<template>
  <div>
    <div class="fw-bold fs-1">{{ year }}/{{ month }}/{{ day }}</div>
    <div class="fw-bold" style="font-size: 3rem;">{{ amPm }}{{ hour }}:{{ minute }}<span class="fs-3 pl-3 fw-semibold">{{ second }}</span> </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const year = ref('');
const month = ref('');
const day = ref('');
const hour = ref('');
const minute = ref('');
const second = ref('');
const amPm = ref('');

const updateDateTime = () => {
  const now = new Date();
  year.value = now.getFullYear();
  month.value = now.getMonth() + 1;
  day.value = now.getDate();
  hour.value = String(now.getHours() % 12 || 12).padStart(2, '0');
  minute.value = String(now.getMinutes()).padStart(2, '0');
  second.value = String(now.getSeconds()).padStart(2, '0');
  amPm.value = now.getHours() < 12 ? 'AM' : 'PM';
};

onMounted(() => {
  updateDateTime();
  setInterval(updateDateTime, 1000);
});
</script>

<style scoped>
/* Add your component-specific styles here */
</style>