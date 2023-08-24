<script setup>
import { reactive, ref } from 'vue';
import { onMounted, defineProps } from 'vue';
import { useRoute } from 'vue-router';
import ServerAPI from '../services/ServerAPI';
const route = useRoute();
console.log(route.params.id);

const props = defineProps({
  childId: {
    type: String,
    required: true
  },
  date: {
    type: String,
    required: true
  },
  useCommnent: {
    type: Boolean,
    required: false,
    default: false
  }
});

const kid = reactive({
  name: '',
  attend: false,
  reason: '',
  confirm: false
});

/*以下はダミーデータ*/
//Todo:APIからデータを取得する
/*
const kid={
        name:'みやざわこうき',
        attend:true,
        reason:'',
        confirm:true
    }
const kid_={
        name:'みやざわこうき',
        attend:false,
        reason:'風邪のためお休みさせてください',
        confirm:false
    }
*/
onMounted(()=>{
    // データベースから園児情報の取得関数
    const res = getChildPresenceInfo().then((data) =>{
        console.log(data);
        if(data.length == 0){
            console.log("データがありません");
            kid.name=props.childId;
            kid.attend=null;
            kid.reason="データなし";
            kid.confirm=null;
            return;
        }
        const result = data[0]
        //TODO:ここで、取得した出欠結果と理由を取得し、変数に反映
        kid.name=props.childId;
        kid.attend=result.submitted_presence;
        kid.reason=result.reason;
        kid.confirm=result.submitted_presence;
    });
})
/**API結合部*/
const api = new ServerAPI("http://127.0.0.1:5000");
const getChildPresenceInfo = async () => {
    const id=props.childId;

    const param = {
        id: id,
        date: props.date
    }
    const response = await api.getChildAttendance(param.id, param.date);
    
    return response;
}

const saveComment = () => {
    //TODO:返信用APIを呼び出す
}

</script>

<template>
    <div class="card" style="width: auto;height: auto;">
        <div>
            <h5 class="card-header" style="display: flex; justify-content: space-between;">
                <span>名前：{{ kid.name }}</span>
                <p v-if="kid.confirm" class="card-text">確認</p>
            </h5>
        </div>
        <div class="card-body">
            <div v-if="kid.attend === false">
                <h5 class="card-title">欠席</h5>
                <p class="card-text">{{ kid.reason }}</p>
            </div>
            <div v-else-if="kid.attend">
                <h5 class="card-title">出席</h5>
            </div>
            <div v-else>
                <h5 class="card-title">出欠席の登録がありません。</h5>
            </div>
        </div>
        <div class="mt-3" v-if="props.useCommnent">
            <label for="comment" class="form-label">保育士のコメント</label>
            <textarea class="form-control" id="comment" rows="3"></textarea>
            <button type="button" class="btn btn-warning mt-2" @click="saveComment">コメントを保存</button>
        </div>
    </div>
</template>