<script setup>
import { ref } from 'vue';
import KidsDetail from '../components/KidsDetail.vue';
import BaseCalender from '../components/BaseCalender.vue';

const nowMonth = ref(new Date().getMonth() + 1);
const nowDate = ref(new Date().getDate());
const nowYear = ref(new Date().getFullYear());
const currentMonth = ref(nowMonth.value);
const currentDate = ref(nowDate.value);
const selectedDateHandler = (selectedDate) => {
    //console.log(selectedDate);
    currentMonth.value = selectedDate.month;
    currentDate.value = selectedDate.day;
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
</script>

<template>
    <div class="container">
        <div class="row justify-content-around">
            <div class="col-md-4 mb-10">
                <div class="d-flex justify-content-center align-items-center">
                    <i class="fa-solid fa-chevron-left" @click="decrementDate"></i>
                    <p class="mx-3 mt-3 fw-bold">{{ currentMonth }} / {{ currentDate }}</p>
                    <i class="fa-solid fa-chevron-right" @click="incrementDate"></i>
                </div>
                <KidsDetail />
            </div>
            <div class="col-md-4 mb-10">
                <BaseCalender :month="nowMonth" @update:selectedDate="selectedDateHandler" />
            </div>
        </div>
    </div>
</template>

<style scoped>
.w-fit {
    width: fit-content;
}
</style>