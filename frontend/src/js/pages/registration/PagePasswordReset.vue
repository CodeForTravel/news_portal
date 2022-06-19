<template>
  <section class="section">
    <div class="section-body">
      <b-row>
        <b-col cols="12" md="8" offset-md="2" lg="6" offset-lg="3">
          <form-password-reset></form-password-reset>
        </b-col>
      </b-row>
    </div>
  </section>
</template>

<script>
const FormPasswordReset = () =>
  import("../../components/registration/FormPasswordReset.vue");
export default {
  components: {
    FormPasswordReset,
  },
};
</script>

<style></style>
