<template>
  <div class="container mb-4 pb-4">
    <p v-for="(item, index) in news.headlineList" :key="index">
      {{ item }}
    </p>

    <b-row>
      <b-col class="d-flex justify-content-end mb-2" cols="12">
        <b-pagination
          v-model="currentPage"
          :per-page="perPage"
          :total-rows="news.headlineCount"
          @change="fetchNewsHeadlines"
        >
        </b-pagination>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      perPage: 10,
      currentPage: 1,
    };
  },

  computed: {
    ...mapState(["news"]),
  },

  created() {
    console.log("======================");
    this.fetchNewsHeadlines();
  },

  methods: {
    fetchNewsHeadlines() {
      console.log("======================");
      this.$store
        .dispatch("news/getNewsHeadlines", {
          perPage: this.perPage,
          page: this.currentPage,
        })
        .then((resp) => {});
    },
  },
};
</script>

<style></style>
