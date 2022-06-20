<template>
  <div class="p-4">
    <h4>{{ $t("News Feed Settings") }}</h4>

    <div class="mt-4"></div>

    <b-form @submit.prevent="onFormSubmit">
      <b-form-group :label="$t('Sources')">
        <Select2
          v-model="news_feed_settings.news_sources"
          :options="sourceOptions"
          :settings="{
            width: '100%',
            placeholder: 'News Sources',
            multiple: true,
          }"
        />
      </b-form-group>

      <b-form-group :label="$t('Country')">
        <Select2
          v-model="news_feed_settings.country_of_news"
          :options="countryOptions"
          :settings="{
            width: '100%',
            placeholder: 'Country',
            multiple: true,
          }"
        />
      </b-form-group>

      <b-form-group :label="$t('Keywords')">
        <Select2
          v-model="news_feed_settings.news_keywords"
          :options="keywordOptions"
          :settings="{
            width: '100%',
            placeholder: 'Keywords',
            multiple: true,
            tags: true,
          }"
        />
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
      countryList: [],
      sourceList: [],
      userId: null,
      news_feed_settings: {
        news_sources: [],
        country_of_news: [],
        news_keywords: [],
      },
    };
  },
  components: {},

  created() {
    this.fetchUserInfo();
    this.fetchFormData();
  },

  computed: {
    sourceOptions() {
      let options = [];
      this.sourceList.forEach((item) => {
        options.push({
          id: item.id,
          text: item.name,
        });
      });
      return options;
    },

    countryOptions() {
      let options = [];
      this.countryList.forEach((item) => {
        options.push({
          id: item.code,
          text: item.name,
        });
      });
      return options;
    },

    keywordOptions() {
      let options = [];
      this.news_feed_settings.news_keywords.forEach((item) => {
        options.push({
          id: item,
          text: item,
        });
      });
      return options;
    },
  },

  methods: {
    fetchUserInfo() {
      this.$store.dispatch("user/getUserInfo").then((resp) => {
        if (resp.status == 200) {
          this.userId = resp.data.id;
          this.news_feed_settings.news_sources = resp.data.news_sources;
          if (resp.data.news_sources) {
            this.news_feed_settings.country_of_news = resp.data.country_of_news;
          }
          if (resp.data.news_keywords) {
            this.news_feed_settings.news_keywords = resp.data.news_keywords;
          }
        }
      });
    },

    fetchFormData() {
      this.$store.dispatch("user/getFormData").then((resp) => {
        if (resp.status == 200) {
          this.countryList = resp.data.country_list;
          this.sourceList = resp.data.source_list;
        }
      });
    },

    onFormSubmit() {
      this.$store
        .dispatch("user/updateUserProfile", {
          userId: this.userId,
          userProfile: this.news_feed_settings,
        })
        .then((resp) => {});
    },
  },
};
</script>

<style></style>
