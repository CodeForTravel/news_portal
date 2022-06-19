<template>
  <div class="my-4 container">
    <b-card no-body>
      <b-tabs pills card vertical>
        <b-tab title="User Info" active
          ><b-card-text>
            <change-user-profile-form></change-user-profile-form> </b-card-text
        ></b-tab>
        <b-tab title="Change Password"
          ><b-card-text>
            <form-change-password></form-change-password> </b-card-text
        ></b-tab>
        <b-tab title="Settings">
          <b-card-text> <news-feed-settings></news-feed-settings> </b-card-text
        ></b-tab>
      </b-tabs>
    </b-card>
  </div>
</template>

<script>
const FormChangePassword = () =>
  import("../components/user/profile/FormChangePassword.vue");
const ChangeUserProfileForm = () =>
  import("../components/user/profile/ChangeUserProfileForm.vue");
const NewsFeedSettings = () =>
  import("../components/user/profile/NewsFeedSettings.vue");

export default {
  components: {
    ChangeUserProfileForm,
    FormChangePassword,
    NewsFeedSettings,
  },
};
</script>

<style></style>
