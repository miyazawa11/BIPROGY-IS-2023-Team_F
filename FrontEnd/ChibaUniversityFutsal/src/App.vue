<script setup>
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router';





</script>

<template>
  <header class="TopHeader fixed-top">
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
  <div class="d-flex align-items-center justify-content-center min-vh-100">
    <!--以下にコンテンツを配置-->
    <div class="">
      <router-link to="/"></router-link>
      <router-view></router-view>
    </div>
  </div>
  <footer class="Footer fixed-bottom shadow-lg">
    <div class="row" >
      <div class="col">
      </div>
      <div class="col TopButtonWrapper">
        <!--トップボタン用-->
      </div>
    </div>
    <div class="col"></div>
  </footer>

</template>

<style scoped>
.TopHeader {
  background-color: #f7C223;
  width: 100%;
}

.LogoWrapper {
  text-align: center;
  padding: 9px;
}
.Logo {
  width: 30%;
}

.ContentArea {
  overflow: auto;
  margin-top: 35%;
  height: 100%;
}

.ContentArea > .row {
  margin-bottom: 10%;
}

.Footer{
  background-color: #f7C223;
  height: 7%;
  width: 100%;
}
</style>
