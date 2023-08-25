<script setup>
/**
 * カレンダーコンポーネント
 * @component
 * @prop {number} month - 表示する月 (必須)
 * @prop {number} [year=new Date().getFullYear()] - 表示する年 (オプション)
 * @prop {number} [weeksToShow=-1] - 表示する週の数 (オプション)
 * @prop {Array} [dateColors=[]] - 特定の日付に適用する色情報の配列 (オプション)
 * @emits update:selectedDate - 選択された日付を返すイベント（コールバック関数）
 */
import { ref, computed } from 'vue';

/** @type {Props} */
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
    default: -1
  },
  dateColors: {
    type: Array,
    default: () => []
  },
  onMonthChange: {
    type: Function,
    default: null
  }
});

// emitの定義
const emit = defineEmits(['update:selectedDate']);


// 選択された日付
const selectedDate = ref('');

// 日付を選択する関数
const selectDate = (day) => {
  //selectedDate.value = `${props.year}-${props.month}-${day}`;
  selectedDate.value = {
    year: props.year,
    month: props.month,
    day: day
  }
  emit('update:selectedDate', selectedDate.value); //呼び出し側に値を返す
};

const currentMonth = ref(props.month);
const currentYear = ref(props.year);


// 指定された日付の色を取得する関数
const getColor = (day) => {
  const dateColor = props.dateColors.find(item => item.day == day && item.month == currentMonth.value.toString());
  return dateColor ? dateColor.color : 'transparent';
};

// 指定された月の日数を取得
const getDaysInMonth = (month, year) => {
    return new Date(year, month, 0).getDate();
};

// 指定された月のカレンダーデータを生成
const generateCalendarDates = (month, year) => {
    const daysInMonth = getDaysInMonth(month, year);
    const firstDayOfWeek = new Date(year, month - 1, 1).getDay(); // 月の最初の日の曜日を取得
    const weeks = [];
    let week = Array(firstDayOfWeek).fill(null); // 月の最初の日までの空の日付を追加

    for (let i = 1; i <= daysInMonth; i++) {
        week.push(i);
        if (week.length === 7 || i === daysInMonth) {
        weeks.push(week);
        week = [];
        }
    }

    // weeksToShowが-1の場合、全ての週を表示
    return props.weeksToShow === -1 ? weeks : weeks.slice(0, props.weeksToShow);
};

// 現在の月と年を更新する関数
const changeMonth = (direction) => {
  if (direction === 'prev') {
    if (currentMonth.value === 1) {
      currentMonth.value = 12;
      currentYear.value -= 1;
    } else {
      currentMonth.value -= 1;
    }
  } else if (direction === 'next') {
    if (currentMonth.value === 12) {
      currentMonth.value = 1;
      currentYear.value += 1;
    } else {
      currentMonth.value += 1;
    }
  }
  // 新しい月の色の状態をpropsから取得
  try {
    props.dateColors = monthColors.value;
  } catch (error) {
    console.log("指定された月,日の色が指定されていないのでスキップします")
  }

  // コールバック関数が提供されている場合、それを実行
  if (props.onMonthChange) {
    props.onMonthChange(currentMonth.value);
  }
};

const weeks = computed(() => generateCalendarDates(currentMonth.value, currentYear.value));


</script>

<template>
  <!-- カレンダーコンポーネント -->
  <div class="calendar">
    <!-- カレンダーのヘッダー部分 -->
    <div class="calendar-header d-flex">
      <!-- 前の月へ移動するアイコン -->
      <i class="fas fa-chevron-left pt-3" @click="changeMonth('prev')"></i>
      <h3 class="mx-4">{{ currentMonth }}月</h3>
      <!-- 次の月へ移動するアイコン -->
      <i class="fas fa-chevron-right pt-3" @click="changeMonth('next')"></i>
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
            <td v-for="day in week" :key="day" :class="{ 'bg-light': !day }" @click="selectDate(day)">
              <button type="button" class="date-circle btn" data-bs-toggle="tooltip" data-bs-placement="top" title="その日の詳細画面へ" :style="{ backgroundColor: getColor(day) }" style="color:rgb(0,0,0);">
                {{ day || '' }}
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.date-circle {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
