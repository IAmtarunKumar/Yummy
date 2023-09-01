import {createWebHistory , createRouter} from 'vue-router'

// import Home from './components/Home.vue'



import Login from './components/Login.vue';
import SignIn from './components/Sign.vue'


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
    }
   
]

const router = createRouter({
    history : createWebHistory(),
    routes
});

export default router