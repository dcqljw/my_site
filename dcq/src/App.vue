<template>
  <div class="header">
    <div class="logo">
      <div class="logo_div">
        <span>D</span>
      </div>
    </div>
    <div class="header-left">
      <div class="animate__animated"
           v-on:mouseover="setClass"
           v-on:mouseleave="setClass"
           v-for="item in language === 'cn'?navListCN:navListUS" :key="item">
        <span>{{ item }}</span>
      </div>
      <div class="contact">
        <span>{{ language === "cn" ? contactCN : contactUS}}</span>
      </div>
      <div>
        <chinese-one theme="outline" size="35" fill="#ffffff" v-if="language === 'en'" @click="setLanguage"/>
        <english theme="outline" size="35" fill="#ffffff" v-if="language === 'cn'" @click="setLanguage"/>
      </div>
    </div>
  </div>
  <router-view/>
</template>

<script>
import {ChineseOne, English} from "@icon-park/vue-next";

export default {
  components: {ChineseOne, English},
  data() {
    return {
      animate: "",
      navListUS: ["Project", "Blog", "About"],
      navListCN: ["项目", "博客", "关于"],
      contactUS: "CONTACT",
      contactCN: "联系我",
      language: "cn",
    }
  },
  methods: {
    setClass() {
    },
    setLanguage() {
      console.log(this.language)
      if (this.language === "cn") {
        this.language = "en"
      } else {
        this.language = "cn"
      }
      console.log(this.language)
    }
  }
}
</script>

<style>

::-webkit-scrollbar {
  display: none;
}

body {
  margin: 0;
}

html {
  background-color: black;
  user-select: none;
  height: 100%;
  font-family: 微软雅黑;
}

body {
  height: 100%;
  margin: 0;
}

#app {
  height: 100%;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 15px;
}

.header-left {
  color: white;
  display: flex;
  align-items: center;
  font-size: 20px;
}

.header-left div {
  cursor: pointer;
  margin-left: 30px;
}

.contact {
  color: white;
  font-size: 20px;
  border: 2px solid #00FFE5;
  width: 140px;
  text-align: center;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 6px;
  cursor: pointer;
}

.logo_div {
  color: white;
  border: 5px solid #00FFE5;
  font-size: 30px;
  width: 50px;
  height: 50px;
  text-align: center;
  border-radius: 18px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
</style>
<script setup>
</script>