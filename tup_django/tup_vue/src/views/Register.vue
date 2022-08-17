<template>
  <section class="vh-100" style="background-color: #eee">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-lg-12 col-xl-11">
          <div class="card text-black" style="border-radius: 25px">
            <div class="card-body p-md-5">
              <div class="row justify-content-center">
                <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">
                  <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">
                    Sign up
                  </p>

                  <form @submit.prevent="submitForm" class="mx-1 mx-md-4">
                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input
                          v-model="first_name"
                          type="text"
                          class="form-control"
                        />
                        <label class="form-label">First Name</label>
                      </div>
                      <div class="form-outline flex-fill mb-0">
                        <input
                          v-model="last_name"
                          type="text"
                          class="form-control"
                        />
                        <label class="form-label">Last Name</label>
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-envelope fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input
                          v-model="email"
                          type="email"
                          id="form3Example3c"
                          class="form-control"
                        />
                        <label class="form-label" for="form3Example3c"
                          >Your Email</label
                        >
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input
                          v-model="password1"
                          type="password"
                          id="form3Example4c"
                          class="form-control"
                        />
                        <label class="form-label" for="form3Example4c"
                          >Password</label
                        >
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-key fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input
                          v-model="password2"
                          type="password"
                          id="form3Example4cd"
                          class="form-control"
                        />
                        <label class="form-label" for="form3Example4cd"
                          >Repeat your password</label
                        >
                      </div>
                    </div>
                    <div
                      class="d-flex justify-content-center mx-4 mb-3 mb-lg-4"
                    >
                      <button type="submit" class="btn btn-primary btn-lg">
                        Register
                      </button>
                    </div>
                  </form>
                </div>
                <div
                  class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2"
                >
                  <img
                    src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/draw1.webp"
                    class="img-fluid"
                    alt="Sample image"
                  />
                </div>
              </div>
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
