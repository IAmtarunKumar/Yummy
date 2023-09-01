<template>
   <!-- nav bar start  -->
   <div id="main">
    <div id="img">
      <p>Yummy</p>
    </div>

    <div id="menu">
    <div>Home</div>
    <div>Recipe</div>
    <div><a href="/sign">Sign In</a></div>
    <div><a href="/login">Sign Up</a></div>
 
  </div>

   </div>
     <!-- nav bar end  -->
   

</template>

<script>
export default{
    name : "NavBar"
}



</script>


<style scoped>
#main{
  display: flex;
  justify-content: space-between;
  align-items: center;
 
  background-color: rgb(9, 43, 9);
  color: white;
}

#img{
width: 40%;
display: flex;
align-items: center;
margin-left: 60px;
margin-top: 10px;

}
#img>p{
  font-size: 30px;
  font-weight: bold;
}

#menu{
  width: 40%;
  display: flex;
  align-items: center;
  justify-content: space-evenly;

  font-size: 20px;
  font-family: Arial, Helvetica, sans-serif;
  padding: 10px;
}



</style>