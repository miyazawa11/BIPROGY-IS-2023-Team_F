<script setup>
import BaseButton from '../components/BaseButton.vue';
import {useRouter} from 'vue-router';

const router = useRouter()
const transition = () => {
    router.push('/');
}
</script>

<template>
    <div>
    <h1>正しい値を入力してください</h1>
        <BaseButton name="戻る" color="#f8b556" size="30px" @click="transition"></BaseButton>
    </div>
</template>

<style scope>
div{
    text-align: center;
}
a{
    color: inherit;
}
</style>