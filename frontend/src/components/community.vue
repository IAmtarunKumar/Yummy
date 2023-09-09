<template>
  <!-- nav start -->
  <div style="display: flex; justify-content:center">
    <div id="main">
      <h1>
        <Center>Community Form</Center>
      </h1>
      <form @submit.prevent="registerUser">
        <div id="search">
          <textarea name="" id="" cols="30" rows="10" placeholder="Connect with your community members"
            v-model="description"></textarea>
          <br />
          <button id="search_btn">Submit</button>
        </div>
      </form>

      <div class="community-data">
        <div id="mainCommment">
          <div id="comment" v-for="(item, index) in communityData" :key="index">
            <pre>{{ item.description }}</pre>
            <a class="action-button" href="#">Like</a>
            <a class="action-button" href="#">Reply</a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- nav end -->
</template>

<script>
import axios from "axios";
import Swal from 'sweetalert2';
export default {
  name: "CommunityPage",
  data() {
    return {
      description: "",
      communityData: [],
    };
  },
  mounted() {
    this.getCommunityData();
  },
  methods: {
    registerUser() {
      // Create an object with the user data
      const userData = {
        description: this.description,
      };

      let localStorage_data = JSON.parse(localStorage.getItem("data"))
      console.log(localStorage_data)
      // let token = localStorage_data["token"]
      //   console.log(token)


      // Set up the axios headers to include the token
      // const axiosConfig = {
      //   headers: {
      //     Authorization: `Bearer ${token}`,
      //   },
      // };

      axios
        .post("https://django-chack.onrender.com/community/post/", userData)
        .then((response) => {
          console.log("Posted successfully:", response.data);
          Swal.fire({
            position: 'center',
            icon: 'success',
            title: 'Posted Successfully ',
            showConfirmButton: false,
            timer: 1500
          })
          // You can handle the response as needed
        })
        .catch((error) => {
          console.error("Error something went wrong in posting:", error);
          Swal.fire({
            position: 'center',
            icon: 'failed',
            title: 'Something Went Wrong',
            showConfirmButton: false,
            timer: 1500
          })
        });
    },

    getCommunityData() {
      // Replace 'API_URL' with the actual URL of your API
      axios
        .get("https://django-chack.onrender.com/community/get/")
        .then((response) => {
          // Handle the API response here
          this.communityData = response.data; // Assign the API data to your variable
        })
        .catch((error) => {
          // Handle any errors that occur during the API request
          console.error("Error fetching data:", error);
        });
    },
  },
};
</script>

<style scoped>
#main {
  width: 80%;
  padding: 20px;
  text-align: left;


}

#search {
  width: 100%;
  margin: 0 auto;
  max-width: 1000px;
}

#search>textarea {
  width: 100%;
  border: 2px solid rgb(5, 62, 16);
  border-radius: 10px;
  padding: 20px;
}

#search_btn {
  display: block;
  margin: 10px auto;
  font-size: 20px;
  padding: 5px 20px;
  border: none;
  background-color: rgb(12, 41, 12);
  border-radius: 10px;
  color: white;
  font-weight: bold;
  cursor: pointer;
}

#comment {
  width: 100%;
  margin: 20px 0;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  border: 2px solid rgba(128, 128, 128, 0.605);
  padding: 20px;
  border-radius: 10px;
}

.action-button {
  text-decoration: none;
  display: inline-block;
  margin: 5px;
  padding: 5px 10px;
  background-color: rgb(44, 93, 157);
  color: white;
  border-radius: 5px;
}
</style>
