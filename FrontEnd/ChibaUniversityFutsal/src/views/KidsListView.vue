<script setup>
const Kids=[
    {id:1,name:"みやざわ　こうき",attend:true},
    {id:2,name:"kid1",attend:true},
    {id:3,name:"kid1",attend:true},
    {id:4,name:"kid1",attend:true},
    {id:6,name:"kid1",attend:true},
    {id:7,name:"kid1",attend:true},
    {id:8,name:"kid1",attend:true},
    {id:9,name:"kid1",attend:true},
    {id:10,name:"kid1",attend:true},
    {id:11,name:"kid1",attend:true},
    {id:12,name:"kid1",attend:true},
    {id:13,name:"kid1",attend:true},
    {id:14,name:"kid1",attend:true},
    {id:15,name:"kid1",attend:false},
]
</script>

<template>
    <nav>
        <ul class="list-group" v-for="kid in Kids" :key="kid.id">
            <li class="list-group-item row d-flex">
                <input class="form-check-input me-1 col" type="checkbox" value="" id="firstCheckbox">
                <div class="form-check-label col" for="firstCheckbox">id:{{ kid.id }}</div>
                <div class="col">{{ kid.name }}</div>
                <div class="col" v-if="kid.attend">〇</div>
                <div class="col" v-else>×</div>
            </li>
        </ul>
    </nav>
</template>

<style>
li{
    list-style: none;
}
</style>