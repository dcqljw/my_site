<script>
export default {
  data() {
    return {
      navList: [["项目", "project"], ["博客", "blog"], ["关于", "about"], ["联系", "contact"]]
    }
  }
}
</script>

<template>
  <div class="nav_page">
    <div class="nav_items">
      <div v-for="item in navList" :key="item">
        <div class="nav_item animate__animated" @click="this.$router.push('/contact')">
          <div class="link_cn">{{ item[0] }}</div>
          <div class="link_en">{{ item[1] }}</div>
          <div class="split_line"></div>
        </div>
      </div>
      <div class="tips">
      </div>
    </div>
  </div>
</template>

<style scoped>
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