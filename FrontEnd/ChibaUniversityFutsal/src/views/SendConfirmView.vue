<script setup>
import { ref, reactive } from 'vue';
import BaseTitle from '@/components/BaseTitle.vue';
import KidsDetail from '../components/KidsDetail.vue';
</script>


<template>
    <div class="row">
        <div class="col">
            <BaseTitle title="送信済み"></BaseTitle>
        </div>
        <div class="col">
            <!---カレンダーゾーン-->
        </div>
        <div class="col">
            <KidsDetail/>
        </div>
    </div>
</template>

<style scoped></style>
