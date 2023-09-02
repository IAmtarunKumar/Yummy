<template>
    <div id="loginDiv">

        <form @submit.prevent="registerUser">
            <h3>Sign In Here</h3>
            <label for="name">Username</label>
            <input type="text" placeholder="Enter Your Name" id="username" v-model="username" required>

            <label for="email">Email</label>
            <input type="email" placeholder="Email or Phone" id="email" v-model="email" required>

            <label for="password">Password</label>
            <input type="password" placeholder="Password" id="password" v-model="password" required>

            <button>Sign In</button>
            <div class="social">
                <div class="go"><i class="fab fa-google"></i> Google</div>
                <div class="fb"><i class="fab fa-facebook"></i> Facebook</div>
            </div>
            <br>
            <!-- <a style="text-decoration: none; color:rgb(18, 110, 147)" href="">I am already member</a> -->
            <router-link to="/login">I am already member</router-link>
        </form>

    </div>
</template>
     
     
<script>


import axios from 'axios';
export default {
    name: "SignInPage",

    data() {
        return {
            username: '',
            email: '',
            password: '',
        };
    },
    methods: {
        registerUser() {
            // Create an object with the user data
            const userData = {
                username: this.username,
                email: this.email,
                password: this.password,
            };

            axios.post('http://localhost:8000/register/', userData)
                .then((response) => {
                    console.log('User registered successfully:', response.data);
                    alert("Successfully")
                    // You can handle the response as needed
                })
                .catch((error) => {
                    console.error('Error registering user:', error);
                });
        }
    }
}


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

    height: 590px;
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
    margin-top: 10px;
}

form * {
    font-family: 'Poppins', sans-serif;
    color: #0c2b19;
    letter-spacing: 0.5px;
    outline: none;
    border: none;
}

form h3 {
    font-size: 32px;
    font-weight: 500;
    line-height: 42px;
    text-align: center;
}

label {
    display: block;
    margin-top: 8px;
    font-size: 16px;
    font-weight: 500;
}

input {
    display: block;
    height: 50px;
    width: 100%;
    background-color: rgba(227, 234, 229, 0.712);
    border-radius: 3px;
    padding: 0 10px;
    margin-top: 4px;
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