<template>
  <!-- Section: Design Block -->

  <section class="text-center text-lg-start">
    <!-- Jumbotron -->
    <div class="container py-4">
      <div class="row g-0 align-items-center">
        <div class="col-lg-6 mb-5 mb-lg-0">
          <div
            class="card cascading-right"
            style="
              background: hsla(0, 0%, 100%, 0.55);
              backdrop-filter: blur(30px);
            "
          >
            <div class="card-body p-5 shadow-5 text-center">
              <h2 class="fw-bold mb-5">Sign up now</h2>
              <form @submit.prevent="submitForm">
                <!-- 2 column grid layout with text inputs for the first and last names -->
                <div class="row">
                  <div class="col-md-6 mb-4">
                    <div class="form-outline">
                      <input
                        v-model="first_name"
                        type="text"
                        id="form3Example1"
                        class="form-control"
                      />
                      <label class="form-label" for="form3Example1"
                        >First name</label
                      >
                    </div>
                  </div>
                  <div class="col-md-6 mb-4">
                    <div class="form-outline">
                      <input
                        v-model="last_name"
                        type="text"
                        id="form3Example2"
                        class="form-control"
                      />
                      <label class="form-label" for="form3Example2"
                        >Last name</label
                      >
                    </div>
                  </div>
                </div>

                <!-- Email input -->
                <div class="form-outline mb-4">
                  <input
                    v-model="email"
                    type="email"
                    id="form3Example3"
                    class="form-control"
                  />
                  <label class="form-label" for="form3Example3"
                    >Email address</label
                  >
                </div>

                <!-- Password input -->
                <div class="form-outline mb-4">
                  <input
                    v-model="password1"
                    type="password"
                    id="form3Example4"
                    class="form-control"
                  />
                  <label class="form-label" for="form3Example4">Password</label>
                </div>
                <div class="form-outline mb-4">
                  <input
                    v-model="password2"
                    type="password"
                    id="form3Example5"
                    class="form-control"
                  />
                  <label class="form-label" for="form3Example5"
                    >Re-enter password</label
                  >
                </div>
                <!-- Checkbox -->
                <div class="form-check d-flex justify-content-center mb-4">
                  <input
                    class="form-check-input me-2"
                    type="checkbox"
                    value=""
                    id="form2Example33"
                    checked
                  />
                  <label class="form-check-label" for="form2Example33">
                    Remember me
                  </label>
                </div>

                <!-- Submit button -->
                <button type="submit" class="btn btn-primary btn-block mb-4">
                  Sign up
                </button>

                <!-- Register buttons -->
                <div class="text-center">
                  <p>or sign up with:</p>
                  <button type="button" class="btn btn-link btn-floating mx-1">
                    <i class="fab fa-facebook-f"></i>
                  </button>

                  <button type="button" class="btn btn-link btn-floating mx-1">
                    <i class="fab fa-google"></i>
                  </button>

                  <button type="button" class="btn btn-link btn-floating mx-1">
                    <i class="fab fa-twitter"></i>
                  </button>

                  <button type="button" class="btn btn-link btn-floating mx-1">
                    <i class="fab fa-github"></i>
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>

        <div class="col-lg-6 mb-5 mb-lg-0">
          <img
            src="https://mdbootstrap.com/img/new/ecommerce/vertical/004.jpg"
            class="w-100 rounded-4 shadow-4"
            alt=""
          />
        </div>
      </div>
    </div>
    <!-- Jumbotron -->
  </section>
  <!-- Section: Design Block -->
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "Register",
  data() {
    return {
      first_name: "",
      last_name: "",
      email: "",
      password1: "",
      password2: "",
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      this.errors = [];
      if (this.first_name === "") {
        this.errors.push("The first name is missing");
      }
      if (this.last_name === "") {
        this.errors.push("The last name is missing");
      }
      if (this.email === "") {
        this.errors.push("The email is missing");
      }
      if (this.password1 === "") {
        this.errors.push("The password is missing");
      }
      if (this.password2 === "") {
        this.errors.push("The password is missing");
      }
      let endpoint = "/auth/users/";
      try {
        const response = await axios.post(endpoint, {
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          password: this.password1,
        });
        this.$router.push("/");
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style>
.cascading-right {
  margin-right: -50px;
}

@media (max-width: 991.98px) {
  .cascading-right {
    margin-right: 0;
  }
}
</style>
