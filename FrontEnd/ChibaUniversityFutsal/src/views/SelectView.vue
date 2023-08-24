<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { inject } from 'vue';
import { provide } from 'vue';
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

const childIdInput = ref('');
let savedChildId = inject('childId');

provide(1,childIdInput.value);
const saveChildId = () => { //次のルーティングページに遷移するボタン押下時に実行
  
  console.log("input", childIdInput.value);
  savedChildId.value = childIdInput.value;
  console.log("saved", savedChildId);
  const savedChildId = inject(1);
  console.log(savedChildId);
}


</script>

<template>
    <div class="row">
        <BaseTitle class="mb-5" title="あなたはどちらですか？"></BaseTitle>
    </div>
    <div class="row">
      <div class="col">
        <div class="button">
          <div class="left-button">
            <BaseButton name="保護者" color="#ffddbd" :size="isMdAndUp ? '40px' : '30px'" :link="`/guardians/${childIdInput}`" @click="saveChildId"></BaseButton>
          </div>
          <div class="right-button">
            <BaseButton name="保育者" color="#cad6fd" :size="isMdAndUp ? '40px' : '30px'" link="/nursery/confirm"></BaseButton>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="d-block w-fit mx-auto mt-4">
          <input class="border-3 rounded border-warning" type="text" v-model="childIdInput" placeholder="園児IDを入力してください" name="childId">
        </div>
      </div>
    </div>
</template>

<style scoped>

.w-fit{
  width: fit-content;
}
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