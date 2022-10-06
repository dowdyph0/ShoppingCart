import { boot } from "quasar/wrappers";
import projectComposables from "src/api/composables";

const publicPages = ["login"];

export default boot(({ router, store }) => {
  router.beforeEach((to, from, next) => {
    const { access, isSuperUser } = projectComposables();
    const authRequired = !publicPages.includes(to.name);
    // si es obligatoria la autenticacion de usuario
    if (authRequired == true && access.value == null) {
      next({ name: "login" });
    } else if (to.name == "login" && access.value != null) {
      next({ name: "shop" });
    } else {
      next();
    }
  });
});