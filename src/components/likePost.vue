
<template>
  <div>
  <div>{{coco}}</div>
  <div v-for="i in coco" :key="i.id">
      {{ i.name }}  <br>
      {{ i.userImage }} <br>
      {{ i.postImage }} <br>
      {{ i.likes }} <br>
      {{ i.date }} <br>
      {{ i.liked }} <br>
      {{ i.content }} <br>
      {{ i.filter }} <br>

  </div>
  <button @click="ADMINTEST">ADMIN TEST</button>
  <button @click="likepost">post</button>
  <button @click="likeput">put</button>  
    
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data () {
        return {
            image1: '',
            image2: '',

            coco: ''
        }
    },
    methods : {
        ADMINTEST(){
            axios
                .get('http://127.0.0.1:8000/api/v1/feed/')
                .then((res) => {
                console.log(res.data)
                this.coco = res.data
                })
                .catch(err => {
                    console.log(err)
                    console.log('에러야 ㅄ아')

                })
        },
        likepost(){
            axios.post('https://reqres.in/api/users',{
                id : "2224",
                title : "post 2224"
            }).then((results) => {
            console.log(results.data);
            });

        },
        likeput(){
            axios.put('https://my-json-server.typicode.com/typicode/demo/posts',{
                id : "3",
                title : "aaa"
            }).then((results) => {
            console.log(results.data);
            });

        }

    }
}
</script>

<style>

</style>