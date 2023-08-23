<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import BaseTitle from '@/components/BaseTitle.vue';
import KidsDetail from '../components/KidsDetail.vue';
import BaseCalender from '../components/BaseCalender.vue';

const nowMonth = ref(new Date().getMonth() + 1);
const isMdAndUp = ref(window.matchMedia('(min-width: 768px)').matches);
const showWeeks = ref(-1)

onMounted(() => {
    const mediaQueryList = window.matchMedia('(min-width: 768px)');

    /**画面幅変更時のハンドラ*/
    const handler = (e) => {
        isMdAndUp.value = e.matches;
        console.log(isMdAndUp.value);
        showWeeks.value = isMdAndUp.value ? -1 : 2;
    };
    mediaQueryList.addEventListener('change', handler);
    // 初期値を設定
    isMdAndUp.value = mediaQueryList.matches;
    showWeeks.value = isMdAndUp.value ? -1 : 2;
    onUnmounted(() => {
        mediaQueryList.removeEventListener('change', handler);
    });
});


</script>

<template>
    <div>
        <div class="row mb-4">
            <div class="col-12 col-md d-flex align-items-center">
                <div class="w-fit h-fit my-auto mx-auto">
                    <div class="w-fit mx-auto">
                        <i class="fa-regular fa-circle-check fa-8x" style="color: #ffad1f;"></i>
                    </div>
                    <BaseTitle title="送信済み" class="mt-3"></BaseTitle>
                </div>
            </div>
            <div class="col-12 col-md">
                <BaseCalender :month="nowMonth" :weeks-to-show="showWeeks"/>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <div class="mx-auto" :class="isMdAndUp ? 'w-50' : 'w-100'">
                    <KidsDetail/>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.w-fit {
    width: fit-content;
}
.h-fit {
    height: fit-content;
}
</style>
