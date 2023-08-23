<script setup>
import { ref, onMounted } from 'vue';

const modalElement = ref(false);
const open =()=>{
  const modalInstance = new bootstrap.Modal(modalElement.value);
  modalInstance.show();
}
onMounted(() => {
    open()
});

defineProps({
    title:String,
})

const absence =ref('')
const send =()=>{
    
}
</script>

<template>
    <div class="modal" tabindex="-1" ref="modalElement">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{ title }}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <textarea v-model="absence" name="" id="textarea" cols="30" rows="10" placeholder="例：風邪のため " required></textarea>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">中断</button>
                    <button type="button" class="btn btn-primary" @click="send">送信</button>
                </div>
            </div>
        </div>
    </div>
</template>
 
<style scoped>
#textarea{
    width: 100%;

}
</style>