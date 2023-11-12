<script>
import Cherry from "cherry-markdown";
import "cherry-markdown/dist/cherry-markdown.min.css"

export default {
  name: "AdminView",
  data() {
    return {
      username: "",
      password: "",
      isLogin: true,
      blogTitle: ""
    }
  },
  methods: {
    login() {
      if (this.username === "dcq" && this.password === "dcq") {
        this.isLogin = true
        this.mkEdit()
      } else {
        this.$message.error("账号密码错误")
      }
    },
    mkEdit() {
      this.cherryInstance = new Cherry({
        id: "blog-edit",
      })
    }
  },
  mounted() {
    if (this.isLogin) {
      this.mkEdit()
    }
  }
}
</script>

<template>
  <div class="admin-view">
    <div style="width: 1000px">
      <div class="login" v-show="!isLogin">
        <div>登录</div>
        <el-input v-model="username" type="text"></el-input>
        <el-input v-model="password" type="password"></el-input>
        <el-button @click="login">登录</el-button>
      </div>
      <div class="blog-admin" v-show="isLogin">
        <el-tabs
            active-name="blogEdit">
          <el-tab-pane label="博客管理" name="blogList">
            博客管理
          </el-tab-pane>
          <el-tab-pane label="编写博客" name="blogEdit">
            <div class="blog-title">
              <span>标题:</span>
              <el-input v-model="blogTitle" style="width: 500px" type="text"></el-input>
            </div>
            <div id="blog-edit" style="height: 800px"></div>
          </el-tab-pane>
        </el-tabs>
      </div>
    </div>
  </div>
</template>

<style>
.admin-view {
  display: flex;
  justify-content: center;
  background-color: #f0f0f0;
}

.blog-title {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}
</style>