<template>
  <Nav/>
 
  <HelloWorld msg="Welcome to Your Vue.js App"/>

  <Login/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

import Nav from './components/Nav.vue'

import Login from './components/Login.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Nav,
    Login
  }
}
</script>

<style>


</style>
