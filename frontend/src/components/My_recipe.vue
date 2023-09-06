<template>
    <div>
      <h1><center>Show My Recipes</center></h1>
      <button @click="createRecipe">Create Recipe</button>
  
      <!-- Display the mydata as cards -->
      <div class="recipe-card" v-for="(recipe, index) in mydata" :key="index">
        <h2>{{ recipe.title }}</h2>
        <div class="recipe-details">
          <p><strong>Title:</strong> {{ recipe.title }}</p>

          <p><strong>Ingredients:</strong> {{ recipe.ingredients }}</p>

          <p><strong>Instructions:</strong> {{ recipe.instructions }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Swal from 'sweetalert2';
  
  export default {
    name: "My_Recipe",
  
    data() {
      return {
        mydata: []
      };
    },
  
    methods: {
      createRecipe() {
        axios.get('http://localhost:8000/my_recipe/')
          .then((response) => {
            if (response.status === 200) {
              console.log('Recipes retrieved successfully:', response.data);
              this.mydata = response.data; // Assign the response data to mydata

              console.log(response.data)
              Swal.fire({
                position: 'center',
                icon: 'success',
                title: 'Recipes Retrieved Successfully',
              });
            } else {
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Something went wrong!'
              });
            }
          })
          .catch((error) => {
            console.error('Error retrieving recipes:', error);
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Something went wrong!'
            });
          });
      }
    }
  }
  </script>
  
  <style scoped>
  /* Style for the recipe cards */
  .recipe-card {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background-color: #fff;
  }
  
  .recipe-details {
    margin-top: 10px;
  }
  </style>
  