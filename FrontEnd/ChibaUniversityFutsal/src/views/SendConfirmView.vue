<script setup>
import { ref, reactive } from 'vue';

import BaseTitle from '@/components/BaseTitle.vue';
</script>


<template>
    <div class="row">
        <div class="col">
            <BaseTitle title="出席しました！！"></BaseTitle>
        </div>
        <div class="col">
            <!---カレンダーゾーン-->
        </div>
        <div class="col">
            <!--選択した日にちの出欠席ログの確認・編集ゾーン-->
        </div>
    </div>
</template>

<style scoped></style>
