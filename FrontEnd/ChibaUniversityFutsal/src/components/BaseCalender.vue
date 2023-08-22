<script setup>
import { ref, computed } from 'vue';

// propsの定義
const props = defineProps({
  month: {
    type: Number,
    required: true
  },
  year: {
    type: Number,
    default: new Date().getFullYear()
  },
  weeksToShow: {
    type: Number,
    default: 5
  }
});

// 指定された月の日数を取得
const getDaysInMonth = (month, year) => {
  return new Date(year, month, 0).getDate();
};

// 指定された月のカレンダーデータを生成
const generateCalendarDates = (month, year) => {
  const daysInMonth = getDaysInMonth(month, year);
  const weeks = [];
  let week = [];
  for (let i = 1; i <= daysInMonth; i++) {
    week.push(i);
    if (i % 7 === 0 || i === daysInMonth) {
      weeks.push(week);
      week = [];
    }
  }
  return weeks.slice(0, props.weeksToShow);
};

const weeks = computed(() => generateCalendarDates(props.month, props.year));
</script>

<template>
  <!-- カレンダーコンポーネント -->
  <div class="calendar">
    <!-- カレンダーのヘッダー部分 -->
    <div class="calendar-header">
      <h3>{{ month }}月</h3>
    </div>
    <!-- カレンダーの日付部分 -->
    <div class="calendar-body">
      <table class="table">
        <thead>
          <tr>
            <th>日</th>
            <th>月</th>
            <th>火</th>
            <th>水</th>
            <th>木</th>
            <th>金</th>
            <th>土</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="week in weeks" :key="week[0]">
            <td v-for="day in week" :key="day" :class="{ 'bg-light': !day }">
              {{ day || '' }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
/* Bootstrap 5のスタイルを利用 */
</style>
