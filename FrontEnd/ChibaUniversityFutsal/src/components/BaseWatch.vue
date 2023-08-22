<template>
    <div id="watch">
        <div id="watch-large">
            {{ currentTime }}:
        </div>
        <div id="watch-seconds">
            {{ currentTimeSeconds }}
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const currentTime = ref('');
const currentTimeSeconds = ref('');

const updateTime = () => {
  const now = new Date();
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');
  currentTime.value = `${hours}:${minutes}`;
  currentTimeSeconds.value=seconds
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
    /*コレ*/display: flex;
    /*コレ*/align-items: flex-end;
}
#watch-large{
    font-size: xx-large;
}
#watch-seconds{
    font-size: x-large;
    align-items: end;
    padding-bottom: 3px;
}
</style>
