<template>
  <div id="watch">
    {{ currentTime }}
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const currentTime = ref('');

const updateTime = () => {
  const now = new Date();
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');
  currentTime.value = `${hours}:${minutes}:${seconds}`;
};

let intervalId;

onMounted(() => {
  updateTime();
  intervalId = setInterval(updateTime, 1000);
});

onBeforeUnmount(() => {
  clearInterval(intervalId);
});
</script>

<style>
#watch{
    font-size: xx-large;
}
</style>
