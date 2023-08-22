<script setup>
import { ref } from 'vue';
import BaseTitle from '@/components/BaseTitle.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseWatch from '@/components/BaseWatch.vue';
import BaseModal from "../components/BaseModal.vue"

const modalOpen=ref(false)
const handleEvent = (left, right) => {
  console.log('親コンポーネントで受け取ったパラメータ:', left, right);
  if(left==true){
    modalOpen.value=true
    console.log(modalOpen.value)
  }
};
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
        <BaseButton @eventTest2="handleEvent" name1="出席" name2="欠席" color1="#ffddbd" color="#cad6fd" size="30px"></BaseButton>
      </div> 
    </div>
    <div v-if="modalOpen">
      <BaseModal title="欠席理由"/>
    </div>
    
</template>

<style scoped>
</style>