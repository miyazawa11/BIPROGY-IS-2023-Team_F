<script setup>
import { ref, onMounted, onUnmounted, inject } from 'vue';
import {useRoute} from 'vue-router'
import BaseTitle from '@/components/BaseTitle.vue';
import KidsDetail from '../components/KidsDetail.vue';
import BaseCalender from '@/components/BaseCalender.vue';
import BaseCalenderSumaho from '../components/BaseCalenderSumaho.vue';
import ServerAPI from '../services/ServerAPI';

const nowMonth = ref(new Date().getMonth() + 1);
const nowDate = ref(new Date().getDate());
const nowYear = ref(new Date().getFullYear());
const isMdAndUp = ref(window.matchMedia('(min-width: 768px)').matches);
const showWeeks = ref(-1);

// 選択された月と年
const selectedMonth = ref(8);
const selectedYear = ref(2023);
const selectedDay = ref(15)
// 日付ごとの色情報
const dateColors = ref([
  { day: 5, month: selectedMonth.value, color: 'blue' },
  { day: 15, month: selectedMonth.value, color: 'green' },
  // 他の日付の色情報も追加
]);

// カレンダーコンポーネントからの選択日付のハンドラ
const handleSelectedDate = (selectedDate) => {
  console.log('選択された日付:', selectedDate);
};

// カレンダーコンポーネントからの月変更のハンドラ
const handleMonthChange = (newMonth) => {
  selectedMonth.value = newMonth;
  console.log('月が変更されました:', selectedMonth.value);
};

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

const route =useRoute()
const childId=route.params.id  //urlにある園児idの取得
console.log("送信されるIDは！！！"+childId)

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
                <BaseCalender
                  :day="selectedDay"
                  :month="selectedMonth"
                  :year="selectedYear"
                  :weeksToShow="5"
                  :dateColors="dateColors"
                  @update:selectedDate="handleSelectedDate"
                  :onMonthChange="handleMonthChange"
                  />
            </div>
        </div>
        <div class="row">
            <div class="col">
                <div class="mx-auto" :class="isMdAndUp ? 'w-50' : 'w-100'">
                    <KidsDetail :childId="childId" :date="nowYear + `_` + nowMonth + `_` + nowDate" />
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
