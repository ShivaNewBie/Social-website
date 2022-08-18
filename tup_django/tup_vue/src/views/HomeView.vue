<template>
  <div class="home">
    {{ this.$store.state.token }}
  </div>
</template>

<script>
// @ is an alias to /src
import { store } from "@/store/index.js";

export default {
  name: "HomeView",
  components: {},
};
</script>
