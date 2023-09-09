<template>
    <div class="recipe-page">
      <hr>
      <h1 class="center-text">Unlock Culinary Creativity with Custom Recipes</h1>
  
      <div id="recipe-box" class="container">
        <div class="cr cr-created">
          <a href="/recipe"><i class="fas fa-list-ul"></i> Created Recipes</a>
        </div>
        <div class="cr cr-create">
          <a href="/recipe"><i class="fas fa-plus-circle"></i> Create Recipes</a>
        </div>
      </div>
      <br>
  
      <form @submit.prevent="AiFunction">
        <div class="form-box">
          <div class="form-group">
            <label for="cuisines">What are your favorite cuisines?</label>
            <select name="cuisines" id="cuisines" v-model="cuisines" required>
              <option value="AMERICAN">AMERICAN</option>
              <option value="">Select</option>

              <option value="KID-FRIENDLY">KID-FRIENDLY</option>
              <option value="ITALIAN">ITALIAN</option>
              <option value="ASIAN">ASIAN</option>
              <!-- Add more cuisine options here -->
            </select>
          </div>
  
       


          <div class="form-group">
            <label for="follow_diets">Do you follow any of these diets?</label>
            <select name="follow_diets" id="follow_diets"  v-model="follow_diets" required>
              <option value="">Select</option>

              <option value="VEGETARIAN">VEGETARIAN</option>
              <option value="LOW-FODMAP">LOW-FODMAP</option>
              <option value="VEGAN">VEGAN</option>
              <!-- Add more diet options here -->
            </select>
          </div>
        </div>

        
  
        <div class="form-box">
         
  
          <div class="form-group">
            <label for="allergies">Do you have any food allergies?</label>
            <select name="allergies" id="allergies" v-model="allergies" required>
              <option value="">Select</option>

              <option value="WHEAT-FREE">WHEAT-FREE</option>
              <option value="DAIRY-FREE">DAIRY-FREE</option>
              <option value="PEANUT-FREE">PEANUT-FREE</option>
              <!-- Add more allergy options here -->
            </select>
          </div>

          <div class="form-group">
            <label for="skills">How would you describe your cooking skills?</label>
            <select name="skills" id="skills" v-model="skills" required >
              <option value="">Select</option>

              <option value="BEGINNER">BEGINNER</option>
              <option value="INTERMEDIATE">INTERMEDIATE</option>
              <option value="ADVANCED">ADVANCED</option>
            </select>
          </div>
        </div>
  
        <div class="form-box">
        
          <div class="form-group">
            <label for="ingredients_not">Any ingredients you don't want to see in your recommended recipes? (User "," for multiple ingredient)</label>
            <input type="text" name="ingredient_not" id="ingredients_not" v-model="ingredients_not" required>
          </div>
  
          <div class="form-group">
            <button class="submit-button">Submit</button>
          </div>
        </div>
      </form>
    </div>

    <br><br>


    <div v-if="search===true && mydata=='' " >
      <div style="display: flex; justify-content: center; ">
        <img src="https://media.tenor.com/On7kvXhzml4AAAAi/loading-gif.gif" alt="">
       <!-- <img src="../img/gifimag.gif" alt=""> -->
     
  
    </div>
    <br>
    <h3>
        <Center> {{ msg="Recipes is processing...." }} </Center>
    </h3>
     </div>




   
 
  <div>
    <div v-if="mydata && mydata.length > 0">
      <div v-for="item in mydata" :key="item.id" class="recipe-item">
        <div class="recipe-image">
          <img :src="'https://source.unsplash.com/600x400/?recipe' + item.title" alt="">
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
  

   <br><br>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "HomePage",
  
    data() {
      return {
        cuisines : "",
        ingredients_not : "",
        skills : "",
        allergies : "",
        follow_diets : "",
        mydata: "",
        search : false
      };
    },
    methods: {
  AiFunction() {
    this.search=true
    // Assuming you want to make a search request here
    const recipeData = {
      cuisines: this.cuisines,
      ingredients_not: this.ingredients_not,
      skills: this.skills,
      allergies: this.allergies,
      follow_diets: this.follow_diets,
    };

    console.log(recipeData)
    axios.post('https://django-chack.onrender.com/custom/', recipeData)
      .then((response) => {
      // Check for the appropriate status code
          console.log('Successful search:', response.data);
          this.mydata = response.data.gpt3_output;
      
      })
      .catch((error) => {
        console.error('Error searching for recipes:', error);
        // Handle the error appropriately, e.g., show an error message to the user
      });
  }
}

  }
  </script>
  
  <style scoped>
  @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');
  
  .recipe-page {
    background-color: #f5f5f5;
    padding: 20px;
    font-family: Arial, sans-serif;
   
  }
  
  .center-text {
    text-align: center;
    margin-top: 20px;
  }
  
  .container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    margin: 0;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
  }
  
  .cr {
    flex: 1;
    padding: 20px;
    text-align: center;
    color: #333;
    text-decoration: none;
    font-weight: bold;
    transition: background-color 0.3s, color 0.3s;
    border: 2px solid #009688;
    border-radius: 5px;
    margin: 10px;
  }
  
  .cr:hover {
    background-color: #009688;
    color: #fff;
  }
  
  form{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
  }
  .form-box {
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    margin: 10px;
    padding: 20px;
    width: 100%;
    
    
  }
  
  .form-group {
    margin-bottom: 20px;
   widows: 100%;
  }
  
  .form-group label {
    font-weight: bold;
  }
  
  .form-group select,
  .form-group input[type="text"] {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .submit-button {
    background-color: #009688;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
    text-align: center;
  }
  
  .submit-button:hover {
    background-color: #007a66;
  }
  
  @media screen and (min-width: 768px) {
    .container {
      flex-wrap: nowrap;
    }
  
    .form-box {
      width: calc(50% - 20px);
    }
  }



  /* APENDING RECIPE CSS */
  .recipe-page {
    background-color: #f5f5f5;
    padding: 20px;
    font-family: Arial, sans-serif;
    
  }
  
  .center-text {
    text-align: center;
    margin-top: 20px;
  }
  
  .recipe-card {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px;
    border-radius: 5px;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .recipe-card h2 {
    font-size: 24px;
    margin-bottom: 10px;
  }
  
  .recipe-card h3 {
    font-size: 18px;
    margin-top: 10px;
  }
  
  ul, ol {
    margin-left: 20px;
  }
  
  @media screen and (max-width: 768px) {
    .recipe-card {
      margin: 10px 0;
    }
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


  }
  
  .recipe-item>div{
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
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
  