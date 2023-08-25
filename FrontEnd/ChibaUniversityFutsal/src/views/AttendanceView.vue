<script setup>
import { ref,onMounted, onUnmounted, inject } from 'vue';
import { useRouter,useRoute } from 'vue-router';
import BaseButton from '@/components/BaseButton.vue';
import BaseWatch from '@/components/BaseWatch.vue';
import BaseLoadingSpinner from '../components/BaseLoadingSpinner.vue';
import ServerAPI from '../services/ServerAPI';

const isAttend = ref(false);
const isLoading = ref(false);
const ModalOpen = ref(null)
const abstract = ref('')
const router = useRouter()
const route = useRoute();
const childId= route.params.id  //urlにある園児idの取得
console.log("ATTENDANCEVIEW ID初期値", childId)
const transition = (link) => {
    //とりあえずここでAPIを呼び出す
    sendAbsence().then(() =>{
      console.log('api POST success');
    }).catch((error) =>{
      console.log(error);
    }).finally(() =>{
      console.log('api POST end');
      console.log("LINK",link)
      if(link.length!=0) {
        console.log("ROUTING")
        isLoading.value = false;
        router.push(link)
      }
    });
}
// メディアクエリを使用して、画面の幅が中サイズ以上かどうかを判定,リサイズを監視し、レイアウトを変更できるようにする
const isMdAndUp = ref(window.matchMedia('(min-width: 768px)').matches);
onMounted(() => {
    const mediaQueryList = window.matchMedia('(min-width: 768px)');
    const handler = (e) => {
        isMdAndUp.value = e.matches;
    };
    mediaQueryList.addEventListener('change', handler);
    // 初期値を設定
    isMdAndUp.value = mediaQueryList.matches;
    onUnmounted(() => {
        mediaQueryList.removeEventListener('change', handler);
    });
});

const hozon=()=>{
    console.log("送信されるIDは"+childId);
}
console.log(isMdAndUp.value);

/*出欠登録APIの呼び出し*/

const api = new ServerAPI("http://127.0.0.1:5000");

const sendAttendanceAPI = () => {
    isLoading.value = true;
    isAttend.value = true;

    console.log('apiTest');
    

    const post = async () => {

      const nowYear = new Date().getFullYear();
      const nowMonth = new Date().getMonth() + 1;
      const nowDate = new Date().getDate();

      const param = {
        id: childId,
        date: `${nowYear}_${nowMonth}_${nowDate}`,
        is_attendance: isAttend.value,
        abstract: abstract.value
      }
      console.log("API REQUEST ATTENDANCE", param);

      const response = await api.registerChildAttendance(
        param.id,
        param.date,
        param.is_attendance,
        param.abstract
      );
    }

    post()
    .catch((error) => {
      console.log("API RESPONSE ATTENDANCE Child", response);
      console.log(error);
    })
    .finally(() => {
      console.log('api POST end');
      isLoading.value = false;
      router.push(`/guardians/confirm/${childId}`)
    });
}

const sendAbsence = async () => {
    isLoading.value = true;
    isAttend.value = false;
    const nowYear = new Date().getFullYear();
    const nowMonth = new Date().getMonth() + 1;
    const nowDate = new Date().getDate();

    const param = {
        id: childId,
        date: `${nowYear}_${nowMonth}_${nowDate}`,
        is_attendance: isAttend.value,
        abstract: abstract.value
    }

    console.log(param);
    const response = await api.registerChildAttendance(
        param.id,
        param.date,
        param.is_attendance,
        param.abstract
    );
    console.log(response);
}

</script>

<template>
  <div style="height: 40vh">
    <div class="row justify-content-center mb-3">
      <div class="col-12 col-md d-flex justify-content-center align-items-center">
        <div class="w-fit mx-auto">
          <BaseWatch :style="isMdAndUp ? {'transform': 'scale(1.5)'} : {}"></BaseWatch>
        </div>
      </div>
      <div class="col-12 col-md">
        <div class="row justify-content-center my-md-8">
          <!-- スマホレイアウトではcol-6を使用してボタンを横並びにし、PCレイアウトではcol-12を使用してボタンを縦並びにします -->
          <div class="col-6 col-md-12 w-fit mx-auto">
              <BaseButton name="出席" color="#ffddbd" :size="isMdAndUp ? '60px' : '40px'" link="" @click="sendAttendanceAPI"></BaseButton>
          </div>
          <div class="col-6 col-md-12 w-fit mx-auto">
              <BaseButton name="欠席" color="#cad6fd" :size="isMdAndUp ? '60px' : '40px'" link="" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="hozon"></BaseButton>
          </div>
        </div>
      </div>
    </div>
    <!-- modal表示 -->
    <div class="modal fade" ref="ModalOpen" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">欠席理由</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <textarea class="abstract" v-model="abstract" cols="30" rows="10" placeholder="例：発熱のため"></textarea>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">中断</button>
            <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="transition(`/guardians/confirm/${childId}`)">送信</button>
          </div>
        </div>
      </div>
    </div>
    
  </div>
</template>

<style scoped>
.w-fit {
  width: fit-content;
}
.abstract {
  width: 100%;
}
</style>
