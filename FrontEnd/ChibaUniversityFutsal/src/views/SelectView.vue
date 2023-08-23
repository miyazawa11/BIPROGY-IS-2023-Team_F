<script setup>
import BaseTitle from '@/components/BaseTitle.vue';
import BaseButton from '@/components/BaseButton.vue';

</script>

<template>
    <div class="row">
        <BaseTitle title="あなたはどちらですか？"></BaseTitle>
    </div>
    <div class="row">
      <div class="col">
        <div class="button">
          <div class="left-button">
            <BaseButton name="保護者" color="#ffddbd" size="20px" link='/guardians/attend'></BaseButton>
          </div>
          <div class="right-button">
            <BaseButton name="保育者" color="#cad6fd" size="20px" link='/nursery/confirm'></BaseButton>
          </div>
        </div>
      </div> 
    </div>
</template>

<style scoped>
.button{
  display: flex;
  justify-content: center;
}
.left-button{
  margin: 0 25px;
}
.right-button{
  margin: 0 25px;
}
</style>