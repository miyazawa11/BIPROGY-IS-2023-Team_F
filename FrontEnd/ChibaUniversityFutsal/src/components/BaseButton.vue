<script setup>
import { useRouter } from 'vue-router'
import { defineProps, defineEmits } from 'vue';


defineProps({
    name: String,
    color: String,
    size: String,
    link: String,
})

const router = useRouter()
const transition = (link) => {
    console.log(link)
    if(link.length!=0){
        console.log(link)
        router.push(link)
    }
}
</script>

<template>
    <div>
        <button @click="transition(link)" class="Button" type="button">
            {{ name }}
        </button>
    </div>
</template>

<style scoped>
button{
    background-color: v-bind(color);
    border-radius: 20px;
    font-weight: bold;
    font-size: v-bind(size);
    transition: 300ms;
}
button:hover{
    opacity: 0.7;
}
</style>