<template>
  <div>
    <h1>Shop</h1>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card class="my-card" v-for="(item, idx) in items" :key="idx">
      <q-img :src="item.image_url">
        <div class="absolute-bottom">
          <div class="text-h6">{{ item.name }}</div>
          <div class="text-subtitle2">
            {{ item.price }} {{ item.price_currency }}
          </div>
        </div>
      </q-img>

      <q-card-actions>
        <q-btn flat icon="fas fa-plus" @click="addToCart(item)">Add to cart</q-btn>
      </q-card-actions>
    </q-card>
    </div>
  </div>
</template>

<script>
import ShopService from 'src/api/shop_service'
const shopService = new ShopService()

export default {
  data() {
    return {
      items: [],
    };
  },
  methods: {
    addToCart(item) {
        console.info("addToCart", item)
    },
  },
  mounted() {
    console.log(shopService)
    shopService.getItemList().then((resp) => {
      this.items = resp.data.results
    })
  },
};
</script>


<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 250px
</style>
