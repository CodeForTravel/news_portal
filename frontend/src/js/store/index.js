import Vue from "vue";
import Vuex from "vuex";

import * as user from "./user/user.js";
import * as registration from "./registration/registration.js";
import * as news from "./news/news.js";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    registration,
    news,
  },
});
