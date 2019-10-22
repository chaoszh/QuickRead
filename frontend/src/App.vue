<template>
  <div id="app">
      
    <!-- <script src="https://unpkg.com/vue-router/dist/vue-router.js"></script> -->
    <router-view></router-view>
    <!-- <Tabbar></Tabbar>
    <Homepage></Homepage> -->
  </div>
</template>

<script>
export default {
  name: "app",
  components: {
  },
  mounted: function(){

  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center;
  color: #2c3e50;
  margin-top: 60px; */
}
</style>
