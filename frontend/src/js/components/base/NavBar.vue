<template>
  <div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">News Portal</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">News Feed</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item v-if="!isAuthenticated" :to="{name:'login'}">Login</b-nav-item>
        <b-nav-item v-if="isAuthenticated" href="#">User</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
import {  mapState } from "vuex";
export default {
  data() {
    return {

    };
  },

   computed: {
    ...mapState(["user"]),

    isAuthenticated(){
      if(this.user.userInfo){
        return true
      }
      else{
        return false
      }
    }
  },

  created(){
    this.fetchUserInfo()
  },

  methods: {
    fetchUserInfo() {
      this.$store
        .dispatch("user/getUserInfo")
        .then((resp) => {
          console.log(resp.data)
        });
    },
  },
};
</script>


<style>

</style>