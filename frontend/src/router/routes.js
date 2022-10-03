
const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import('pages/AppLogin.vue'),
  },

  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/shop', name: 'shop', component: () => import('pages/AppShop.vue') },
      {
        path: '/cart',
        name: 'cart',
        component: () => import('pages/AppCart.vue'),
      },
      {
        path: '/administration',
        name: 'administration',
        component: () => import('pages/AppAdministration.vue'),
      },
    ]
  },


  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
