<template>
  <div id="footerDiv">
    <div class="container-footer">
      <div class="footer-column">
        <a href="">
        <img
          src="https://uploads-ssl.webflow.com/5966ea9a9217ca534caf139f/596d33f36607b12cfdaf8ad2_LogoWhite.png"
          alt=""
          width="40"
          class="failory-logo-image"
        /></a>
        <h3 class="footer-failory-name">Yummy</h3>
        <p class="footer-description-failory">For Better Diets! Yummy</p>
      </div>
      <div class="footer-column">
        <h3 class="footer-titles">About Yummy</h3>
        <p class="footer-links">
          <a class="footer_a" href="" target="_blank"><span class="footer-link">Yummy Startups</span></a><br>
          <a class="footer_a" href=""><span class="footer-link">Our Branches</span></a><br>
          <a class="footer_a" href=""><span class="footer-link">Blog</span></a><br>
          <a class="footer_a" href=""><span class="footer-link">Entrepreneurial Tools</span></a><br>
          <a class="footer_a" href=""><span class="footer-link">Projects</span></a><br>
         
        </p>
      </div>
      <div class="footer-column">
        <h3 class="footer-titles">Other</h3>
        <p class="footer-links">
          <a class="footer_a"  href=""><span class="footer-link">Sponsor Us!</span></a><br>
          <a class="footer_a" href=""><span class="footer-link">Open Startup</span></a><br>
          <a class="footer_a" href=""><span class="footer-link">Contribute</span></a><br>
          <a class="footer_a" href=""><span class="footer-link">FAQ</span></a><br>
        </p>
      </div>
      <div class="footer-column">
        <h3 class="footer-titles">Follow Us!</h3>
        <div class="footer-social-icons">
          <a href="" target="_blank" class="footer-social-icon">
            <img src="https://uploads-ssl.webflow.com/5966ea9a9217ca534caf139f/5c8dbf0a2f2b67e3b3ba079c_Twitter%20Icon.svg" width="20" alt="Twitter icon">
          </a>
          <a href="" target="_blank" class="footer-social-icon">
            <img src="https://uploads-ssl.webflow.com/5966ea9a9217ca534caf139f/5c8dbfe70fcf5a0514c5b1da_Instagram%20Icon.svg" width="20" alt="Instagram icon">
          </a>
          <a href="" target="_blank" class="footer-social-icon">
            <img src="https://uploads-ssl.webflow.com/5966ea9a9217ca534caf139f/5c8dbe42e1e6034fdaba46f6_Facebook%20Icon.svg" width="20" alt="Facebook Icon">
          </a>
          <a href="" target="_blank" class="footer-social-icon">
            <img src="https://uploads-ssl.webflow.com/5966ea9a9217ca534caf139f/5c8dc0002f2b676eb4ba0869_LinkedIn%20Icon.svg" width="20" alt="LinkedIn Icon">
          </a>
          <a href="" target="_blank" class="footer-social-icon">
            <img src="https://uploads-ssl.webflow.com/5966ea9a9217ca534caf139f/5c8dc0112f2b6739c9ba0871_Pinterest%20Icon.svg" width="20" alt="Pinterest Icon">
          </a>
        </div>
        <p class="footer-description">
          Email me at: <a style="text-decoration: none; color:white" href=""><strong class="link-email-footer">yummy@gmail.com</strong></a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "footerPage"
};
</script>

<style scoped>
#footerDiv {
  background-color: rgb(9, 43, 9);
  color: white;
  padding: 40px 0;
}

.container-footer {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-gap: 20px;
  max-width: 940px;
  margin: 0 auto;
  justify-items: center;
  text-align: center;
}

.failory-logo-image {
  max-width: 100%;
}

.footer-column {
  width: 100%;
}
.footer_a{
  text-decoration: none;
 

}
.footer-failory-name {
  font-size: 20px;
  font-weight: 900;
  margin: 15px 0;
}

.footer-description-failory {
  font-size: 17px;
  font-weight: 300;
  color: rgba(255, 255, 255, 0.8);
  margin: 0;
}

.footer-titles {
  font-size: 20px;
  font-weight: 900;
  margin: 15px 0;
}

.footer-links {
  font-size: 17px;
  font-weight: 300;
  color: rgba(255, 255, 255, 0.8);
  margin: 0;
}

.footer-link {
  color: rgba(255, 255, 255, 0.8);
  font-weight: 300;
  text-decoration: none;
}

.footer-link:hover {
  color: white;
  font-weight: 400;
}

.footer-social-icons {
  display: flex;
  justify-content: center;
  margin: 10px 0;
}

.footer-social-icon {
  margin: 0 5px;
}

.link-email-footer {
  font-weight: 700;
}
</style>
