<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title> QVantel Test </q-toolbar-title>

        <q-btn-dropdown color="default" flat icon="fas fa-user">
      <q-list flat>
        <q-item clickable flat v-close-popup @click="logout">
          <q-item-section>
            <q-item-label>Logout</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header>Navigation </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>

      <q-list v-if="isSuperUser()">
        <q-item-label header>Administration </q-item-label>

        <EssentialLink
          v-for="link in administrationLinks"
          :key="link.title"
          target="_blank"
          v-bind="link"
        />
      </q-list>

    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import ShopService from 'src/api/shop_service'
const shopService = new ShopService()

import { defineComponent, ref } from "vue";
import EssentialLink from "components/EssentialLink.vue";
import projectComposables from "src/api/composables";

const linksList = [
  {
    title: "Shop",
    caption: "shop",
    icon: "school",
    to: "shop",
  },
  {
    title: "My Cart",
    caption: "my cart",
    icon: "school",
    to: "cart",
  },
];

const administrationLinks = [
  {
    title: "Administration",
    caption: "administration",
    icon: "school",
    to: "/admin/",
  },
]

export default defineComponent({
  name: "MainLayout",

  components: {
    EssentialLink,
  },
  methods: {
    logout() {
      shopService.logout().then((ok)=>{
        this.$router.push({name: 'login'})
      })
    }

  },
  setup() {
    const leftDrawerOpen = ref(false);
    const {isSuperUser} = projectComposables()
    return {
      essentialLinks: linksList,
      administrationLinks: administrationLinks,
      leftDrawerOpen,
      isSuperUser,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
});
</script>
