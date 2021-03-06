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
  getNewsHeadlines(perPage, page, home) {
    var relativeURL =
      urlList.urlRoot + "top-headlines/?page_size=" + perPage + "&page=" + page;

    if (home) {
      relativeURL = relativeURL + "&home_page=" + home;
    }
    return apiClient.get(relativeURL);
  },
};
