<template>
  <div class="Homepage">
    <div class="Cover">
      <p style="font-weight:bold; margin-bottom:0;">Hello</p>
      <div class="greeting">
        你在
        <span id="locationFeature" style="opacity:0;transition: 500ms;">{{location}}</span>
        ，现在天气
        <span id="condFeature" style="opacity:0;transition: 500ms;">{{cond}}</span>
        。
        <br />
        <b style="font-style:italic;">速读</b> 祝你生活愉快。
      </div>
    </div>
    <div class="IAMWORKINGHARD">
      <div class="load-2">
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
      </div>速读正在火速加载中~
    </div>
    <Tabbar></Tabbar>
    <main role="main">
      <div id="sudu">今 日 速 读</div>
      <div class="container">
        <div class="row">
          <ArticleRect v-for="(item, i) in articleList" :key="i" :topic="item"></ArticleRect>
        </div>
      </div>
    </main>
    <Footer></Footer>
  </div>
</template>

<script>
import Tabbar from "@/src/components/Tabbar";
import Footer from "@/src/components/Footer";
import ArticleRect from "@/src/components/ArticleRect";

export default {
  name: "Homepage",
  props: {},
  data() {
    return {
      articleList: new Array(),
      location: "哪",
      cond: ""
    };
  },
  components: {
    Tabbar,
    Footer,
    ArticleRect
  },
  mounted: async function() {
    // if(this.$route.query!=)
    // if(loading_time="")
    this.getUserMsg();
    this.getData();
    this.addMoveHandler();
  },
  methods: {
    addMoveHandler() {
      window.onmousewheel = this.moveHandler;
    },
    moveHandler(e) {
      e = e || window.event;
      var t = 0;
      if (e.wheelDelta) {
        //IE/Opera/Chrome
        t = e.wheelDelta;
        if (t > 0) {
          return;
        } else if (t < 0) {
          this.moveHandlerEvent();
        }
      } else if (e.detail) {
        //Firefox
        t = e.detail;
        if (t < 0) {
          return;
        } else if (t > 0) {
          this.moveHandlerEvent();
        }
      }
    },
    moveHandlerEvent() {
      let ele = document.getElementsByClassName("Cover")[0];
      ele.style.display = "fixed";
      ele.style.opacity = 0;
      ele.style.fontSize = "14px";
      setTimeout(function() {
        document.getElementsByClassName("Cover")[0].style.display = "none";
      }, 500);
      window.onmousewheel = null;
    },
    getData: async function() {
      let topics = await this.api.getTopics();
      this.articleList = topics.data;
      console.log("[CHAOSZH] RETURN topics", topics);
      document.getElementsByClassName("IAMWORKINGHARD")[0].style.display =
        "none";
    },
    getUserMsg: async function() {
      let ip = await this.api.getIP();
      console.log("[CHAOSZH] RETURN ip", ip);
      ip = ip["data"];
      let location = await this.api.getLocation(ip);
      console.log("[CHAOSZH] RETURN location", location);
      this.location = location["data"];
      document.getElementById("locationFeature").style.opacity = 1;
      let weather = await this.api.getWeather(this.location);
      this.cond = weather.data["cond"];
      document.getElementById("condFeature").style.opacity = 1;
      console.log("[CHAOSZH] RETURN weather", weather);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.Cover {
  position: fixed;
  top: 0;
  background: #0085d1;
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 2;
  transition: 500ms;
  /* beautify */
  font-size: 140px;
  color: #ffffff;
}

.Cover .greeting {
  font-size: 26%;
  text-align: center;
}

.IAMWORKINGHARD {
  background: #ffffff;
  position: fixed;
  top: 0;
  width: 100vw;
  height: calc(100vh - 60px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* beautify */
  font-size: 20px;
}

.Homepage {
  padding-top: 60px;
}

#sudu {
  font-weight: bold;
  background: #0085d1;
  color: #ffffff;
  text-align: center;
  font-size: 45px;
  /* margin-top: 30px; */
  padding-bottom: 35px;
  margin-bottom: 20px;
  /* box-shadow: #00000055 0px 0px 12px; */
}

.common-navbar-brand:hover {
  background: #ffffff28;
}

.common-home-btn {
  display: block;
  color: #ffffff;
  /* padding: 0 3px; */
  /* letter-spacing: 5px; */
}

.common-weather-rect {
}

/* test */
.undone {
  background: #feffb4;
  border-radius: 4px;
}

.line {
  display: inline-block;
  width: 15px;
  height: 15px;
  border-radius: 15px;
  background-color: #4b9cdb;
}

.load-2 {
  display: block;
  margin-bottom: 20px;
}

.load-2 .line:nth-last-child(1) {
  animation: loadingB 1.5s 1s infinite;
  margin-left: 5px;
}
.load-2 .line:nth-last-child(2) {
  animation: loadingB 1.5s 0.5s infinite;
}
.load-2 .line:nth-last-child(3) {
  animation: loadingB 1.5s 0s infinite;
  margin-right: 5px;
}

@keyframes loadingB {
  0 {
    width: 15px;
  }
  50% {
    width: 35px;
  }
  100% {
    width: 15px;
  }
}
</style>
