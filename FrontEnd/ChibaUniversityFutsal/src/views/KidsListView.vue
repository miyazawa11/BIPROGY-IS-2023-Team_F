<script setup>
const kids=([
    {id:1,name:"みやざわ こうき",attend:true,confirm:false},
    {id:2,name:"みやざわ こうき",attend:true,confirm:true},
    {id:3,name:"みやざわ こうき",attend:true,confirm:false},
    {id:4,name:"みやざわ こうき",attend:true,confirm:false},
    {id:5,name:"みやざわ こうき",attend:true,confirm:false},
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
    <div>
        <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
            <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
            <label class="btn btn-outline-primary" for="btnradio1">Radio 1</label>

            <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio2">Radio 2</label>

            <input type="radio" class="btn-check" name="btnradio" id="btnradio3" autocomplete="off">
            <label class="btn btn-outline-primary" for="btnradio3">Radio 3</label>
        </div>
        <div class="w-100 p-3 color:">
            <nav class="w-75 p-3 mx-auto">
                <ul class="list-group height">
                    <li class="list-group-item row d-flex" v-for="kid in kids" :key="kid.id">
                        <div class="col-1  mx-auto">
                            <input class="form-check-input" type="checkbox" v-model="kid.confirm">
                        </div>
                        <label class="col-2  mx-auto form-check-label" :for="`checkbox-${kid.id}`">id:{{ kid.id }}</label>
                        <div class="col-5  mx-auto">
                            <button type="button" class="btn hover:btn-light">{{ kid.name }}</button>
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