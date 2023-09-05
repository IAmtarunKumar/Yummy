<template>
  <!-- nav start -->
  <div id="main" :class="{ 'active': isMenuActive }">
    <div id="img">
      <img
        src="https://uploads-ssl.webflow.com/5966ea9a9217ca534caf139f/596d33f36607b12cfdaf8ad2_LogoWhite.png"
        alt="" width="40" class="failory-logo-image">
      <span>
        <h4>Yummy</h4>
      </span>
    </div>

    <!-- Toggle button -->
    <div id="toggle-button" @click="toggleMenu">
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
    </div>

    <div id="menu">
      <div><a href="/">Home</a></div>
      <div><a href="/recipe">Recipe</a></div>
      <div><a href="/Community">Community</a></div>
      <div><a href="/login">Login</a></div>
      <div><a href="/logout">Logout</a></div>
    </div>
  </div>
  <!-- nav end -->
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
    closeMenu() {
      this.isMenuActive = false;
    },
  },
};
</script>

<style scoped>
#main {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: rgb(9, 43, 9);
  color: white;
  padding: 10px 20px;
}

#img {
  display: flex;
  align-items: center;
}

#img>p {
  font-size: 30px;
  font-weight: bold;
  margin-left: 10px;
}

#menu {
  display: flex;
  align-items: center;
  font-size: 20px;
  font-family: Arial, Helvetica, sans-serif;
  list-style: none;
  padding: 0;
}

#menu>div {
  margin: 0 10px;
}

#menu>div>a {
  text-decoration: none;
  color: white;
  font-weight: 600;
}

#toggle-button {
  display: none;
  flex-direction: column;
  cursor: pointer;
}

.bar {
  width: 25px;
  height: 3px;
  background-color: white;
  margin: 3px 0;
  border-radius: 3px;
}

/* Media Query for small screens */
@media (max-width: 768px) {
  #menu {
    display: none;
    flex-direction: column;
    align-items: center;
    background-color: rgb(9, 43, 9);
    position: absolute;
    top: 60px;
    right: 0;
    left: 0;
    text-align: center;
  }

  #menu.active {
    display: flex;
  }

  #toggle-button {
    display: flex;
    z-index: 1;
  }
}
</style>
