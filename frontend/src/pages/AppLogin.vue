<template>
  <div class="column q-pa-lg">
    <div class="row">
      <q-card square class="shadow-24" style="width: 400px; height: 540px">
        <q-card-section class="bg-deep-purple-7">
          <h4 class="text-h5 text-white q-my-md">QVantelTest Login</h4>
        </q-card-section>
        <q-card-section>
          <q-form class="q-px-sm q-pt-xl">
            <q-input
              ref="username"
              square
              clearable
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
              clearable
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
          </q-form>
        </q-card-section>

        <q-card-actions class="q-px-lg">
          <q-btn
            unelevated
            size="lg"
            color="secondary"
            @click="login"
            class="full-width text-white"
            label="Submit"
          />
        </q-card-actions>
        <q-card-section class="text-center q-pa-sm">
          <p class="text-grey-6">Forgot password?</p>
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login() {
      console.info("login");
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
