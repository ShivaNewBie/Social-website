<template>
  <!-- Section: Design Block -->
  <section class="text-center text-lg-start">
    <div class="card mb-3">
      <div class="row g-0 d-flex align-items-center">
        <div class="col-lg-4 d-none d-lg-flex">
          <img
            src="https://mdbootstrap.com/img/new/ecommerce/vertical/004.jpg"
            alt="Trendy Pants and Shoes"
            class="w-100 rounded-t-5 rounded-tr-lg-0 rounded-bl-lg-5"
          />
        </div>
        <div class="col-lg-8">
          <div class="card-body py-5 px-md-5">
            <form @submit.prevent="onSubmit">
              <!-- Email input -->
              <div class="form-outline mb-4">
                <input
                  v-model="email"
                  type="email"
                  id="form2Example1"
                  class="form-control"
                />
                <label class="form-label" for="form2Example1"
                  >Email address</label
                >
              </div>

              <!-- Password input -->
              <div class="form-outline mb-4">
                <input
                  v-model="password1"
                  type="password"
                  id="form2Example2"
                  class="form-control"
                />
                <label class="form-label" for="form2Example2">Password</label>
              </div>
              <!-- Submit button -->
              <button
                type="submit"
                class="form-control btn btn-primary btn-block mb-4"
              >
                Sign in
              </button>
              <!-- 2 column grid layout for inline styling -->
              <div class="row mb-4">
                <div class="col d-flex justify-content-center">
                  <!-- Checkbox -->
                  <div class="form-check">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      value=""
                      id="form2Example31"
                      checked
                    />
                    <label class="form-check-label" for="form2Example31">
                      Remember me
                    </label>
                  </div>
                </div>
                <div class="col">
                  <!-- Simple link -->
                  <a href="#!">Register</a>
                </div>
                <div class="col">
                  <!-- Simple link -->
                  <a href="#!">Forgot password?</a>
                </div>
              </div>
            </form>
            <div class="notification is-danger" v-if="errors.length">
              <!--Check if there are errors -->
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "Login",
  data() {
    return {
      email: "",
      password1: "",
      errors: [],
    };
  },
  methods: {
    async onSubmit() {
      let endpoint = "/auth/token/login/";
      this.errors = [];
      if (this.email === "") {
        this.errors.push("The email is missing");
      }
      if (this.password1 === "") {
        this.errors.push("The password is missing");
      }

      try {
        const response = await axios.post(endpoint, {
          email: this.email,
          password: this.password1,
        });
        const token = response.data.auth_token;

        this.$store.commit("setToken", token);

        axios.defaults.headers.common["Authorization"] = "Token " + token;

        localStorage.setItem("token", token);

        this.$router.push("/");
        console.log(response);
        // console.log(response.data.auth_token);
      } catch (error) {
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`);
          }
        } else if (error.message) {
          this.errors.push("Something went wrong. Please try again");
        }
      }
    },
  },
};
</script>
<style>
.rounded-t-5 {
  border-top-left-radius: 0.5rem;
  border-top-right-radius: 0.5rem;
}

@media (min-width: 992px) {
  .rounded-tr-lg-0 {
    border-top-right-radius: 0;
  }

  .rounded-bl-lg-5 {
    border-bottom-left-radius: 0.5rem;
  }
}
</style>
