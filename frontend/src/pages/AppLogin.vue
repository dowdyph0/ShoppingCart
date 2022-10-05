<template>
  <div class="column q-pa-lg">
    <div class="row">
      <q-card square class="shadow-24" style="width: 400px; height: 540px">
        <q-form class="q-px-sm q-pt-xl" @submit.prevent="login">
          <q-card-section class="bg-deep-purple-7">
            <h4 class="text-h5 text-white q-my-md">QVantelTest Login</h4>
          </q-card-section>
          <q-card-section>
            <q-input
              ref="username"
              square
              v-model="username"
              lazy-rules
              :rules="[this.required, this.short]"
              type="username"
              label="Username"
            >
              <template v-slot:prepend>
                <q-icon name="person" />
              </template>
            </q-input>
            <q-input
              ref="password"
              square
              v-model="password"
              type="password"
              lazy-rules
              :rules="[this.required, this.short]"
              label="Password"
            >
              <template v-slot:prepend>
                <q-icon name="lock" />
              </template>
            </q-input>
          </q-card-section>

          <q-card-actions class="q-px-lg">
            <q-btn
              type="submit"
              unelevated
              size="lg"
              color="secondary"
              class="full-width text-white"
              label="Submit"
            />
          </q-card-actions>
          <q-card-section class="text-center q-pa-sm">
            <p class="text-grey-6">Forgot password?</p>
          </q-card-section>
        </q-form>
      </q-card>
    </div>
  </div>
</template>

<script>
import ShopService from "src/api/shop_service";
const shopService = new ShopService();

export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login() {
      shopService.login(this.username, this.password).then((ok) => {
        console.log("login suceeded");
        this.$router.push({name: 'shop'})
      });
    },
    required(val) {
      return (val && val.length > 0) || "Field is required";
    },
    short(val) {
      return (val && val.length > 3) || "Entered text is too short";
    },
  },
};
</script>
