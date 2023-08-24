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
  day:{
    type:Number,
    required:true
  },
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
const currentDay = ref(props.day)

// 指定された日付の色を取得する関数
const getColor = (day) => {
  const dateColor = props.dateColors.find(item => item.day == day && item.month == currentMonth.value.toString());
  return dateColor ? dateColor.color : 'transparent';
};


const getDaysInMonth = (month, year) => {
    return new Date(year, month, 0).getDate();
};
let CurrentDay = new Date(currentYear.value,currentMonth.value, currentDay.value);
const generateCalendarDates = (month,year,day) => {
    const weeks = [];
    const startDate = new Date(year, month-1, day);
    startDate.setDate(startDate.getDate() - 7);
    const endDate = new Date(year, month-1, day);
    endDate.setDate(endDate.getDate() + 7);
    const firstDayOfWeek = startDate.getDay();
    // let week = Array(firstDayOfWeek).fill(null);
    let week = [];
    
    CurrentDay.setDate(startDate.getDate() - firstDayOfWeek);
    for(let i=firstDayOfWeek - 1; i >= 0; i--){
      week.push(new Date(CurrentDay).getDate());
      CurrentDay.setDate(CurrentDay.getDate() + 1);
    }
    for (CurrentDay = new Date(startDate); CurrentDay <= endDate; CurrentDay.setDate(CurrentDay.getDate() + 1)) {
      week.push(new Date(CurrentDay).getDate());
      if (week.length === 7) {
          weeks.push(week);
          week = [];
      }
    }
    CurrentDay.setDate(endDate.getDate() + 1);
    for(let i=endDate.getDay(); i < 6; i++){
      week.push(new Date(CurrentDay).getDate());
      CurrentDay.setDate(CurrentDay.getDate() + 1);
    }
    if (week.length > 0) {
      weeks.push(week);
    }
    return weeks;
};


let weeks =  generateCalendarDates(currentMonth.value, currentYear.value,currentDay.value);
weeks=ref(weeks)
// 現在の月と年を更新する関数
const changeMonth = (direction) => {
  weeks.value=[]
  let week=[]
  if (direction === 'prev') {
    CurrentDay.setDate(CurrentDay.getDate() -42);
    for (let i=0;i<21;i++) {
        week.push(new Date(CurrentDay).getDate());
        CurrentDay.setDate(CurrentDay.getDate() + 1);
        if (week.length === 7) {
            weeks.value.push(week);
            week = [];
        }
      }
  } else if (direction === 'next') {
      for (let i=0;i<21;i++) {
        week.push(new Date(CurrentDay).getDate());
        CurrentDay.setDate(CurrentDay.getDate() + 1);
        if (week.length === 7) {
            weeks.value.push(week);
            week = [];
        }
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
    currentMonth.value=CurrentDay.getMonth() + 1;
    //右下の日付が基準になっている
};

</script>

<template>
  <!-- カレンダーコンポーネント -->
  <div class="calendar">
    <!-- カレンダーのヘッダー部分 -->
    <div class="calendar-header d-flex">
      <!-- 前の月へ移動するアイコン -->
      <i class="fas fa-chevron-left pt-3" @click="changeMonth('prev')"></i>
      <h3 class="mx-4">{{ currentYear }}年</h3>
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
              <div class="date-circle" :style="{ backgroundColor: getColor(day) }" style="color:rgb(0,0,0);">
                {{ day || '' }}
              </div>
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
