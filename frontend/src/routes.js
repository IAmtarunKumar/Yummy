import {createWebHistory , createRouter} from 'vue-router'

// import Home from './components/Home.vue'



import Login from './components/Login.vue';
import SignIn from './components/Sign.vue'
import Home from './components/home.vue'
import Recipe from './components/Recipe.vue'
import Community from './components/community.vue'

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
    }
   
]

const router = createRouter({
    history : createWebHistory(),
    routes
});

export default router