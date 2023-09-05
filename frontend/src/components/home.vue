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

  <form @submit.prevent="AiFunction">

    <div class="search-container">
      <input class="search-input" type="text" placeholder="Search 2M+ Recipes" id="keyword" v-model="keyword">
      <button class="search-button">Search</button>
    </div>

  </form>

  <br><br>

 
  <div>
    <div v-if="mydata && mydata.length > 0">
      <div v-for="item in mydata" :key="item.id" class="recipe-item">
        <div class="recipe-image">
          <img :src="'https://source.unsplash.com/600x400/?' + item.title" alt="">
        </div>
        <div class="recipe-details">
          <h3>{{ item.title }}</h3>


          <div style="display: flex; justify-content:space-evenly; flex-wrap:wrap" class="ing_div">
          <div class="recipe-ingredients">
            <h4>Ingredients:</h4>
            <ul>
              <li v-for="ingredient in item.ingredients" :key="ingredient">{{ ingredient }}</li>
            </ul>
          </div>


          <div class="recipe-instructions">
            <h4>Instructions:</h4>
            <ul>
              <li v-for="instruction in item.instructions" :key="instruction">{{ instruction }}</li>
            </ul>
          </div>
        </div>


        </div>
      </div>
    </div>
  </div>
  

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



  <!-- <p> {{ typeof(mydata) }} </p> -->
  <!-- <p> {{ mydata }} </p> -->


 


  <br><br><br>
  <hr>
</template>

<script>
import axios from "axios";
// import Swal from "sweetalert2";
export default {
  name: "HomePage",

  data() {
    return {
      keyword: "",
      mydata: ""

    };
  },
  methods: {
    AiFunction() {
      const recipeData = {
        keyword: this.keyword,
      };

      console.log(recipeData)
      axios.post('http://localhost:8000/gpt/', recipeData)
        .then((response) => {
          if (response.status === 201) {
            // let data = response.data
            console.log('successfull:', response.data);
          
            this.mydata = response.data.gpt3_output
            // console.log(this.mydata)
          } else {
            alert("error")
          }
        })
        .catch((error) => {
          console.error('Error creating gpt:', error);
          alert("error")
        });
    }
  }
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
  flex-wrap: wrap;

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

  flex-wrap: wrap;

}

/* Style for the search input */
.search-input {
  width: 400px;
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
}



/*gpt recipe css  */
/* Recipe item container */
.recipe-item {
  display: grid;
  grid-template-columns: 40% 60%;
  gap: 10px;
  align-items: center;
  border: 1px solid #ddd;
 
  padding: 10px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
  box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
}

.recipe-item>div{
  box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
}

/* Recipe image container */
.recipe-image {
  
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  overflow: hidden;
}


/* Recipe details container */
.recipe-details {
  padding: 20px;
}

/* Recipe title */
.recipe-details h3 {
  font-size: 24px;
  margin: 0;
  text-align: center;
  background-color: rgba(36, 186, 104, 0.315);
  padding: 10px 0;
  border-bottom: 1px solid #ddd;
}

/* Ingredients and Instructions */
.recipe-ingredients{
  margin-top: 20px;
  text-align: left;
  width: 40%;

}
.recipe-instructions {

  margin-top: 20px;
  text-align: left;
  width: 60%;
}

/* Ingredients and Instructions titles */
.recipe-ingredients h4,
.recipe-instructions h4 {
  font-size: 18px;
  margin-top: 10px;
  font-weight: bold;
}

/* Ingredients and Instructions lists */
.recipe-ingredients ul,
.recipe-instructions ul {
  list-style: none;
  padding: 0;
}

/* Ingredients and Instructions list items */
.recipe-ingredients li,
.recipe-instructions li {
  margin-left: 0;
  font-size: 16px;
  padding-left: 20px;
  position: relative;
}

/*  MEDIA QUERY */


/* Styles for screens up to 768px wide (Mobile) */
@media screen and (max-width: 768px) {

  .recipe-item {
    display: grid;
    grid-template-columns: 100%;
     }
   
     .recipe-image {
      display: grid;
      place-items: center;
       width: 100%;
       border-top-right-radius: 0;
       border-bottom-left-radius: 5px;
     }
   
     .recipe-details {
       width: 100%;
     }
   
     .ing_div{
      flex-direction: column;
     }
   

  /* Add specific mobile styles here */
}

/* Styles for screens between 769px and 1024px wide (Tablet) */
@media screen and (min-width: 769px) and (max-width: 1024px) {

  .recipe-item {
    display: grid;
    grid-template-columns: 100%;
     }
   
     .recipe-image {
       width: 100%;
       display: grid;
      place-items: center;
       border-top-right-radius: 0;
       border-bottom-left-radius: 5px;
     }
   
     .recipe-details {
       width: 100%;
     }
   
 
  
}

/* Styles for screens between 1025px and 1440px wide (Laptop) */
@media screen and (min-width: 1025px) and (max-width: 1440px) {

  /* Add specific laptop styles here */
}

/* Styles for screens wider than 1440px (Extra Large) */
@media screen and (min-width: 1441px) {

  /* Add specific extra-large screen styles here */
}





</style>