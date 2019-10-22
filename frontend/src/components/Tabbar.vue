<template>
  <div class="Tabbar">
    <div class="homebtn">
        <div class="logo" @click="routeTo('homepage')">
            HOMEPAGE
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Tabbar",
  props: {

  },
  methods:{
    routeTo: function(routerName){
        this.$router.push({
            name: routerName,
            params: {

            }
        })
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.Tabbar {
  width: 100%;
  height: 60px;
  background: #0085d1;
  display: flex;
  align-items: center;
  position: fixed;
  top:0;
  z-index: 1;
}

.homebtn {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 40px;
  padding: 0 15px;
  margin-left: 15px;
  border-radius: 4px;
  font-size: 15px;
  color: #ffffffcc;
  transition: 0.3s;
}

.homebtn:hover {
  color: #ffffff;
  background: #ffffff28;
  /* padding: 0 3px; */
  /* letter-spacing: 5px; */
}

.homebtn .logo::before{
    content: " ";
    display: block;
  height: 30px;
  width: 30px;
  margin-right: 5px;
  background: url("../assets/logo.svg") no-repeat;
  background-size: cover;
}

.homebtn .logo{
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
