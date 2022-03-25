<template>
  <!-- FeedList GET API test start -->
  <div>
    <p>***********************************</p>
    <h3>FeedList GET API test start</h3>
    <button @click="ADMINTEST">BM'sADMIN TEST</button>

    <div>
      <div v-for="Feed in FeedList" :key="Feed">
        <p>응애 나 {{ Feed.id }}번 아이디</p>
        <p>name : {{ Feed.name }}</p>
        <div>
          <p>userImage</p>
          <img :src="Feed.get_userImage" style="height: 300px; width: 200px" />
        </div>
        <div>
          <p>postImage</p>
          <img :src="Feed.get_postImage" style="height: 300px; width: 200px" />
        </div>
        <p>likes : {{ Feed.likes }}</p>
        <p>date : {{ Feed.date }}</p>
        <p>좋아요했니? : {{ Feed.liked }}</p>
        <p>content : {{ Feed.content }}</p>
        <p>사진필터 : {{ Feed.filter }}</p>
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
    <form v-on:submit.prevent="POSTTEST" enctype="multipart/form-data">
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
          id="userImage"
          ref="userImage"
          @change="onFileChange"
        />
      </div>

      <div class="form-group" style="margin-top: 10px">
        <label for="name">postImage : </label>
        <input
          type="file"
          id="postImage"
          ref="postImage"
          @change="onFileChange2"
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
        userImage: '',
        postImage: '',
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
          console.log('axios work');
        })

        .catch(function (err) {
          console.log(err);
          console.log('에러입니다.');
        });
    },

    POSTTEST() {
      const formData = new FormData();
      formData.append('name', this.form.name);
      formData.append('userImage', this.form.userImage);
      formData.append('postImage', this.form.postImage);
      formData.append('content', this.form.content);

      axios
        .post('http://127.0.0.1:8000/api/v1/feed/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        .then((res) => {
          console.log('POST WORK');
          console.log(res);
        })

        .catch((err) => {
          console.log('post error');
          console.log(err);
        });
    },

    onFileChange() {
      this.form.userImage = this.$refs.userImage.files[0];
    },
    onFileChange2() {
      this.form.postImage = this.$refs.postImage.files[0];
    },
    CheckOut() {
      console.log(this.$data.form);
    },
  },
};
</script>

<style>
</style>