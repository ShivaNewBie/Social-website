//https://docs.djangoproject.com/en/3.2/ref/csrf/

const axios = require("axios");

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export { axios };
