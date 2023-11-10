<script>
import {Code, Game, VideoTwo, Snowflake} from "@icon-park/vue-next";

export default {
  components: {Code, Game, VideoTwo, Snowflake}
}
</script>

<template>
  <div class="index-view">
    <div class="logo_image">
      <el-avatar style="background: none" :size="70" :src="require('../images/logo.png')"/>
    </div>
    <div class="title">
      <span>DCQ Site</span>
    </div>
    <div class="other">
      <Code theme="outline" size="32" fill="#0c0c0c" :strokeWidth="3"/>
      <Game theme="outline" size="32" fill="#0c0c0c" :strokeWidth="3"/>
      <VideoTwo theme="outline" size="32" fill="#0c0c0c" :strokeWidth="3"/>
      <Snowflake theme="outline" size="32" fill="#0c0c0c" :strokeWidth="3"/>
    </div>
    <div class="footer">
      <span>&copy;2023-2023 DCQ · SITE</span>
    </div>
  </div>
</template>

<style>
.index-view {
  height: 80%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  user-select: none;
}

.index-view > div {
  margin-top: 10px;
}

.logo_image {
}

.title {
  font-size: 40px;
}

.other span {
  cursor: pointer;
}

.other {
  display: flex;
  justify-content: space-between;
  width: 200px;
}

.footer {
  position: fixed;
  bottom: 20px;
  font-size: 15px;
}
</style>