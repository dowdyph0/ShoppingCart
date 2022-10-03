<template>
  <div>
    <h1>My cart</h1>

    <q-table title="My cart" :data="data" :columns="columns" row-key="name" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: [],
      columns: [
        {
          name: "name",
          required: true,
          label: "Name",
          align: "left",
          field: (row) => row.name,
          format: (val) => `${val}`,
          sortable: true,
        },
        {
          name: "price",
          align: "center",
          label: "Price",
          field: "price",
          format: (val) => `${val.price} ${val.price_currency}`,
          sortable: true,
        },
        { name: "qty", label: "Item quantity", field: "qty", sortable: true },
      ],
    };
  },
  methods: {
    getCartData() {},
  },
};
</script>
