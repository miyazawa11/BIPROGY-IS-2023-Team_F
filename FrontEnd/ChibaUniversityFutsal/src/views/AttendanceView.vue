<script setup>
import { ref } from 'vue';
import BaseTitle from '@/components/BaseTitle.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseWatch from '@/components/BaseWatch.vue';


</script>


<template>
    <div class="row justify-content-center mb-3">
        <div class="col ">
            <div class="w-25 mx-auto">
                <BaseWatch></BaseWatch>
            </div>
        </div>
    </div>
    <div class="row">
      <div class="col">
        <BaseButton name1="出席" name2="欠席" color1="#ffddbd" color="#cad6fd" size="30px"></BaseButton>
      </div> 
    </div>
</template>

<style scoped>
</style>