
<template>
  <div>
<!-- 데이터바인딩 테스트 start -->

  <div>{{coco}}</div>

  <hr>

  <div v-for="i in coco" :key="i.id">
    <p>{{ i.name }} </p> 
    <p>{{ i.get_userImage }}</p> 
    <p>{{ i.get_postImage }}</p> 
    <p>{{ i.likes }}</p> 
    <p>{{ i.date }}</p> 
    <p>{{ i.liked }}</p> 
    <p>{{ i.content }}</p> 
    <p>{{ i.filter }}</p> 
    <div>
        <img :src="i.get_userImage" 
            style="height:300px; width:200px">
    </div>

    <hr>
  </div>

<!-- 데이터바인딩 테스트 end -->

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

            coco: []
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