<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import BaseTitle from '@/components/BaseTitle.vue';
import BaseButton from '@/components/BaseButton.vue';

// メディアクエリを使用して、画面の幅が中サイズ以上かどうかを判定,リサイズを監視し、レイアウトを変更できるようにする
const isMdAndUp = ref(window.matchMedia('(min-width: 768px)').matches);

onMounted(() => {
    const mediaQueryList = window.matchMedia('(min-width: 768px)');
    const handler = (e) => {
        isMdAndUp.value = e.matches;
    };
    mediaQueryList.addEventListener('change', handler);
    // 初期値を設定
    isMdAndUp.value = mediaQueryList.matches;

    onUnmounted(() => {
        mediaQueryList.removeEventListener('change', handler);
    });
});

console.log(isMdAndUp.value);

</script>

<template>
    <div class="row">
        <BaseTitle title="あなたはどちらですか？"></BaseTitle>
    </div>
    <div class="row">
      <div class="col">
        <div class="button">
          <div class="left-button">
            <BaseButton name="保護者" color="#ffddbd" :size="isMdAndUp ? '40px' : '30px'" link='/guardians/attend'></BaseButton>
          </div>
          <div class="right-button">
            <BaseButton name="保育者" color="#cad6fd" :size="isMdAndUp ? '40px' : '30px'" link='/nursery/confirm'></BaseButton>
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