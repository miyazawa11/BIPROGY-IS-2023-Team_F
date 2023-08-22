<script setup>
import { ref} from 'vue';
import { useRouter } from 'vue-router';
import BaseButton from '@/components/BaseButton.vue';
import BaseWatch from '@/components/BaseWatch.vue';

const ModalOpen = ref(null)
const abstract = ref('')
const router = useRouter()
const transition = (link) => {
    if(link.length!=0){
        router.push(link)
    }
}
</script>


<template>
  <div>
    <div class="row justify-content-center mb-3">
        <div class="col">
            <div class="w-25 mx-auto">
                <BaseWatch></BaseWatch>
            </div>
        </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="button">
          <div class="left-button" >
          <BaseButton name="出席" color="#ffddbd" size="30px" link="confirm"></BaseButton>
          </div>
          <div class="right-button">
            <BaseButton name="欠席" color="#cad6fd" size="30px" link="" data-bs-toggle="modal" data-bs-target="#exampleModal"></BaseButton>
          </div>
        </div>
      </div> 
    </div>
    <!-- modal表示 -->
    <div class="modal fade" ref="ModalOpen" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered" >
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">欠席理由</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
            <div class="modal-body">
              <textarea class="abstract" v-model="abstract" cols="30" rows="10" placeholder="例：発熱のため"></textarea>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">中断</button>
              <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="transition('confirm')">送信</button>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<style scoped>
.button{
  display: flex;
}
.left-button{
  margin: 0 25px;
}
.right-button{
  margin: 0 25px;
}
.abstract{
  width: 100%;
}
</style>