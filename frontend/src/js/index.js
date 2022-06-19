import Vue from "vue";
import Select2 from "v-select2-component";
import Toasted from "vue-toasted";
import i18n from "../i18n.js";
import * as filters from "../filters.js";
import store from "./store";
import router from "./router";
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


const NavBar =()=> import("./components/base/NavBar.vue")

Vue.component("Select2", Select2);
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

window.Vue = Vue;

Vue.use(Toasted, {
  class: "rounded",
  position: "bottom-right",
  fitToScreen: true,
  theme: "toasted-primary",
  duration: 4000,
});

const app = new Vue({
  el: "#app",
  i18n,
  router,
  store,
  components: {
    NavBar  
  },
});
