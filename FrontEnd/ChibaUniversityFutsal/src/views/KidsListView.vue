<script setup>
import { ref, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import ServerAPI from '../services/ServerAPI';
import BaseLoadingSpinner from '../components/BaseLoadingSpinner.vue';

const kids = ref([]);
const api = new ServerAPI("http://127.0.0.1:5000");

const nowYear = new Date().getFullYear();
const nowMonth = new Date().getMonth() + 1;
const nowDate = new Date().getDate();

const currentMonth = ref(nowMonth);
const currentDate = ref(nowDate);
const currentYer = ref(nowYear);

const isLoadingAPI = ref(false);

/*API連結部*/
const getKidsInfo = async () => {
    isLoadingAPI.value = true;
    const response = await api.teacherGetListByDate(currentYer.value, currentMonth.value, currentDate.value);
    //以下で取得したデータをkidsに反映
    console.log("園児一覧API", response);
    for(const data of response) {
        kids.value.push({
            id: data.id_children,
            name: `${data.first_name} ${data.last_name}`,
            attend: data.attend,
            confirm: false,
        });
    }
}

onMounted(() => {
    getKidsInfo().then((data) => {
        console.log("api success");
    }).catch((error) => {
        console.log("api error");
        kids.value = [];
    }).finally(() => {
        console.log("api end");
        isLoadingAPI.value = false;
    });
});


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
    //APIの再取得
    kids.value = [];
    getKidsInfo().then((data) => {
        console.log("api success");
    }).catch((error) => {
        console.log("api error");
    }).finally(() => {
        console.log("api end");
        isLoadingAPI.value = false;
    });
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
    //APIの再取得
    kids.value = [];
    getKidsInfo().then((data) => {
        console.log("api success");
    }).catch((error) => {
        console.log("api error");
    }).finally(() => {
        console.log("api end");
        isLoadingAPI.value = false;
    });
}

</script>

<template>
    <div>
        <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
            <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
            <label class="btn btn-outline-primary" for="btnradio1">Radio 1</label>

            <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio2">Radio 2</label>

            <input type="radio" class="btn-check" name="btnradio" id="btnradio3" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio3">Radio 3</label>
        </div>
        <div class="row mt-5">
            <div class="d-flex justify-content-center align-items-center" style="transform:scale(1.5)">
                <i class="fa-solid fa-chevron-left" @click="decrementDate"></i>
                <p class="mx-3 mt-3 fw-bold">{{ currentMonth }} / {{ currentDate }}</p>
                <i class="fa-solid fa-chevron-right" @click="incrementDate"></i>
            </div>
        </div>
        <div class="w-100 p-3 color:">
            <nav class="w-75 p-3 mx-auto">
                <ul class="list-group height">
                    <p v-if="kids.length == 0 && !isLoadingAPI" class="text-center fs-1 fw-bold">登録済みの園児がいません。</p>
                    <BaseLoadingSpinner v-else-if="isLoadingAPI" text="登録されている園児一覧を読み込み中..."/>
                    <li v-else class="list-group-item row d-flex" v-for="kid in kids" :key="kid.id">
                        <div class="col-1  mx-auto">
                            <input class="form-check-input" type="checkbox" v-model="kid.confirm">
                        </div>
                        <label class="col-2  mx-auto form-check-label" :for="`checkbox-${kid.id}`">id:{{ kid.id }}</label>
                        <div class="col-5  mx-auto">
                            <routerLink :to="{name:'KidDetailViewPage',params:{id:kid.id}}">
                                <button type="button" class="btn hover:btn-light">{{ kid.name }}</button>
                            </routerLink>
                        </div>
                        <div class="col-2  mx-auto" v-if="kid.attend">〇</div>
                        <div class="col-2  mx-auto" v-else>×</div>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</template>

<style scoped>
.height {
    height: 100vh; 
    width:100%;
    overflow-x: hidden; 
    overflow-y: auto;
}
</style>