import {createWebHistory , createRouter} from 'vue-router'

// import Home from './components/Home.vue'



import Login from './components/Login.vue';
import SignIn from './components/Sign.vue'
import Home from './components/home.vue'
import Recipe from './components/Recipe.vue'
import Community from './components/community.vue'
import Logout from './components/Logout.vue'
import Create_Recipe from './components/Create_recipe.vue'
import My_recipes from './components/My_recipe.vue'


const routes = [
    {
        name : "SignIn",
        path : "/sign",
        component : SignIn,
    },

    {
        name : "Login",
        path : "/login",
        component : Login,
    },
    {
        name : "Home",
        path : "/",
        component : Home
    },
    {
        name : "Recipe",
        path : "/recipe",
        component : Recipe
    },
    {
        name : "Community",
        path : "/community",
        component : Community
    },
    {
        name : "Logout",
        path : "/logout",
        component : Logout
    },
    {
        name : "Create_Recipe",
        path : "/create_recipe",
        component : Create_Recipe
    },
    {
        name : "My_Recipe",
        path : "/my_recipe",
        component : My_recipes
    }
   
]

const router = createRouter({
    history : createWebHistory(),
    routes
});

export default router