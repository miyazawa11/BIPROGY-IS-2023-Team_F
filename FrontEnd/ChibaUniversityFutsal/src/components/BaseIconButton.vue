<script setup>
defineProps({
    name: String,
})
</script>

<template>
    <div>
        <button class="Button" type="button">
            <div>
                <slot name="BaseIconButton" />
            </div>
            <div id="name">
                {{ name }}
            </div>
        </button>
    </div>
</template>

<style scoped>

i{
    font-size: large;
}
button{
    background: orange;
    color: #fff;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    font-weight: bold;
    font-size: v-bind(size);
    margin: 0 50px;
    transition: 300ms;
}
#name{
    font-size:medium ;
}
button:hover{
    opacity: 0.7;
}
</style>