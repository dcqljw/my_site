<template>
  <CoverView v-show="show_cover" class="animate__animated" v-bind:class="show_cover_animate" @click="bless"></CoverView>
  <div class="nav_page animate__animated " v-bind:class="show_animate" v-show="showNavItem">
    <div class="close_nava_item animate__animated" v-bind:class="close_animate" v-show="showNavItem">
      <close theme="outline" size="35" fill="black" @click="showNav"/>
    </div>
    <div class="nav_items">
      <div v-for="item in navList" :key="item">
        <div class="nav_item animate__animated" @click="toView(item[2])">
          <div class="link_cn">{{ item[0] }}</div>
          <div class="link_en">{{ item[1] }}</div>
          <div class="split_line"></div>
        </div>
      </div>
      <div class="tips">
      </div>
    </div>
  </div>
  <div class="header">
    <div class="logo" @click="this.$router.push('/')">
      <div class="logo_div">
        <span>D</span>
      </div>
    </div>
    <div class="header-left">
      <div class="header-nav-item animate__animated hidden-xs-only"
           v-on:mouseover="setClass"
           v-on:mouseleave="setClass"
           v-for="item in language === 'cn'?navListCN:navListUS" :key="item">
        <span @click="this.$router.push(item[1])">{{ item[0] }}</span>
      </div>
      <div>
        <span @click="bless">祝福</span>
      </div>
      <div>
        <chinese-one theme="outline" size="35" fill="#ffffff" v-if="language === 'en'" @click="setLanguage"/>
        <english theme="outline" size="35" fill="#ffffff" v-if="language === 'cn'" @click="setLanguage"/>
      </div>
      <div>
        <hamburger-button theme="outline" size="40" fill="#ffffff" @click="showNav"/>
      </div>
    </div>
  </div>
  <router-view/>
</template>

<script>
import {ChineseOne, English, HamburgerButton, Close} from "@icon-park/vue-next";
import CoverView from "@/views/CoverView.vue";

export default {
  components: {CoverView, ChineseOne, English, HamburgerButton, Close},
  data() {
    return {
      animate: "",
      navListUS: [["Home", "/"], ["Project", 'project'], ["Blog", 'blog'], ["About", 'about']],
      navListCN: [["主页", "/"], ["项目", 'project'], ["博客", 'blog'], ["关于", 'about']],
      contactUS: "CONTACT",
      contactCN: "联系",
      language: "cn",
      showNavItem: false,
      close_animate: "",
      show_animate: "",
      navList: [["主页", "home", '/'], ["项目", "project", 'project'], ["博客", "blog", 'blog'], ["关于", "about", 'about']],
      show_cover_animate: "",
      show_cover: false
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
    },
    bless() {
      if (!this.show_cover) {
        this.show_cover = true
      }
      if (this.show_cover_animate === "animate__fadeInDownBig") {
        this.show_cover_animate = "animate__fadeOutUpBig"
      } else {
        this.show_cover_animate = "animate__fadeInDownBig"
      }

    },
    showNav() {
      console.log(this.showNavItem)
      if (this.showNavItem) {
        this.close_animate = ""
        if (this.show_animate === "animate__fadeOutDownBig" || this.close_animate === "animate__rotateOutUpRight") {
          this.show_animate = "animate__fadeInUpBig"
          this.close_animate = "animate__fadeInRightBig"
        } else {
          this.show_animate = "animate__fadeOutDownBig"
          this.close_animate = "animate__rotateOutUpRight"
        }
      } else {
        this.showNavItem = true
        this.close_animate = "animate__fadeInRightBig"
        this.show_animate = "animate__fadeInUpBig"
      }
    },
    toView(path) {
      console.log(path)
      this.$router.push(path)
      this.show_animate = "animate__fadeOutDownBig"
      this.close_animate = "animate__rotateOutUpRight"
    }
  }, created() {
  }
}
</script>

<style>
.header-nav-item {
  position: relative;
}

.header-nav-item:hover {
  color: #0ff;
}

.header-nav-item:hover:after {
  width: 100%;
}

.header-nav-item:after {
  color: #0ff;
  position: absolute;
  content: "";
  border-bottom: 3px solid;
  width: 0;
  display: block;
  margin: 10px 0;
  transition: width 0.1s ease-in-out;
}

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

.close_nava_item {
  z-index: 1000;
  position: fixed;
  right: 21px;
  top: 20px;
  cursor: pointer;
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
  overflow: hidden;
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
  width: 110px;
  text-align: center;
  height: 40px;
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

.nav_page {
  background-color: #f7f7f7;
  height: 100%;
  width: 100%;
  position: fixed;
  z-index: 1000;
}

.nav_items {
  margin-top: 60px;
  text-align: center;
}

.link_cn {
  font-size: 40px;
}

.link_en {
  font-size: 20px;
}

.nav_items > div {
  margin-bottom: 40px;
  display: flex;
  justify-content: center;
}

.split_line {
  border-bottom: 4px solid;
  height: 10px;
  width: 88px;
}

.tips {
  position: fixed;
  bottom: 0;
  width: 100%;
}

.nav_item:hover {
  color: #00FFE5;
  animation-name: swing;
}
</style>