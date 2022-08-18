import { createStore } from "vuex";

export default createStore({
  state: {
    token: "",
    isAuthenticated: true,
  },
  mutations: {
    initializeStore(state) {
      //this function only inializes an if statement not change any data rather it checks whether the data is authenticated
      if (localStorage.getItem("token")) {
        //token determines if the user is authenticated
        state.token = localStorage.getItem("token");
      }
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
  },
});
