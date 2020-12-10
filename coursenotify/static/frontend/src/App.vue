<template>
  <div id="app">
    <div id="form-container" class="mt-5">
      <h1 id="form-header" class="display-4">CourseNotify</h1>
      <div id="form-header-description" class="font-weight-light mb-2">
        <span>Tell me a class and I will notify you when it's available to add.</span>
      </div>
      <WatcheeForm id="watch-form"></WatcheeForm>
    </div>
    <footer>
      <span class="font-weight-light text-muted">
        CourseNotify v1.2 | Email: coursenotify@gmail.com
      </span>
    </footer>
  </div>
</template>

<script>
import WatcheeForm from "./components/WatcheeForm";

export default {
  name: 'App',
  components: {
    WatcheeForm
  },
  mounted() {
  },
  data() {
    return {}
  },
  methods: {}
}
</script>

<style>
#app {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
  Roboto, "Helvetica Neue", Arial, sans-serif,
  "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  -moz-osx-font-smoothing: grayscale;
}

#form-container {
  margin: auto;
  max-width: 400px;
}

#watch-form {
  padding-top: 7px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: lightgrey;
}

#form-header {
}

#form-header-description {
  font-size: 28px;
}

footer {
  border-top-width: 1px;
  border-top-style: solid;
  border-color: lightgrey;
  height: 100px;
  margin: 0 auto;
  margin-top: 5rem;
  max-width: 400px;
  display: flex !important;
  justify-content: center;
  padding: 5px;
}

</style>
