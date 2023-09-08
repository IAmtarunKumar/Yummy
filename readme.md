
  
  <h1><center> <img
          src="https://uploads-ssl.webflow.com/5966ea9a9217ca534caf139f/596d33f36607b12cfdaf8ad2_LogoWhite.png"
          alt=""
          width="40"
          class="failory-logo-image"
        />    Yummy.com </center></h1>

  <p><center>  - Your Personalized Recipe Recommendation Platform</center></p>
  
  ## Introduction
  
  Welcome to Yummy.com, your ultimate destination for personalized recipe recommendations, culinary inspiration, and vibrant community engagement. Whether you're an experienced chef or just embarking on your culinary adventure, Yummy.com is designed to make cooking a delightful and stress-free experience for everyone.
  
  At Yummy.com, we harness state-of-the-art technologies to provide you with tailored recipe suggestions, precisely matched to your unique tastes and dietary preferences. Our platform combines the power of Vue.js for the frontend, Django for the backend, and MongoDB for robust data storage. What sets us apart is our integration of cutting-edge machine learning algorithms that analyze your preferences, ensuring the most accurate recipe recommendations.
  
  With Yummy.com, you can effortlessly discover, save, and share recipes, curate your personalized recipe collections, rate dishes, and provide invaluable feedback. Dive into our passionate community of food enthusiasts, share your culinary creations, and contribute your cooking wisdom. Yummy.com is more than just a recipe platform; it's a place to connect with like-minded individuals who share your passion for food.
  
  ## Deployed App
  
  - <b>Backend</b>: [https://backend.yummy.com](https://django-chack.onrender.com)
  - <b>Frontend</b>: [https://frontend.yummy.com](https://frontend.yummy.com)
  
  ## Video Walkthrough
  
  [Link to Video Walkthrough]
  
  ## Features
  
  Discover the exciting features that Yummy.com offers:
  
  - **Personalized Recipe Recommendations:** Our machine learning algorithms analyze your taste preferences to suggest recipes you'll adore.
  - **Recipe Discovery & Collection:** Explore diverse recipes based on cuisines, dietary preferences, and ingredients. Save your cherished recipes for easy access.
  - **Community Interaction:** Connect with fellow food enthusiasts, share your culinary experiences, and engage in discussions about recipes within our lively community forum.
  - **Ingredient Substitutions:** Yummy.com suggests ingredient substitutions tailored to your preferences and dietary restrictions, making recipes highly adaptable.
  - **User Ratings & Reviews:** Share your opinions by rating and reviewing recipes you've tried, helping others make informed choices.
  - **Culinary Profiles:** Create detailed culinary profiles to refine the accuracy of your recipe recommendations.
  - **Recipe Sharing:** Spread the love for your favorite recipes with the community or via social media.
  - **User-Generated Content:** Contribute cooking tips, modifications, and variations to enhance the overall culinary experience.
  - **Machine Learning-driven Flavor Analysis:** Our natural language processing and machine learning algorithms extract flavor information from recipe descriptions, ensuring precise recommendations.
  
  ## Design Decisions and Assumptions
  
  We've made several design decisions and assumptions to craft Yummy.com into the platform you see today:
  
  - **Diverse User Base:** We anticipate that our users will come from diverse backgrounds with a wide range of dietary preferences and culinary expertise.
  - **User-Centric Design:** Every design choice we've made prioritizes user engagement, personalization, and an enjoyable overall user experience.
  - **Technology Stack:** Yummy.com relies on Vue.js for the frontend, Django for the backend, and MongoDB for data storage to ensure scalability and peak performance.
  
  ## Installation & Getting Started
  
  To embark on your Yummy.com journey, follow these simple steps:
  
  1. Clone the Yummy.com repository from [GitHub](https://github.com/IAmtarunKumar/Yummy.com).
  2. Navigate to the project directory.
  3. Install the necessary dependencies:
  
  
  
  ```bash
  npm install my-project
  cd my-project
  npm start
  ```
  
  ## Usage
  - **Sign in or create an account to personalize your recipe recommendations.
  - **Explore recipes based on your preferences or search for specific cuisines, ingredients, or dietary requirements.
  - **Save your favorite recipes to your collection for quick access.
  - **Rate and review recipes you've tried to help others discover great dishes.
  - **Share your culinary creations and tips with the Yummy community.
  - **Contribute ingredient substitutions, modifications, and variations to enhance the recipes.
  
  ```bash
  # Example
  ```
  
  Include screenshots as necessary.
  
  ## APIs Used
  Yummy relies on the following external APIs:
  
  Vue.js: A progressive JavaScript framework for building user interfaces.
  Django: A high-level Python web framework for back-end development.
  MongoDB: A NoSQL database used for efficient data storage.
  
  ## API Endpoints
  
  Here are some of the key API endpoints used in Yummy:

- \*\*POST /api/signin/: Register a new user.
  <br>
  <img src="./readme img/sign in.png" alt="">
- \*\*POST /api/login/: Log in as an existing user.
  <br>
  <img src="./readme img/login.png" alt="">

- \*\*POST /api/logout/: Log out from the application.
  <br>
  <img src="./readme img/logout.png" alt="">

- \*\*GET /api/get/community/: Get a list of communities.
- \*\*POST /api/post/community/: Create a new community.
  <br>
  <img src="./readme img/comunity.png" alt="">

- \*\*GET /api/get/my_recipe/: Retrieve your recipes.
- \*\*POST /api/post/my_recipe/: Create a new recipe.

- \*\*POST /api/search/dish/: Search for a dish using chatbot integration.
  <br>
  <img src="./readme img/home.png" alt="">

- \*\*POST /api/filtered/dish/: Get custom recipes based on specific criteria.

## Technology Stack

Yummy utilizes a modern technology stack to provide a seamless user experience:

<b>Front-end</b>: Vue.js <br>
<b>Back-end</b>: Django <br>
<b>Database</b>: MongoDB <br>
