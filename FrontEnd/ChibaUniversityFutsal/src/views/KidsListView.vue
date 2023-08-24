<script setup>
import { RouterLink } from 'vue-router';
import { ref } from 'vue';

const colClass = ref('col-3');
const kids=([
    {id:1,name:"みやざわ こうき",attend:true,confirm:false},
    {id:2,name:"みやざわ こうき",attend:true,confirm:true},
    {id:3,name:"みやざわ こうき",attend:true,confirm:false},
    {id:4,name:"みやざわ こうき",attend:true,confirm:false},
    {id:5,name:"みやざわ こうき",attend:false,confirm:false},
    {id:6,name:"みやざわ こうき",attend:true,confirm:false},
    {id:7,name:"みやざわ こうき",attend:true,confirm:true},
    {id:8,name:"みやざわ こうき",attend:true,confirm:false},
    {id:9,name:"みやざわ こうき",attend:true,confirm:false},
    {id:10,name:"みやざわ こうき",attend:true,confirm:false},
    {id:11,name:"みやざわ こうき",attend:true,confirm:false},
    {id:12,name:"みやざわ こうき",attend:true,confirm:true},
    {id:13,name:"みやざわ こうき",attend:true,confirm:false},
    {id:14,name:"みやざわ こうき",attend:true,confirm:false},
    {id:15,name:"みやざわ こうき",attend:true,confirm:false},
    {id:16,name:"みやざわ こうき",attend:true,confirm:false},
    {id:17,name:"みやざわ こうき",attend:true,confirm:true},
    {id:18,name:"みやざわ こうき",attend:true,confirm:false},
    {id:19,name:"みやざわ こうき",attend:true,confirm:false},
    {id:20,name:"みやざわ こうき",attend:true,confirm:false},
])
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