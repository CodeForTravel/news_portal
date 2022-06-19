import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const apiClient = axios.create({
  baseURL: process.env.BACKEND_HOST,
});

const urlList = {
  urlRoot: "/api/v1/news/",
};

export default {
  getNewsHeadlines(perPage, page) {
    var relativeURL =
      urlList.urlRoot + "top-headlines/?page_size=" + perPage + "&page=" + page;
    return apiClient.get(relativeURL);
  },
};
