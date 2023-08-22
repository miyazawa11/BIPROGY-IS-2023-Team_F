<script setup>
defineProps({
    title:String
})
</script>
    
<template>
    <h1>{{ title }}</h1>
</template>

<style scoped>
h1{
    font-weight: bold;
    color: rgb(80, 80, 80);
    text-align: center;
    margin: 30px 0 30px 0;
}
</style>