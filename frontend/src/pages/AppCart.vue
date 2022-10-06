<template>
  <div>
    <h1>Total: {{ data.price }} {{ data.price_currency }}</h1>
    <q-table :rows="data.cart_items" :columns="columns" row-key="id">
      <template v-slot:body="props">
        <q-tr>
          <q-td class="text-right" key="name" :props="props">{{
            props.row.item.name
          }}</q-td>
          <q-td class="text-right" key="item_price" :props="props"
            >{{ props.row.price }} {{ props.row.price_currency }}</q-td
          >
          <q-td class="text-right" key="quantity" :props="props">
            {{ parse(props.row.quantity) }}
            <q-popup-edit buttons v-model="props.row.quantity" v-slot="scope">
              <q-input
                step="1"
                min="0"
                type="number"
                v-model="scope.value"
                dense
                autofocus
                counter
                @keyup.enter="scope.set"
              />
            </q-popup-edit>
          </q-td>
        </q-tr>
      </template>
    </q-table>
    <q-btn color="primary" icon="check" label="Checkout Cart" @click="checkoutCart" />
  </div>
</template>

<script>
import ShopService from "src/api/shop_service";
import projectComposables from "src/api/composables"
const shopService = new ShopService();

export default {
  setup() {
    const {getCartID} = projectComposables()
    return {getCartID}
  },
  data() {
    return {
      data: {
        price: 0.0,
        price_currency: "USD",
        items: [],
      },
      columns: [
        {
          name: "name",
          required: true,
          label: "Name",
          align: "right",
          field: "item",
          format: (val) => {
            return val.name;
          },
          sortable: true,
        },
        {
          name: "item_price",
          align: "right",
          label: "Price",
          field: "price",
          sortable: true,
        },
        { name: "quantity", label: "Item quantity", field: "quantity", sortable: true },
      ],
    };
  },
  mounted() {
    var cartID = this.getCartID()
    this.loadCartData(cartID)
  },
  methods: {
    parse(quantity) {
      if (quantity) {
        return parseFloat(quantity).toFixed(2).replace(".", ",");
      }
      return quantity;
    },
    
    loadCartData(cartID) {
      shopService.getCart(cartID).then((resp) => {
        this.data = resp.data;
      });
    },
    
    checkoutCart() {
      var cart_items = []
      for (var cart_item of this.data.cart_items) {
        cart_items.push({
          item_id: cart_item.item.id,
          quantity: cart_item.quantity,
        })
      }

      shopService.checkoutCart('US', cart_items).then((resp) => {
        this.loadCartData(resp.data.id)
      })
    },

    updateCart(newVal, cart_item) {
      var cartID = this.getCartID()
      var value = parseFloat(newVal).toFixed(2);
      shopService.updateCart(cartID, cart_item.id, value).then((resp) => {
        this.data = resp.data;
      });
    },
  },
};
</script>
