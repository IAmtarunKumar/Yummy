<template>
  <div id="loginDiv">
    <form @submit.prevent="registerUser">
      <h3>Login Here</h3>

      <label for="username">Username</label>
      <input
        type="text"
        placeholder="Email or Phone"
        id="username"
        v-model="username"
      />

      <label for="password">Password</label>
      <input
        type="password"
        placeholder="Password"
        id="password"
        v-model="password"
      />

      <button>Log In</button>
      <div class="social">
        <div class="go"><i class="fab fa-google"></i> Google</div>
        <div class="fb"><i class="fab fa-facebook"></i> Facebook</div>
      </div>
      <br />
      <!-- <a style="text-decoration: none; color:rgb(18, 110, 147)" href="">I am already member</a> -->
      <router-link to="/sign">I am new user</router-link>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import Swal from "sweetalert2";
export default {
  name: "LoginPage",

  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    registerUser() {
      // Create an object with the user data
      const userData = {
        username: this.username,
        password: this.password,
      };

      axios
        .post("http://localhost:8000/login/", userData)
        .then((response) => {
          console.log("User Login successfully:", response.data);
          let token_user = {
            token: response.data.token,
            username: response.data.username,
          };
          if (response.data.message == "Login successful") {
            localStorage.setItem("data", JSON.stringify(token_user));
            Swal.fire({
              position: "center",
              icon: "success",
              title: "Login Successfully ",
              showConfirmButton: false,
              timer: 1500,
            });
            this.$router.push("/");
          } else {
            alert("Something Went Wrong");
            alert("Please Sign in first");
          }

          // You can handle the response as needed
        })
        .catch((error) => {
          console.error("Error Login user:", error);
          alert("Please Sign in first");
        });
    },
  },
};
</script>

<style scoped>
#loginDiv {
  width: 100%;
  height: 91vh;
  background: url(https://img.freepik.com/free-photo/colorful-veggies-frame-with-copy-space_23-2148290738.jpg?w=1060&t=st=1693564595~exp=1693565195~hmac=d00314a1618f55bdcd6968fbfc131b5d05f46e7157ef94739f28964e9168b51a);

  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: center center;
}

form {
  height: 550px;
  width: 400px;
  background-color: rgba(21, 157, 62, 0.664);
  position: absolute;
  transform: translate(-50%, -50%);
  top: 50%;
  left: 50%;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border: 2px solid rgba(58, 237, 114, 0.1);
  box-shadow: 0 0 40px rgba(6, 54, 32, 0.6);
  padding: 50px 35px;
}

form * {
  font-family: "Poppins", sans-serif;
  color: #0c2b19;
  letter-spacing: 0.5px;
  outline: none;
  border: none;
}

form h3 {
  font-size: 32px;
  font-weight: 501;
  line-height: 42px;
  text-align: center;
}

label {
  display: block;
  margin-top: 30px;
  font-size: 16px;
  font-weight: 501;
}

input {
  display: block;
  height: 50px;
  width: 100%;
  background-color: rgba(227, 234, 229, 0.712);
  border-radius: 3px;
  padding: 0 10px;
  margin-top: 2px;
  font-size: 14px;
  font-weight: 300;
}

::placeholder {
  color: #9eb4a6;
}

button {
  margin-top: 50px;
  width: 100%;
  background-color: #071207;
  color: #efeef5;
  padding: 15px 0;
  font-size: 18px;
  font-weight: 600;
  border-radius: 5px;
  cursor: pointer;
}

.social {
  margin-top: 30px;
  display: flex;
}

.social div {
  background: red;
  width: 150px;
  border-radius: 3px;
  padding: 5px 10px 10px 5px;
  background-color: rgba(255, 255, 255, 0.27);
  color: #eaf0fb;
  text-align: center;
}

.social div:hover {
  background-color: rgba(255, 255, 255, 0.47);
}

.social .fb {
  margin-left: 25px;
}

.social i {
  margin-right: 4px;
}
</style>
