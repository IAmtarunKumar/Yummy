<template>
  <hr>
  <h1 style="background-color: rgba(57, 218, 25, 0.344); padding: 10px">
    <Center>Community Form</Center>
  </h1>
  <hr />
  <form @submit.prevent="registerUser">
    <div id="search">
      <textarea
        name=""
        id=""
        cols="30"
        rows="10"
        placeholder="Connect with your community members"
        v-model="description"
      ></textarea>
      <br />
      <button id="search_btn">submit</button>
    </div>
  </form>

  <div class="community-data">
    <div id="mainCommment">
      <div id="comment" v-for="(item, index) in communityData" :key="index">
        <pre>{{ item.description }}</pre>
        <a id="like" href="">Like</a>
        <a id="reply" href="">Reply</a>
      </div>
    </div>
  </div>

  <br /><br />
</template>

<script>
import axios from "axios";
import Swal from 'sweetalert2';
export default {
  name: "CommunityPage",

  data() {
    return {
      description: "",
      communityData: "",
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
      let token = localStorage_data["token"]
    //   console.log(token)
    

      // Set up the axios headers to include the token
    const axiosConfig = {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };

      axios
        .post("http://localhost:8000/com/", userData , axiosConfig)
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
        .get("http://localhost:8000/community/show/")
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
#search {
  widows: 80%;
  margin-left: 10%;
  margin-right: 10%;
}

#search > textarea {
  width: 100%;
  height: 200px;
  border: 2px solid rgb(5, 62, 16);
  border-radius: 10px;
  padding: 20px;
}

#search_btn {
  margin-left: 88%;
  font-size: 20px;
  padding: 5px 40px;
  border: none;
  background-color: rgb(12, 41, 12);
  border-radius: 10px;
  color: white;
  font-weight: bold;
}

#comment {
  width: 80%;
  margin: 20px 10%;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  border: 2px solid rgba(128, 128, 128, 0.605);
  padding: 20px 0px 20px 20px;
  border-radius: 10px;
  /* Adjust the width as needed */
}

#reply {
  text-decoration: none;

  border: none;
  padding: 5px 10px;
  background-color: rgb(44, 93, 157);
  color: white;
  border-radius: 5px;
}

#like {
  text-decoration: none;
  margin-left: 88%;
  margin-right: 1%;
  border: none;
  padding: 5px 10px;
  background-color: rgb(44, 93, 157);
  color: white;
  border-radius: 5px;
}
</style>
