<script setup>
import { ref, defineProps } from 'vue';

const props = defineProps({
  text: {
    type: String,
    required: true
  },
});

</script>


<template>
    <div class="d-flex justify-content-center align-items-center">
        <div class="spinner-border text-warning" role="status">
        </div>
        <span class="">{{ props.text }}</span>
    </div>
</template>