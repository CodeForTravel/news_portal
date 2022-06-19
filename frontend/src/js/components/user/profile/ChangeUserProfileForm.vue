<template>
  <div class="p-4">
    <h4>{{ $t("Update Profile") }}</h4>

    <div class="mt-4"></div>

    <b-form @submit.prevent="onFormSubmit">
      <b-form-group :label="$t('Name')">
        <b-form-input
          v-model="user_profile.name"
          type="text"
          placeholder="e.g. John Doe"
        >
        </b-form-input>
      </b-form-group>

      <b-form-group :label="$t('Email Address')">
        <b-form-input
          v-model="user_profile.email"
          type="email"
          placeholder="e.g. example@email.com"
        >
        </b-form-input>
      </b-form-group>

      <b-row class="mt-4">
        <b-col cols="12" class="text-right">
          <b-button type="submit" variant="outline-primary">
            <b>{{ $t("SAVE") }}</b>
          </b-button>
        </b-col>
      </b-row>
    </b-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userId: null,
      user_profile: {
        name: "",
        email: "",
      },
    };
  },
  components: {},

  created() {
    this.fetchUserInfo();
  },

  computed: {},

  methods: {
    fetchUserInfo() {
      this.$store.dispatch("user/getUserInfo").then((resp) => {
        if (resp.status == 200) {
          this.userId = resp.data.id;
          this.user_profile.name = resp.data.name;
          this.user_profile.email = resp.data.email;
        }
      });
    },

    onFormSubmit() {
      console.log("==============");

      if (["", null].includes(this.user_profile.email)) {
        Vue.toasted.show("You must fill up the email!", {
          className: "bg-danger",
        });
        return false;
      }

      this.$store
        .dispatch("user/updateUserProfile", {
          userId: this.userId,
          userProfile: this.user_profile,
        })
        .then((resp) => {});
    },
  },
};
</script>

<style></style>
