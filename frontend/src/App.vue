<template>
  <div class="app">
    <!-- Header -->
    <div class="app-header">
      <div class="header">
        <div class="logo">
          <img src="https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1637759004/Croma%20Assets/CMS/Category%20icon/Final%20icon/Croma_Logo_acrkvn.svg" alt="Croma" />
        </div>
      </div>
    </div>

    <div class="container">
      <h1 class="title">Televisions & Accessories</h1>
      
      <!-- Products card -->
      <div class="prod_grid">
        <Product 
          v-for="(product, index) in products" 
          :key="index" 
          :product="product" 
        />
      </div>
    </div>
  </div>  
</template>

<script>
import Product from './Product.vue';

export default {
  components: { Product},  
  data() {
    return {products: []} // products fetched from the backend
  },
  mounted() {
    const apiUrl = '/api/scraped-content'; //used /api endpoint to make it accessible to other devices on same network
                                            // used a simple proxy defined in vue.config.js 
    fetch(apiUrl)
      .then(res => res.json())
      .then(response => {
        if (response.data && response.data.products) {
          this.products = response.data.products;
        }
      });
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Roboto', 'Arial', sans-serif;
}

body {
  background-color: #111;
  color: #333;
  line-height: 1.5;
}

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #111;
  color: #fff;
}

.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 15px;
}

.app-header {
  background-color: #000;
  color: #fff;
  padding: 10px 0;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px 20px;
  max-width: 1280px;
  margin: 0 auto;
}

.logo img {
  height: 30px;
}

.title {
  font-size: 24px;
  font-weight: 600;
  margin: 20px 0;
  color: #fff;
}

/* Grid Layout */
.prod_grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 20px;
}

/* to make responsive */
@media (max-width: 1024px) {
  .prod_grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .header {
    flex-wrap: wrap;
  }
  
  .prod_grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .prod_grid {
    grid-template-columns: 1fr;
  }
}
</style>