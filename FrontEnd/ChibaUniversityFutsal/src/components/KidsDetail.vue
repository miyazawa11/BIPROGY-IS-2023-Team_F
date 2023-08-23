<script setup>
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute();
console.log(route.params.id);
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
onMounted(()=>{
    // データベースから園児情報の取得関数
})

</script>

<template>
    <div class="card" style="width: 30rem;height: 15rem;">
        <div>
            <h5 class="card-header" style="display: flex; justify-content: space-between;">
                <span>名前：{{ kid_.name }}</span>
                <p v-if="kid.confirm" class="card-text">確認</p>
            </h5>
        </div>
        <div class="card-body">
            <div v-if="!kid_.attend">
                <h5 class="card-title">欠席</h5>
                <p class="card-text">{{ kid_.reason }}</p>
            </div>
            <div v-else>
                <h5 class="card-title">出席</h5>
            </div>
        </div>
    </div>
</template>