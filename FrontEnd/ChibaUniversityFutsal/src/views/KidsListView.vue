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

const colClass = ref('col-3');

</script>

<template>
    <div class="mb-10">
        <div class="btn-group" role="group" aria-label="Basic radio toggle button group" style="width:300px;">
            <input type="radio" class="btn-check mx-auto" name="btnradio" id="btnradio1" autocomplete="off" checked>
            <label class="btn btn-outline-primary mx-auto" for="btnradio1">ID順</label>

            <input type="radio" class="btn-check mx-auto" name="btnradio" id="btnradio2" autocomplete="off">
            <label class="btn btn-outline-primary mx-auto" for="btnradio2">チェック済み</label>

            <input type="radio" class="btn-check mx-auto" name="btnradio" id="btnradio3" autocomplete="off">
            <label class="btn btn-outline-primary mx-auto" for="btnradio3">チェック無し</label>
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
                    </li>
                </ul>
            </nav>
        </div>
        <div class="">
            <nav class="p-6 mx-auto">
                <ul class="list-group overflow-auto vh-65">
                    <li class="list-group-item row d-flex d-flex align-items-center" v-for="kid in kids" :key="kid.id">
                        <label :class="['fs-4', colClass, 'mx-auto', 'form-check-label', 'text-center', 'd-flex', 'align-items-center']" :for="`checkbox-${kid.id}`">{{ kid.id }}</label>
                        <div :class="['mx-auto text-center', colClass, 'name-hover']">
                            <router-link :to="{name:'KidDetailViewPage',params:{id:kid.id}}" class="name-hover" style="color: inherit;">
                                <button type="button" class="fs-4">{{ kid.name }}</button>
                            </router-link>
                        </div>
                        <span :class="['mx-auto fw-bolder fs-4 d-flex align-items-center', colClass]" style="vertical-align: middle;" v-if="kid.attend">出席</span>
                        <span :class="['mx-auto fw-bolder fs-4 d-flex align-items-center', colClass]" style="vertical-align: middle;" v-else>欠席</span>
                        <input :class="['form-check-input text-center d-flex align-items-center', colClass]" type="checkbox" v-model="kid.confirm">
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</template>

<style scoped>
.list-group {
    overflow: auto;
    max-height: 65vh;
}
.name-hover:hover {
    background-color: #f0f0f0; /* 任意の色 */
  }
.form-check-input {
  border-color: #0000ff !important;
  width: 40px !important;  /* 幅 */
  height: 40px !important; /* 高さ */
  /* 以下の行は、大きさが変更された後の配置を調整します */
  vertical-align: middle !important;
  margin: 0 auto !important;
}
</style>