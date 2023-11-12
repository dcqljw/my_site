<script>
// import Cherry from "cherry-markdown";
import "cherry-markdown/dist/cherry-markdown.min.css"

export default {
  data() {
    return {
      content: '<div data-inline-code-theme="red" data-code-block-theme="tomorrow-night"><h1 data-lines="1" data-sign="e89628827479e88c8a5ea6c040f7c15d" id="welcome" class="cherry-highlight-line"><a href="#welcome" class="anchor"></a>welcome</h1></div>'
    }
  },
  mounted() {
    // this.cherryInstance = new Cherry({
    //   value: "# welcome"
    // })
  }
}


</script>

<template>
  <div>
    <div v-html="content"></div>
  </div>
</template>

<style scoped>
div {
  color: white;
}
</style>