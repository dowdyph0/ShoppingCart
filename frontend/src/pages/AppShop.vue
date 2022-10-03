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
    getItemList() {
      this.items = [
        {
          id: 1,
          name: "Katiuskas",
          price: 10.3,
          price_currency: "USD",
          image_url:
            "https://www.calzaditos.com/4120-thickbox_default/botas-de-agua-para-ninos-modelo-chufo-de-igor.jpg",
        },
        {
          id: 2,
          name: "Teletubbie",
          price: 35,
          price_currency: "USD",
          image_url:
            "https://images.ecestaticos.com/QhRv4Et-jrgPFrBLJLu_t1p47Os=/1x12:1023x587/1600x900/filters:fill(white):format(jpg)/f.elconfidencial.com%2Foriginal%2Fc6f%2Fc49%2F200%2Fc6fc49200334447aa6bd9850351b3d21.jpg",
        },
      ];
    },
  },
  mounted() {
    this.getItemList();
  },
};
</script>


<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 250px
</style>
