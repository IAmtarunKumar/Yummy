<template>
  <!-- Bootstrap Navbar -->
  <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #063006;">
    <div class="container">
      <!-- Brand/logo -->
      <a style="display: flex; justify-content:space-evenly; align-item:center; width:10% ; margin-left:30px" class="navbar-brand" href="#">
        <img
          src="https://uploads-ssl.webflow.com/5966ea9a9217ca534caf139f/596d33f36607b12cfdaf8ad2_LogoWhite.png"
          alt="Logo"
          width="40"
          class="failory-logo-image"
        />
        <span style="margin-top:16px ;"><h4 class="text-white">Yummy</h4></span>
      </a>

      <!-- Toggle button -->
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
        @click="toggleMenu"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Menu for larger screens -->
      <div class="collapse navbar-collapse" :class="{ show: isMenuActive }" id="navbarNav">
        <ul style="width: 60%; display:flex; justify-content:space-evenly; margin-left:50%; font-size:20px; color:white; font-weight:600"  class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="/">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/recipe">Recipe</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/Community">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/login">Login</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/logout">Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <!-- Bootstrap Navbar End -->
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      isMenuActive: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuActive = !this.isMenuActive;
    },
  },
};
</script>

<style scoped>
/* Your custom CSS styles here */
.nav-link{
  color: white;
}
</style>
