<template>
  <div class="recipe-form">
    <br /><br />
    <form @submit.prevent="createRecipe">
      <h2>Create a New Recipe</h2>
      <div class="form-group">
        <label for="title">Recipe Title</label>
        <input type="text" id="title" v-model="title" required />
      </div>
      <div class="form-group">
        <label for="ingredients">Ingredients</label>
        <textarea id="ingredients" v-model="ingredients" required></textarea>
      </div>
      <div class="form-group">
        <label for="instructions">Instructions</label>
        <textarea id="instructions" v-model="instructions" required></textarea>
      </div>
      <button>Create Recipe</button>
    </form>
    <br /><br />
  </div>
</template>

<script>
import axios from "axios";
import Swal from "sweetalert2";

export default {
  name: "CreateRecipe",

  data() {
    return {
      title: "",
      ingredients: "",
      instructions: "",
    };
  },

  methods: {
    createRecipe() {
      let localStorage_data = JSON.parse(localStorage.getItem("data"));
      let user_id = localStorage_data["user_id"];

      const recipeData = {
        user_id: user_id,
        title: this.title,
        ingredients: this.ingredients,
        instructions: this.instructions,
      };

      axios
        .post("https://django-chack.onrender.com/api/post/my_recipe/", recipeData)
        .then((response) => {
          if (response.status === 201) {
            console.log("Recipe created successfully:", response.data);
            Swal.fire({
              position: "center",
              icon: "success",
              title: "Recipe Created Successfully",
            });

            // Clear the form fields after successful creation
            this.title = "";
            this.ingredients = "";
            this.instructions = "";
          } else {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Something went wrong!",
            });
          }
        })
        .catch((error) => {
          console.error("Error creating recipe:", error);
          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Something went wrong!",
          });
        });
    },
  },
};
</script>

<style scoped>
.recipe-form {
  display: flex;
  justify-content: center;
  align-items: center;
  background: url(https://i.pinimg.com/736x/31/2a/a9/312aa900f902fe472a775157adc89157.jpg);
}

form {
  padding: 50px;
  background-color: #3663328b;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  color: #333;
  margin-bottom: 20px;
  background-color: #366332fe;
  color: white;
  padding: 10px;
  border-radius: 5px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  font-weight: 700;
  font-size: 20px;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  color: #555;
}

textarea {
  width: 100%;
  height: 100px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  color: #555;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
