
<template>
  <button @click="ADMINTEST">ADMIN TEST</button>
  <button @click="likepost">post</button>
  <button @click="likeput">put</button>
</template>

<script>
import axios from 'axios'
export default {
    methods : {
        ADMINTEST(){
            axios.get('https://reqres.in/api/users').then((res) => {
            console.log(res.data);
            });
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