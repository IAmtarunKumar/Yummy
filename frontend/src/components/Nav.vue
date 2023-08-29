<template>
   <!-- nav bar start  -->

   <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link "  href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Recipe</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link"  >Login/SignUp</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

   <!-- nav bar end  -->
   

</template>

<script>
export default{
    name : "NavBar"
}



</script>


<style scoped>


li{
    margin-left: 70px;
    font-size: 18px;
    
}
li>a{
    color: blue;
}

</style>