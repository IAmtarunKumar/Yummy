<template>
   <!-- nav bar start  -->
   <div id="main">
    <div id="img">
      <img src="https://uploads-ssl.webflow.com/5966ea9a9217ca534caf139f/596d33f36607b12cfdaf8ad2_LogoWhite.png" alt="" width="40" class="failory-logo-image"><span>
        <h4>Yummy</h4>
      </span>
      
    </div>

    <div id="menu">
    <div><a href="/">Home</a></div>
    <div><a href="/recipe">Recipe</a></div>
   
    
    <div><a href="/Community">Community</a></div>
    <div><a href="/login">Login</a></div>
    <div><a href="/logout">Logout</a></div> 
  </div>
   </div>
     <!-- nav  end  -->
   

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

#menu>div>a{
  text-decoration: none;
  color: white;
  font-weight: 600;
}


</style>