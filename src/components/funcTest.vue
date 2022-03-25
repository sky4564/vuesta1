<template>
  <button @click="TernaryConditional"> 삼항 연산자 작동</button><br>
  <p>{{weapon}}</p>

</template>

<script>
export default {
    data() {
        return {
            isKing : true,
            weapon : " ",
        
        }   
    },

    methods : {
        TernaryConditional(){
            this.weapon = this.isKing ? "kingsword" : "sword"
        }
    }


}
</script>

<style>

</style>