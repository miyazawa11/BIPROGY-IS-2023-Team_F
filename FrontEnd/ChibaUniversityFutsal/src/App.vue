<script setup>
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router';

import BaseIconButton from "@/components/BaseIconButton.vue";

</script>

<template>
  <header class="TopHeader BaseColor fixed-top vh-9 vh-sm-10">
    <div class="row">
      <div class="col">
        <!--追加のボタン配置用-->
      </div>
      <div class="col LogoWrapper">
        <img src="@/assets/logo.png" alt="ロゴ" class="Logo">
      </div>
      <div class="col">
        <!--追加のボタン配置用-->
      </div>
    </div>
  </header>
  <div class="ContentWrapper d-flex align-items-center py-sm-21 pt-sm-25 px-sm-0 overflow-hidden">
    <!--以下にコンテンツを配置-->
    <div class="ContentParent">
      <router-link to="/"></router-link>
      <router-view></router-view>
    </div>
  </div>
  <footer class="Footer fixed-bottom shadow-lg border-top border-3">
    <div class="row d-sm-none" >
      <div class="col">
      </div>
      <div class="col">
        <div class="IconButtonWrapper position-relative mx-auto">
          <BaseIconButton name="出欠">
            <template v-slot:BaseIconButton>
              <i class="fa-solid fa-user fa-2xs"></i>
            </template>
          </BaseIconButton>
        </div>
      </div>
      <div class="col"></div>
    </div>
    <div class="row d-none d-md-block">
      <div class="col-3">
        <div class="IconButtonWrapper position-relative mx-auto">
          <BaseIconButton name="出欠" class="IconButtonSize">
            <template v-slot:BaseIconButton>
              <i class="fa-solid fa-user fa-2xs"></i>
            </template>
          </BaseIconButton>
        </div>
      </div>
      <div class="col-3"></div>
      <div class="col-3"></div>
    </div>
  </footer>

</template>

<style scoped>
.TopHeader {
  width: 100%;
}

.LogoWrapper {
  text-align: center;
  padding: 9px;
}
.Logo {
  width: 30%;
}

.ContentWrapper {
  background-color: #ffffff;
  width: 100%;
  height: 100vh;
  padding-top: 13%;
}

.ContentParent {
  width: 100%;
  height: auto;
  max-height: 100%;
}

.Footer{
  background-color: #ffffff;
  height: 7%;
  width: 100%;
}

.IconButtonWrapper {
  top: -33%;
  width: fit-content;
}

.IconButtonSize{
  transform: scale(2.5);
  position: relative;
  top: -3vw;
}

.min-vh-90 {
  min-height: 70vh !important;
}

.py-21 {
  padding-top: 21%;
  padding-bottom: 21%;
}

.pt-21 {
  padding-top: 21%;
}

/* スマホのみに適用 */
@media (max-width: 767.98px) {
  .vh-sm-10 {
      height: 10vh !important;
  }

  .px-sm-0 {
      padding-right: 0 !important;
      padding-left: 0 !important;
  }

  .py-sm-21 {
      padding-top: 21% !important;
      padding-bottom: 21% !important;
  }

  .pt-sm-25 {
    padding-top: 25% !important;
  }
  .Logo{
    width: 60%;
  }
}
</style>
