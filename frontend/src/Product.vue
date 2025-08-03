<template>
  <div class="product-card">
    <div class="prod_img">
        <div class="dummy_img">TV Image</div>
    </div>
    
    <div class="prod_info">
      <h3 class="title">{{ product.title }}</h3>
      

      <div class="cost">
          
          
          <div class="discount">
              <div class="dis-per">{{ product.discount_percentage }}</div>
              <div class="dis-val">
                  {{ ('₹' + calculateDiscount(product.price || product.sale_price, product.sale_price) + ' Off') || product.discount_value }}
                </div>
            </div>
            <div class="sale_price">{{ product.sale_price }}</div>
            <div class="old_price">{{ product.price || product.sale_price }}</div>
        </div>
    </div>
    <!-- Rating Part  Commented Out Since It can be scraped -->
    <!-- <div class="ratings"> -->
      <!-- <span class="rating-value">{{ product.rating }}</span> -->
      <!-- <span class="review-count">({{ product.review_count }})</span> -->
    <!-- </div> -->
  </div>
</template>

<script>
export default {
  props: {
    product: {
      type: Object,
      required: true
    }
  },
  methods: {
    calculateDiscount(originalPrice, salePrice) {
      if (!originalPrice || !salePrice) return '';
      
      // Extract numbers from price strings for calculation from product.price and product.sale_price
      const origNum = parseFloat(originalPrice.replace(/[^\d.]/g, ''));
      const saleNum = parseFloat(salePrice.replace(/[^\d.]/g, ''));

      if (isNaN(origNum) || isNaN(saleNum) || origNum <= 0) return '';
      
      const discount = Math.round(origNum - saleNum);
      return discount;
    }
  }
}
</script>

<style scoped>
.product-card {
  background-color: #222;
  border-radius: 8px;
  overflow: hidden;
  position: relative;
  padding: 15px;
  display: flex;
  flex-direction: column;
}

.prod_img {
  height: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 15px;
  background-color: #222;
}

.dummy_img {
  color: #999;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  font-size: 14px;
  background-color: #333;
}

.prod_info {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.title {
  font-size: 16px;
  font-weight: 500;
  color: #fff;
  line-height: 1.4;
  min-height: 45px;
}


.cost {
    margin: 10px 0;
}

.sale_price {
    font-size: 22px;
    font-weight: bold;
    color: #fff;
}

.discount {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 5px;
}

.old_price {
    font-size: 16px;
    color: #999;
    text-decoration: line-through;
}

.dis-per {
    color: #fff;
    background-color: #e41d36;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 12px;
    font-weight: bold;
}
/* .ratings {
  display: flex;
  align-items: center;
  gap: 5px;
}

.rating-value {
  font-weight: bold;
  color: #fff;
}

.review-count {
  color: #999;
  font-size: 12px;
} */
</style>