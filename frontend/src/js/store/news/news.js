import ServiceNews from "../../service/news/ServiceNews.js";

export const namespaced = true;

export const state = {
  headlineList: [],
  headlineCount: 0,
};

export const mutations = {
  SET_HEADLINE_LIST(state, headlineList) {
    state.headlineList = headlineList;
  },
  SET_HEADLINE_COUNT(state, headlineCount) {
    state.headlineCount = headlineCount;
  },
};

export const actions = {
  getNewsHeadlines({ commit }, { perPage, page, home }) {
    return ServiceNews.getNewsHeadlines(perPage, page, home)
      .then((resp) => {
        commit("SET_HEADLINE_LIST", resp.data.results);
        commit("SET_HEADLINE_COUNT", resp.data.count);

        return resp;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },
};
