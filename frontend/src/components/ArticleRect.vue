<template>
  <div class="col-md-6 wrapper">
      <div class="ArticleRect" @click="goToDetailedPage()">
        <div class="title">{{topic.title}}</div>
        <div class="author">{{topic.author}}</div>
        <div class="content">{{topic.content}}</div>
        <!-- <hr> -->
      </div>
  </div>
</template>

<script>
export default {
  name: "New",
  props: {
    topic: null
  },
  components: {},
  data() {
    return {
    };
  },
  mounted:function(){
    //   console.log(this.topic);
  },
  methods:{
    goToDetailedPage: function(){
        this.$router.push({
            name:'article',
            query:{
                'id':this.topic.id,
                'title':this.topic.title,
                'author':this.topic.author,
                'time':this.topic.time||false,
                'from':this.topic.from,
                'content':'加载中',
            }
        })
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wrapper{
    padding: 15px 30px;
}

.ArticleRect {
    border-radius: 5px;
    padding: 15px 20px 15px 30px;
    cursor: pointer;
}

.ArticleRect:hover {
    transition: 400ms;
    background:#f6f6f7;
}

.title{
    font-size: 33px;
    /* font-weight: bold; */
    color: #000000;
}

.author{
    color: #585b60;
    font-size: 10px;
    margin: 5px 0 10px 0;
}

.content{
  margin-bottom: 15px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: box;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 8;
}

.common-btn{
    /* float: left; */
    color: white;
    background: #8cbf49;
    padding: 7px 14px;
    border-radius: 6px;
    cursor: pointer;
}
</style>


