<template>
  <div class="header-nav">
    <div class="logo">DCQ Site</div>
    <div class="nav-items">
      <div class="nav-item" v-for="item in navItems[currentLanguage]" :key="item">{{ item }}</div>
      <div class="check-language" @click="checkLanguage">
        <chinese-one v-show="currentLanguage === 'en' " theme="outline" size="25" fill="#0c0c0c"
                     :strokeWidth="3"></chinese-one>
        <english v-show="currentLanguage === 'cn'" theme="outline" size="25" fill="#0c0c0c" :strokeWidth="3"></english>
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
      currentLanguage: "en",
      navItems: {
        "cn": ["主页", "项目", '博客', '关于'],
        "en": ["Home", 'Project', 'Blog', 'About']
      }
    }
  },
  methods: {
    checkLanguage() {
      if (this.currentLanguage === "cn") {
        this.currentLanguage = "en"
      } else {
        this.currentLanguage = "cn"
      }
    }
  }

}
</script>

<style>
html, body {
  height: 100%;
}

body {
  margin: 0;
}

#app {
  height: 100%;
  background: #f0f0f0;
}

.header-nav {
  display: flex;
  justify-content: space-around;
  font-size: 18px;
  font-family: "Microsoft YaHei";
  padding-top: 20px;
  user-select: none;
}

.nav-item:after {
  display: block;
  content: "";
  width: 0;
  border-bottom: 2px solid black;
  margin: 8px auto;
  transition: width .5s;
}

.logo, .check-language, .nav-item {
  cursor: pointer;
}

.nav-item:hover:after {
  width: 100%;
}

.nav-items {
  display: flex;
  justify-content: space-between;
  width: 300px;
}
</style>