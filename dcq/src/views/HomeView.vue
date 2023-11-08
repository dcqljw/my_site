<template>
  <div class="home">

    <div class="container">
      <div class="container-left">
        <div class="title animate__animated animate__fadeInDownBig">DCQ</div>
        <div class="desc animate__animated animate__fadeInUpBig">欢迎来到DCQ个人网站</div>
      </div>
      <div class="container-right" v-bind:style="styleObj">
        <div class="code-info animate__animated animate__fadeInRightBig">
          <div class="code-nav">
            <div></div>
            <div></div>
            <div></div>
          </div>
          <div class="code-text">
            <span class="func_color">def</span>&nbsp;&nbsp;<span class="func_name_color">DCQ</span><span>( ):</span>
            <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="func_name_color">text</span><span> = </span><span
              class="func_text_color">"欢迎来到DCQ个人网站"</span>
            <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span>print(</span><span class="func_name_color">text</span><span>)</span>
            <br/>
            <br/>
            <span class="func_color">DCQ</span><span>( )</span>
          </div>
        </div>
      </div>

    </div>


    <div class="footer_scroller">
      <div class="footer">
        <div class="footer_text" v-for="i in 6" :key="i">
          <div class="start">DCQ</div>
          <div class="end">SITE</div>
        </div>
      </div>
      <div class="footer">
        <div class="footer_text" v-for="i in 6" :key="i">
          <div class="start">DCQ</div>
          <div class="end">SITE</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {},
  data() {
    return {
      styleObj: {
        width: "402px",
        height: "243px",
        padding: "10px",
      }
    }
  },
  created() {
    console.log(window.innerWidth)
    if (window.innerWidth < 800) {
      console.log("宽度小于800")
      this.styleObj.padding = "60px 10px 10px"
    }
  }
}
</script>

<style>
.home {
  height: 70%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
}

.container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.container-left {
  color: white;
}


.code-info {
  height: 100%;
  background-color: #22212C;
  border-radius: 10px;
}

.code-nav {
  display: flex;
  padding-top: 20px;
}

.code-nav div {
  height: 20px;
  width: 20px;
  margin-left: 20px;
  border-radius: 20px;
}

.code-nav div:nth-child(1) {
  background-color: #FF5F56;
}

.code-nav div:nth-child(2) {
  background-color: #FFBD2E;
}

.code-nav div:nth-child(3) {
  background-color: #27C93F;
}

.code-text {
  color: white;
  padding-left: 20px;
  padding-top: 20px;
  font-size: 20px;
  line-height: 31px;
  font-family: 微软雅黑;
}

.func_color {
  color: #ff80bf;
}

.func_name_color {
  color: #86f87d;
}

.func_text_color {
  color: #f9f97e;
}

.title {
  font-size: 60px;
  font-family: 微软雅黑;
  font-weight: bold;
  overflow: hidden;
  white-space: nowrap;
}

.desc {
  font-size: 20px;
  border-bottom: 5px solid #0ff;
  height: 35px;
  width: 300px;
}

.footer_scroller {
  display: flex;
  overflow: hidden;
  position: fixed;
  bottom: 20px;
}

.footer {
  display: flex;
  animation: scroll 7s linear infinite;
}

.footer_text {
  font-weight: bold;
}

@keyframes scroll {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-100%);
  }
}

.footer_text {
  display: flex;
  font-size: 40px;
}

.start {
  color: white;
  padding-right: 30px;
}

.end {
  color: #00FFE5;
  padding-right: 200px;
  -webkit-text-stroke: 1px #00FFE5;
  -webkit-text-fill-color: transparent;

}
</style>