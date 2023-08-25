<script setup>
import { ref, onMounted, onUnmounted, inject } from 'vue';
import {useRoute} from 'vue-router'
import BaseTitle from '@/components/BaseTitle.vue';
import KidsDetail from '../components/KidsDetail.vue';
import BaseCalender from '@/components/BaseCalender.vue';
import BaseCalenderSumaho from '../components/BaseCalenderSumaho.vue';
import ServerAPI from '../services/ServerAPI';
import BaseLoadingSpinner from '../components/BaseLoadingSpinner.vue';

const nowMonth = ref(new Date().getMonth() + 1);
const nowDate = ref(new Date().getDate());
const nowYear = ref(new Date().getFullYear());
const isMdAndUp = ref(window.matchMedia('(min-width: 768px)').matches);
const showWeeks = ref(-1);

// 選択された月と年
const currentMonth = ref(nowMonth.value);
const currentYear = ref(nowYear.value);
const currentDate = ref(nowDate.value);


// カレンダーコンポーネントからの選択日付のハンドラ
const handleSelectedDate = (selectedDate) => {
  console.log('選択された日付:', selectedDate);
};

// カレンダーコンポーネントからの月変更のハンドラ
const handleMonthChange = (newMonth) => {
  currentMonth.value = newMonth;
  console.log('月が変更されました:', currentMonth.value);
}

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
    
    //その園児IDの月の出欠情報を取得
    getPresenceCalender();
});

const route =useRoute()
const childId=route.params.id  //urlにある園児idの取得
console.log("送信されるIDは！！！"+childId)

const api = new ServerAPI("http://127.0.0.1:5000");
const userDatas = ref([]);
const isLoading = ref(false);
const calenderCompKey = ref(0);
const dateColors = ref([]);
const getPresenceForMonth = async () => {   
    //currentMonthの全ての日付を取得
    const dates = [];
    for (let i = 1; i <= new Date(nowYear.value, currentMonth.value, 0).getDate(); i++) {
        dates.push(`${nowYear.value}_${currentMonth.value}_${i}`);
    }
    for(const date of dates) {
        const data = await api.getChildAttendance(childId, date);
        userDatas.value.push(
            data.length == 0 ? {
                date: undefined,
                id: undefined,
                reason: undefined,
                submitted_presence: undefined,
                was_present: undefined,
            } : 
            data[0]
        );
    }
}

const changeCalenderColor = () => {
    //出欠登録に合わせてカレンダーの色を変更する
    userDatas.value.forEach((data, i) =>{
        const isPresence = data.submitted_presence;
        const date = i+1;
        if (isPresence) {
            dateColors.value.push({
                day: date,
                month: currentMonth.value,
                color: 'green'
            });
        } else if(isPresence === false) {
            dateColors.value.push({
                day: date,
                month: currentMonth.value,
                color: 'red'
            });
        }
    });
    //カレンダーコンポーネントを再生成し、色情報を渡す
    calenderCompKey.value++;
}

const getPresenceCalender = () => {
    isLoading.value = true;
    getPresenceForMonth().then((data) => {
        console.log("api success");
    }).catch((error) => {
        console.log("api error", error);
        userDatas.value = [];
    }).finally(() => {
        console.log("api end");
        //色情報の定義
        changeCalenderColor();
        isLoading.value = false;
    });
}
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
                <BaseLoadingSpinner v-if="isLoading" text="月の出欠情報を取得中" style="transform:scale(1.5);"/>
                <BaseCalender
                    :key="calenderCompKey"
                    v-if="!isLoading"
                    :day="currentDate"
                    :month="currentMonth"            
                    :year="currentYear"
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
