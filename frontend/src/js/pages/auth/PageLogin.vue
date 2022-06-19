<template>
  <section class="section mt-4">
    <div class="section-body">
      <b-row>
        <b-col cols="12" class="text-center">
          <div class="login-brand">
            <!-- <img src="/static/img/news_portal.png" alt="logo" /> -->
            <h5 class="my-4">
              NEWS PORTAL
            </h5>
          </div>
        </b-col>
        <b-col
          cols="12"
         xl="4"
         lg="6"
         class="mx-auto"

        >
          <form-login></form-login>
        </b-col>
      </b-row>
    </div>
  </section>
</template>

<script>
const FormLogin = () => import("../../components/user/auth/FormLogin.vue");

export default {
  components: {
    FormLogin,
  },
};
</script>

<style></style>
