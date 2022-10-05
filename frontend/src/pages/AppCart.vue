<template>
  <div>
    <h1>Total: {{ data.price }} {{ data.price_currency }}</h1>
    <q-table :rows="data.items" :columns="columns" row-key="id">
      <template v-slot:body="props">
        <q-tr>
          <q-td class="text-right" key="name" :props="props">{{
            props.row.item.name
          }}</q-td>
          <q-td class="text-right" key="item_price" :props="props"
            >{{ props.row.price }} {{ props.row.price_currency }}</q-td
          >
          <q-td class="text-right" key="qty" :props="props">
            {{ parse(props.row.qty) }}
            <q-popup-edit buttons v-model="props.row.qty" v-slot="scope">
              <q-input
                step="1"
                min="0"
                type="number"
                v-model="scope.value"
                dense
                autofocus
                counter
                @keyup.enter="updateCart(scope, props.row.item)"
              />
            </q-popup-edit>
          </q-td>
        </q-tr>
      </template>
    </q-table>
  </div>
</template>

<script>
import ShopService from "src/api/shop_service";
const shopService = new ShopService();

export default {
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
        { name: "qty", label: "Item quantity", field: "qty", sortable: true },
      ],
    };
  },
  mounted() {
    shopService.getCart().then((resp) => {
      this.data = resp.data;
    });
  },
  methods: {
    parse(qty) {
      if (qty) {
        return parseFloat(qty).toFixed(2).replace(".", ",");
      }
      return qty;
    },
    updateCart(scope, item) {
      var value = parseFloat(scope.value).toFixed(2);
      //item.qty = value
      scope.value = value;
      scope.set();
      shopService.updateCart(item.id, value).then((resp) => {
        this.data = resp.data;
      });
    },
  },
};
</script>
