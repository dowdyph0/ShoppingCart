import { boot } from "quasar/wrappers";
import { Notify } from "quasar";
import { Loading } from "quasar";
import axios from "axios";
import { LocalStorage } from "quasar";
import projectComposables from "src/api/composables"
import ShopService from "src/api/shop_service";

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)
let protocol = document.location.protocol
let host = document.location.hostname
let port = document.location.port
// port = 8000

let baseUrl = `${protocol}//${host}:${port}/api/`

const api = axios.create({ baseURL: baseUrl });
const shopService = new ShopService()

export default boot(({ app, router, store }) => {
  const { access, refresh } = projectComposables()
  api.interceptors.request.use(
    async (config) => {
      if (access.value) {
        config.headers.Authorization = `Bearer ${access.value}`;
      }
      return config;
    },
    (error) => {
      Promise.reject(error);
    }
  );

  api.interceptors.response.use(
    async function (resp) {
      // guardamos request original
      const originalRequest = resp.config;

      // if errors and refresh failed and token not valid -> logout
      if (
        resp.config.url == "/auth/token/refresh/" &&
        resp.data.code == "token_not_valid"
      ) {

        shopService.logout().then(() => {
          Notify.create({
            message: 'Session expired',
            type: "info",
          });
          router.push({ name: "login" });
        })
      }

      // with errors and token_not_valid we refresh it
      else if (resp.data.code == "token_not_valid") {
        shopService.refreshToken().then((ok) => {
          if (ok) {
            originalRequest.headers.Authorization = `Bearer ${access.value}`;
            return axios(originalRequest);
          }
        })
      }

      // if normal response comes with errors
      else if (resp.data.errors && resp.status == 200) {
        Loading.hide();
        Notify.create({
          message: `<p>Error: ${resp.data.errors}</p>`,
          type: "negative",
          timeout: 0,
          html: true,
          actions: [
            {
              label: "Cerrar",
              color: "white",
              handler: () => {
                /* ... */
              },
            },
          ],
        });
      }

      // in another case we use normal response
      else {
        Loading.hide();
        return resp;
      }
    },

    async function (error) {

      var originalRequest = error.response.config

      if (originalRequest.url == "/auth/token/refresh/" && error.response.data.code == "token_not_valid") {
        shopService.logout().then(() => {
          Notify.create({
            message: 'Session expired',
            type: "info",
          });
          router.push({ name: "login" });
        })
      }

      if (error.response.data.code == "token_not_valid") {
        shopService.refreshToken().then((ok) => {
          if (ok) {
            originalRequest.headers.Authorization = `Bearer ${access.value}`;
            return axios(originalRequest);
          }
        })
      }

      Loading.hide();
      // if there is any error we show it 
      var html_errors = "Error during request.";
      if (error.response && error.response.data && error.response.data.errors) {
        html_errors = error.response.data.errors.join("<br>");
      }

      Notify.create({
        message: `<p>${html_errors}</p>`,
        type: "negative",
        timeout: 0,
        html: true,
        actions: [
          {
            label: "Cerrar",
            color: "white",
            handler: () => {
              /* ... */
            },
          },
        ],
      });
      router.push({ name: "login" });
      return Promise.reject(error);
    }
  );

  app.config.globalProperties.$axios = axios;
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$api = api;
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
});

export { api };
