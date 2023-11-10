<script>
export default {
  data() {
    return {
      isPhone: false,
      showCount: 1
    }
  },
  created() {
    if (window.innerWidth < 600) {
      this.isPhone = true
      this.showCount = 1
      console.log("phone")
    }
  }
}
</script>

<template>
  <div class="cover-view">
    <div class="aaaa" v-bind:class="{phone:isPhone}">
      <div>
        <div style="display: flex;position: fixed">
          <div class="text_group" v-for="i in 2" :key="i">
            <div class="text_group_item" v-for="i in 2" :key="i">
              <div class="text_item">
                <div style="color: #C800FF">天天</div>
                <div style="color: #3AFF00">开心&nbsp;&nbsp;</div>
              </div>
              <div class="text_item">
        <span style="color: #04DBFF">
          HAPPY&nbsp;&nbsp;
        </span>
              </div>
            </div>
            <div class="text_group_item" v-for="i in 2" :key="i">
              <div class="text_item">
                <div style="color: #C800FF">天天</div>
                <div style="color: #3AFF00">开心&nbsp;&nbsp;</div>
              </div>
              <div class="text_item">
        <span style="color: #04DBFF">
          HAPPY&nbsp;&nbsp;
        </span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <div style="display: flex;position:fixed;">
          <div class="text_group" v-for="i in 2" :key="i">
            <div class="text_group_item" v-for="i in 2" :key="i">
              <div class="text_item">
                <span style="color: #FBFF00">RICH&nbsp;&nbsp;</span>
              </div>
              <div class="text_item">
                <span style="color:#3AFF00;">暴</span>
                <span style="color: #FBFF00">富&nbsp;&nbsp;</span>
              </div>
            </div>
            <div class="text_group_item" v-for="i in 2" :key="i">
              <div class="text_item">
                <span style="color: #FBFF00">RICH&nbsp;&nbsp;</span>
              </div>
              <div class="text_item">
                <span style="color:#3AFF00;">暴</span>
                <span style="color: #FBFF00">富&nbsp;&nbsp;</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <div style="display: flex;position: fixed">
          <div class="text_group" v-for="i in 2" :key="i">
            <div class="text_group_item" v-for="i in 2" :key="i">
              <div class="text_item">
                <span style="color:#3AFF00;">吃</span>
                <span style="color: #FF0000">嘛嘛</span>
                <span style="color: #3AFF00">香&nbsp;&nbsp;</span>
              </div>
              <div class="text_item">
                <span style="color: #FF7E02">FOOD&nbsp;&nbsp;</span>
              </div>
            </div>
            <div class="text_group_item" v-for="i in 2" :key="i">
              <div class="text_item">
                <span style="color:#3AFF00;">吃</span>
                <span style="color: #FF0000">嘛嘛</span>
                <span style="color: #3AFF00">香&nbsp;&nbsp;</span>
              </div>
              <div class="text_item">
                <span style="color: #FF7E02">FOOD&nbsp;&nbsp;</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
@font-face {
  font-family: "myfont";
  src: url("../../public/text.ttf");
}

.cover-view {
  height: 100%;
  width: 100%;
  color: white;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: #000000;
  position: fixed;
  z-index: 1000;
}

.text_group {
  display: flex;
  animation: scroll 5s linear infinite;
  width: 100%;
}

.text_group_item {
  display: flex;

}

.text_group > div {
  display: flex;
}

.text_item {
  display: flex;
  white-space: nowrap;
  font-size: 100px;
  font-family: "myfont";
}

@keyframes scroll {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-150%);
  }
}

@keyframes fscroll {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(0);
  }
}

.aaaa {
  display: flex;
  height: 80%;
  width: 100%;
  flex-direction: column;
  align-content: space-between;
  justify-content: space-evenly;
}

.phone {
  transform: rotate(70deg);
}

@media screen and(min-width: 400px) {
  .cover-view > div:nth-child(1) {
    background-color: red;
  }
}
</style>