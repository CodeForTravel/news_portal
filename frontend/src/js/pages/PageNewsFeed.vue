<template>
  <div class="container mb-4 pb-4">
    <b-row v-if="news.headlineList.length > 0">
      <b-col
        class="p-2"
        cols="4"
        v-for="(item, index) in news.headlineList"
        :key="index"
      >
        <card-news :news-info="item"></card-news>
      </b-col>
    </b-row>

    <b-row v-else>
      <b-col class="p-4">
        <b-alert show variant="warning"> No news available</b-alert>
      </b-col>
    </b-row>

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
const CardNews = () => import("../components/news/CardNews.vue");
export default {
  data() {
    return {
      perPage: 10,
      currentPage: 1,
    };
  },

  components: { CardNews },

  computed: {
    ...mapState(["news"]),
  },

  created() {
    this.fetchNewsHeadlineRecursively();
  },

  methods: {
    fetchNewsHeadlineRecursively() {
      this.fetchNewsHeadlines();
      setTimeout(this.fetchNewsHeadlineRecursively, 1000 * 60 * 7);
    },

    fetchNewsHeadlines() {
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
