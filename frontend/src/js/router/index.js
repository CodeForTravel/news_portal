import Vue from 'vue'
import Router from 'vue-router'

const PageUserProfile = () => import("../pages/PageUserProfile.vue");
const PageLogin =()=> import("../pages/auth/PageLogin.vue")
const PagePasswordReset =()=> import("../pages/registration/PagePasswordReset.vue")
const PagePasswordResetDone =()=> import("../pages/registration/PagePasswordResetDone.vue")
const PagePasswordResetComplete =()=> import("../pages/registration/PagePasswordResetComplete.vue")
const PagePasswordResetConfirm =()=> import("../pages/registration/PagePasswordResetConfirm.vue")
const HomePage =()=> import("../components/base/HomePage.vue")

Vue.use(Router)

const routes = [
  {
    path: "",
    name: "home",
    component: HomePage,
    props: true,
    meta: { title: "Home | News Portal", navBarTitle: "HOME" },
  },

  {
    path: "/user/profile/",
    name: "profile",
    component: PageUserProfile,
    props: true,
    meta: { title: "Profile | News Portal", navBarTitle: "PROFILE" },
  },

  {
    path: "/login/",
    name: "login",
    component: PageLogin,
    props: true,
    meta: { title: "LOGIN | News Portal", navBarTitle: "LOGIN" },
  },

  {
    path: "/account/password_reset",
    name: "password-reset",
    component: PagePasswordReset,
    props: true,
    meta: {
      title: "Password Reset | News Portal",
      navBarTitle: "Password Reset",
    },
  },
  {
    path: "/account/password_reset/done/",
    name: "password-reset-done",
    component: PagePasswordResetDone,
    meta: {
      title: "Password Reset Done | News Portal",
    },
  },
  {
    path: "/account/reset/done/",
    name: "password-reset-complete",
    component: PagePasswordResetComplete,
    meta: {
      title: "Password Reset Complete | News Portal",
    },
  },
  {
    path: "/account/reset/:token/confirm",
    name: "password-reset-confirm",
    component: PagePasswordResetConfirm,
    props: true,
    meta: {
      title: "Password Reset Confirm | News Portal",
    },
  },
]

const router = new Router({
  mode: 'history',
  routes
})

export default router
