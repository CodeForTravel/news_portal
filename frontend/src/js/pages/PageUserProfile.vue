<template>
  <div class="my-4">
    <b-row>
      <b-col cols="12" md="12" sm="12" lg="12" xl="6" class="mb-4">
        <change-user-profile-form></change-user-profile-form>
      </b-col>

      <b-col cols="12" md="12" sm="12" lg="12" xl="6">
        <form-change-password></form-change-password>
      </b-col>
    </b-row>
  </div>
</template>

<script>
const FormChangePassword =()=> import("../components/user/profile/FormChangePassword.vue")
const ChangeUserProfileForm =()=> import("../components/user/profile/ChangeUserProfileForm.vue")


export default {
  components: {
    ChangeUserProfileForm,
    FormChangePassword,
  },
};
</script>

<style></style>
