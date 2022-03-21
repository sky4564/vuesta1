<template>
        <div id="btn_group"> 
            <button @click="goFront" type="button">FRONT</button> [1]
            <button @click="goBack" type="button">BACK</button> 
            <button @click="goHome" type="button">HOME</button> 
        </div> 
</template>

<script>
export default {
    methods:{
        goFront(){
            this.$router.go(1);
        },
        goBack(){
            this.$router.go(-1); [2]
        },
        goHome(){
            this.$router.push('/'); [3]
        }
    }
}
</script>

<style>

</style>