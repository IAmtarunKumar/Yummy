<template>
  <div class="slider-container">
    <hr>
    <div class="slider">
      <div class="slide"><img src="../img/burgur.jpeg" alt="Image 1"></div>
      <div class="slide"><img src="../img/daal.jpeg" alt="Image 2"></div>
      <div class="slide"><img src="../img/sweet.jpeg" alt="Image 3"></div>
    </div>
  </div>
  <hr>

  <!-- Search Box  -->



  <h1>
    <Center style="color: rgb(9, 41, 9);">Discover Your Favorite Dish</Center>
  </h1>
  <br>
  <div class="search-container">
    <input class="search-input" type="text" placeholder="Search 2M+ Recipes">
    <button class="search-button">Search</button>
  </div>

  <br><br>



  <br><br><br>
  <hr>
  <h1>
    <center>Just For You</center>
  </h1>
  <div id="dishMenu">
    <div>
      <img src=" https://source.unsplash.com/300x200/?burgur" alt="">
      <h5>Burger Delight</h5>
      <span style="font-weight: bold;"> Description </span> <span>:</span> <span> Sink your teeth into our mouthwatering
        burgers that are cooked to perfection. Each bite is a flavor explosion, with juicy patties, fresh vegetables, and
        our secret sauce. Satisfy your cravings with the best burgers in town.</span>
    </div>

    <div>
      <img src=" https://source.unsplash.com/300x200/?soup" alt="">
      <h5>Crispy Chicken Classics</h5>
      <span style="font-weight: bold;"> Description </span> <span>:</span> <span> Description: Our crispy chicken classics
        are a crispy, crunchy, and flavorful treat. Tender chicken, coated with a special blend of herbs and spices, is
        fried to golden perfection. Whether in a sandwich, bucket, or combo meal, it's a taste that's hard to
        resist..</span>
    </div>

    <div>
      <img src=" https://source.unsplash.com/300x200/?pizza" alt="">
      <h5>Pizza Paradise</h5>
      <span style="font-weight: bold;"> Description </span> <span>:</span> <span> Experience pizza like never before at
        Pizza Paradise. Our handcrafted pizzas feature a variety of toppings, a perfectly baked crust, and a rich tomato
        sauce. From classic Margherita to gourmet specialties, there's a slice for everyone.</span>
    </div>

    <div>
      <img src=" https://source.unsplash.com/300x200/?food" alt="">
      <h5>Taco Fiesta</h5>
      <span style="font-weight: bold;"> Description </span> <span>:</span> <span> Join the fiesta with our delicious tacos
        bursting with authentic flavors. Soft or crunchy, our tacos are filled with savory meats, fresh salsa, and zesty
        toppings. Get ready to savor the taste of Mexico right in your neighborhood.</span>
    </div>





  </div>

  <br><br><br>
  <hr>
</template>

<script>
export default {
  name: "HomePage"
}

</script>


<style scoped>
.slider-container {
  width: 100%;
  /* Adjust the width as needed */
  max-height: 400px;

  overflow: hidden;
  position: relative;
}

.slider {
  display: flex;
  animation: slide 4s linear infinite;

}


.slide {
  flex: 0 0 100%;
  /* Each slide takes up 100% of container width */
}

/* Auto sliding animation */
@keyframes slide {

  0%,
  25% {
    transform: translateX(0);
  }

  50%,
  75% {
    transform: translateX(-100%);
  }

  100% {
    transform: translateX(-200%);
  }
}



/* Add some styling for the images */
img {
  max-width: 100%;
  height: auto;
}

#dishMenu {
  display: flex;
  justify-content: space-evenly;
  align-items: center;


}

#dishMenu div {
  box-shadow: rgba(0, 0, 0, 0.19) 0px 10px 20px, rgba(0, 0, 0, 0.23) 0px 6px 6px;

  width: 300px;

  padding: 20px;
}

#dishMenu>div>h5 {
  text-align: center;

}



.search-container {
  display: flex;
  justify-content: center;
  align-items: center;


}

/* Style for the search input */
.search-input {
  width: 800px;
  padding: 10px;
  border: none;
  border-radius: 20px;
  font-size: 25px;
  box-shadow: 0px 2px 4px rgba(5, 4, 4, 0.995);
  outline: none;
}

/* Style for the search button */
.search-button {
  background-color: #082b19;
  color: white;
  border: none;
  border-radius: 20px;
  padding: 10px 60px;
  margin-left: 10px;
  cursor: pointer;
  font-size: 22px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
}

/* Hover effect for the search button */
.search-button:hover {
  background-color: #0056b3;
}</style>