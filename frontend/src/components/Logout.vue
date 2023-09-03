<template>
    <div id="main">
        <img src="https://media.tenor.com/On7kvXhzml4AAAAi/loading-gif.gif" alt="">

    </div>
    <br>
    <h3>
        <Center> {{ msg="Logout is processing...." }} </Center>
    </h3>
    <br><br><br>
</template>


<script>
import axios from 'axios';
import Swal from 'sweetalert2';

export default {
    name: 'LogoutPage',

    mounted() {
        // Send a logout request to your server-side endpoint
        axios.post('http://localhost:8000/logout/') // Replace with your server's endpoint
            .then((response) => {
                console.log('User Logout successfully:', response.data);
                //   alert('Logout Successfully');
                // Redirect to the landing page

                setTimeout(() => {
                    Swal.fire({
                        position: 'center',
                        icon: 'success',
                        title: 'Logout Successfully ',
                        showConfirmButton: false,
                        timer: 1500
                    })
                    localStorage.removeItem("data");

                    this.$router.push('/');
                }, 1000);

            })
            .catch((error) => {
                console.error('Error Logout user:', error);
                alert("Something Went Wrong")
            });
    },
};
</script>


<style scoped>
#main {
    height: 400px;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
