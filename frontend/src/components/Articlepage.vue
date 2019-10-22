<template>
  <div class="Articalpage">
    <Tabbar></Tabbar>
    <main role="main">
      <div class="container">
        <div class="common-article">
          <div class="common-article-title">{{topic.title}}</div>
          <hr />
          <div class="common-article-description">
            <span class="author">{{topic.author}}</span>
            <span class="time" v-bind:style="{display:isTimeShowed}">{{topic.time}}</span>
          </div>
          <div class="common-article-content">
            {{topic.content}}
          </div>
        </div>
      </div>
    </main>
    <Footer></Footer>
  </div>
</template>

<script>
import Tabbar from "@/src/components/Tabbar"
import Footer from "@/src/components/Footer"
export default {
  name: "Articalpage",
  props: {

  },
  data() {
      return {
          topic:{
                'title':'加载中',
                'author':'加载中',
                'time':'加载中',
                'content':'加载中',
          }
      }
  },
  computed:{
      isTimeShowed: function(){
          return this.topic.time != 'false'?'flex':'none';
      },
  },
  components: {
        Tabbar,
        Footer,
    },
  mounted: function(){
      console.log(this.$route.query);
      this.getData(this.$route.query);
  },
  methods: {
      getData : async function(param){
          this.topic=param;
          let topic = await this.api.getTopic(param);
          console.log("[CHAOSZH] RETURN topic", topic.data);
          let length = topic.data['content'].length;
          let content = topic.data['content'];
          this.topic.content=content;
          $('.common-article-content').html(content);
          console.log(typeof(content));
      }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* @import url('../css.markdown.css'); */
.Articalpage{
    padding-top: 80px;
}

/* article.html */
.common-article {
  padding: 20px 5%;
}
.common-article-title {
  font-size: 38px;
  font-weight: bold;
}
.common-article-description {
  display: flex;
  color: #999999;
  font-size: 13px;
  padding-bottom: 30px;
  line-height: 15px;
  vertical-align: middle;
}

.common-article-description .author,
.common-article-description .time {
  display: flex;
  align-items: center;
  margin-right: 20px;
}

.common-article-description .author::before {
  content: "";
  display: inline-block;
  background: url(../assets/person.svg) no-repeat;
  height: 24px;
  width: 24px;
  background-size: cover;
  margin-right: 10px;
}

.common-article-description .time::before {
  content: "";
  display: inline-block;
  background: url(../assets/time.svg) no-repeat;
  height: 22px;
  width: 22px;
  margin: 2px;
  background-size: cover;
  margin-right: 10px;
}

.common-article-content {
  /* text-indent: 2em; */
  /* white-space: pre-line; */
  all:initial;
}

img{
    width: 70%;
}
</style>
