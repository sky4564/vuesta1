<template>
  <div class="post">
    <div class="post-header">
      <div class="profile"></div>
      <span class="profile-name">{{게시물.name}}</span>
    </div>
    <div class="post-body" :style="{backgroundImage : `url(${게시물.postImage})`}"> </div>
    <!-- es6 신문법  style 데이터 바인딩 할때 `백틱`쓰면 `안에있는것중에 $ {이것만 데이터처리} ` 나머지는 텍스트로 읽으니 ok -->
    <div class="post-content">
      <p>{{게시물.likes}}</p>
      <p><strong>{{게시물.name}}</strong> {{게시물.content}}</p>
      <p class="date">{{게시물.date}}</p>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {

      }
    },
    props : {
      게시물 : Object,
      
    }
  }
</script>

<style>

</style>