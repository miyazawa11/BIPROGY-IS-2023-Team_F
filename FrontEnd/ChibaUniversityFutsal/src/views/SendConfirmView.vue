<script setup>
import { ref} from 'vue';
import BaseTitle from '@/components/BaseTitle.vue';
import KidsDetail from '../components/KidsDetail.vue';
import BaseCalender from '../components/BaseCalender.vue';
import BaseCalenderSumaho from '../components/BaseCalenderSumaho.vue';

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
</script>


<template>
    <div class="row">
        <div class="col">
            <BaseTitle title="送信済み"></BaseTitle>
        </div>
        <div class="col">
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
        <div class="col">
            <KidsDetail/>
        </div>
    </div>
</template>

<style scoped></style>
