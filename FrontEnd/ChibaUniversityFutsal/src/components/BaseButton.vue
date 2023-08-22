<script setup>
defineProps({
    name1: String,
    name2: String,
    color1:String,
    color2:String,
    size:String
})
</script>

<template>
    <div>
        <button class="ButtonLeft" type="button">
            {{ name1 }}
        </button>
        <button class="ButtonRight" type="button">
            {{ name2 }}
        </button>
    </div>
</template>

<style scoped>
div{
    text-align: center;
}
.ButtonLeft{
    background-color: v-bind(color1);
}
.ButtonRight{
    background-color: v-bind(color2);
}
button{
    border-radius: 20px;
    font-weight: bold;
    font-size: v-bind(size);
    margin: 0 50px;
    transition: 300ms;
}
button:hover{
    opacity: 0.7;
}
</style>