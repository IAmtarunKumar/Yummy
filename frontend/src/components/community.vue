<template>

<h1 style="background-color: rgba(128, 128, 128, 0.463); padding:10px"><Center>Community Form</Center></h1>
<hr>
<div id="search">
<textarea name="" id="" cols="30" rows="10"></textarea>
<br>
<button id="search_btn">submit</button>
</div>

<br><br>
</template>

<script>
export default{
    name : "CommunityPage"
}
</script>

<style scoped>

#search{
    widows: 80%;
    margin-left: 10%;
    margin-right: 10%;
    
}
#search>textarea{
    width: 100%;
    height: 200px;
    border: 2px solid rgb(5, 62, 16);
    border-radius: 10px;
    padding: 20px;
}
#search_btn{
    margin-left: 88%;
    font-size: 20px;
    padding: 5px 40px;
    border: none;
    background-color: rgb(12, 41, 12);
    border-radius: 10px;
    color: white;
    font-weight: bold;
}

</style>