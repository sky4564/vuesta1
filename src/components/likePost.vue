<template>
  <button @click="ADMINTEST">BM'sADMIN TEST</button>&&
  <button @click="POSTTEST">POST TEST</button>
  <button @click="PUTTEST">PUT TEST</button>
  <button @click="DELETETEST">DELETETEST</button>

  <button><router-link to="/test">테스트환경으로</router-link></button>

  <!-- 데이터바인딩 테스트 start -->

  <div>{{ coco }}</div>

  <hr />

  <div v-for="i in coco" :key="i.id">
    <p>{{ i.name }}</p>
    <p>{{ i.get_userImage }}</p>
    <p>{{ i.get_postImage }}</p>
    <p>{{ i.likes }}</p>
    <p>{{ i.date }}</p>
    <p>{{ i.liked }}</p>
    <p>{{ i.content }}</p>
    <p>{{ i.filter }}</p>
    <div>
      <img :src="i.get_userImage" style="height: 300px; width: 200px" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      image1: '',
      image2: '',
      coco: '',
    };
  },
  methods: {
    ADMINTEST() {
      axios
        .get('http://127.0.0.1:8000/api/v1/feed/')

        .then((res) => {
          console.log(res.data);
          this.coco = res.data;
        })

        .catch(function (err) {
          console.log(err);
          console.log('에러입니다.');
        })

        .then(function () {
          console.log('axios work');
        });
    },

    POSTTEST() {
      axios
        .post('http://127.0.0.1:8000/api/v1/feed/', {
          name: '사용자이름',
          content: 'post내용',
        })
        .then((res) => {
          console.log('POST WORK');
          console.log(res);
        })

        .catch((err) => {
          console.log('post error');
          console.log(err);
        })

        .then(() => {
          console.log('post post...');
        });
    },
  },
};
</script>

<style>
</style>
