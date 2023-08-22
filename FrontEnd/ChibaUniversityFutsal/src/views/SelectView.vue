<script setup>
import { ref } from 'vue';

import BaseTitle from '@/components/BaseTitle.vue';
import BaseButton from '@/components/BaseButton.vue';

</script>

<template>
    <div class="row">
        <BaseTitle title="あなたはどちらですか？"></BaseTitle>
      </div>
      <div class="row">
        <div class="col">
          <BaseButton name1="保護者" name2="保育者" color1="#ffddbd" color="#cad6fd" size="20px"></BaseButton>
        </div> 
      </div>
</template>

<style scoped>

</style>