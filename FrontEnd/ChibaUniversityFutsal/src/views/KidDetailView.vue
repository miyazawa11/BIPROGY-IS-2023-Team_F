<script setup>
import { ref, onMounted } from 'vue';
import {useRoute} from 'vue-router'
import KidsDetail from '../components/KidsDetail.vue';
import BaseCalender from '@/components/BaseCalender.vue';
import BaseLoadingSpinner from '../components/BaseLoadingSpinner.vue';
import ServerAPI from '../services/ServerAPI';



const route = useRoute()
const childId=route.params.id  //urlにある園児idの取得

const nowMonth = ref(new Date().getMonth() + 1);
const nowDate = ref(new Date().getDate());
const nowYear = ref(new Date().getFullYear());
const currentYear = ref(nowYear.value);
const currentMonth = ref(nowMonth.value);
const currentDate = ref(nowDate.value);

const isLoading = ref(false);

const componentKey = ref(0);
const calenderCompKey = ref(0);

const userDatas = ref([]);
const dateColors = ref([]);

const selectedDateHandler = (selectedDate) => {
    console.log(selectedDate);
    currentMonth.value = selectedDate.month;
    currentDate.value = selectedDate.day;
    //KidsDetailのコンポーネントを再生成
    componentKey.value++;
    console.log(componentKey.value);
}

const incrementDate = () => {
    if (currentMonth.value == 12 && currentDate.value == 31) {
        currentMonth.value = 1;
        currentDate.value = 1;
    } else if (currentDate.value > new Date(nowYear.value, currentMonth.value, 0).getDate() -1 ) {
        currentMonth.value++;
        currentDate.value = 1;
        //Todo:カレンダーの月を変更する

    } else {
        currentDate.value++;
    }
}

const decrementDate = () => {
    if (currentMonth.value == 1 && currentDate.value == 1) {
        currentMonth.value = 12;
        currentDate.value = 31;
    } else if (currentDate.value == 1) {
        currentMonth.value--;
        currentDate.value = 31;
        //Todo:カレンダーの月を変更する
    } else {
        currentDate.value--;
    }
}

/*API 連結部*/
const api = new ServerAPI("http://127.0.0.1:5000");

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

onMounted(() => {
    getPresenceCalender();    
});
</script>

<template>
    <div class="container">
        <div class="row justify-content-around">
            <div class="col-md-4 mb-10">
                <div class="d-flex justify-content-center align-items-center">
                    <i class="fa-solid fa-chevron-left" @click="decrementDate"></i>
                    <p class="mx-5 mt-3 fw-bold" style="transform:scale(1.5)">{{ currentMonth }} / {{ currentDate }}</p>
                    <i class="fa-solid fa-chevron-right" @click="incrementDate"></i>
                </div>
                <KidsDetail v-if="!(isLoading)" :key="componentKey" :useCommnent="true" :childId="childId" :date="`${currentYear}_${currentMonth}_${currentDate}`"/>
            </div>
            <div class="col-md-4 mb-10">
                <BaseLoadingSpinner v-if="isLoading" text="月の出欠情報を取得中..." style="transform:scale(1.5);"/>
                <BaseCalender v-if="!(isLoading)" :key="calenderCompKey" :month="nowMonth" @update:selectedDate="selectedDateHandler" :dateColors="dateColors" :year="nowYear"/>
            </div>
        </div>
    </div>
</template>

<style scoped>
.w-fit {
    width: fit-content;
}
</style>