<template>
  <router-view />
</template>
<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "App",
  beforeCreate() {
    //before code will run
    this.$store.commit("initializeStore"); //the commit will make initializeStore run or use the function
    console.log(this.$store.state.token);

    if (this.$store.state.token) {
      //reference to the token
      axios.defaults.headers.common["Authorization"] =
        "Token " + this.$store.state.token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
};
</script>

<style lang="scss"></style>
