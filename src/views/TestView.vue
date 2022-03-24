<template>
  <!-- FeedList GET API test start -->
  <div>
    <p>***********************************</p>
    <h3>FeedList GET API test start</h3>
    <button @click="ADMINTEST">BM'sADMIN TEST</button>

    <div>
      <div v-for="Feed in FeedList" :key="Feed">
        <p>응애 나 {{ Feed.id }}번 아이디</p>
        <p>{{ Feed.name }}</p>
        <p>{{ Feed.get_userImage }}</p>
        <p>{{ Feed.get_postImage }}</p>
        <p>{{ Feed.likes }}</p>
        <p>{{ Feed.date }}</p>
        <p>{{ Feed.liked }}</p>
        <p>{{ Feed.content }}</p>
        <p>{{ Feed.filter }}</p>
        <div>
          <img :src="Feed.get_userImage" style="height: 300px; width: 200px" />
        </div>
      </div>
    </div>

    <h3>FeedList GET API test end</h3>
    <p>***********************************</p>
  </div>
  <!-- FeedList GET API test end -->

  <br />
  <br />

  <!-- FeedList POST API test start -->
  <div>
    <p>***********************************</p>
    <h3>FeedList POST API test start</h3>
    <form v-on:submit.prevent="POSTTEST">
      <div style="margin-top: 10px">
        <label for="name">Name : </label>
        <input
          type="text"
          id="name"
          placeholder="Your name"
          v-model="form.name"
        />
      </div>

      <div class="form-group" style="margin-top: 10px">
        <label for="name">userImage : </label>
        <input
          type="file"
          name="userImage"
          id="userImage"
          @change="onFileChange"
        />
      </div>

      <div class="form-group" style="margin-top: 10px">
        <label for="name">postImage : </label>
        <input
          type="file"
          name="postImage"
          id="postImage"
          @change="onFileChange"
        />
      </div>

      <div class="form-group" style="margin-top: 10px">
        <label for="name">content : </label>
        <input
          type="text"
          id="content"
          placeholder="content"
          v-model="form.content"
        />
      </div>

      <div style="margin-top: 10px">
        <button type="submit">feed post!</button>
      </div>
    </form>
    <div style="margin-top: 10px">
      <button @click="CheckOut">click and check console</button>
    </div>
    <h3>FeedList POST API test end</h3>
    <p>***********************************</p>
  </div>
  <!-- FeedList POST API test end -->

  <br />
  <br />

  <div>
    <button @click="PUTTEST">PUT TEST</button>
  </div>

  <div>
    <button @click="DELETETEST">DELETETEST</button>
  </div>

  <!-- 데이터바인딩 테스트 start -->
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      FeedList: '',
      form: {
        name: '',
        userImage: Image,
        postImage: Image,
        content: '',
      },
    };
  },
  methods: {
    ADMINTEST() {
      axios
        .get('http://127.0.0.1:8000/api/v1/feed/')

        .then((res) => {
          console.log(res.data);
          this.FeedList = res.data;
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
        .post('http://127.0.0.1:8000/api/v1/feed/', this.form)
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
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return alert('파일넣으셈');
      }

      console.log(e.target.id);
      this.userImage = files[0];
      console.log(this.userImage);
    },
    CheckOut() {
      console.log(this.form);
    },
  },
};
</script>

<style>
</style>