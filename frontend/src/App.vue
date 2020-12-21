<template>
  <div id="app">
    <router-view></router-view>
    <footer>
        <span class="font-weight-light text-muted">
          <a href="/">FHDA CourseNotify</a> v1.2 | Email: <a href="mailto:coursenotfy@gmail.com">coursenotify@gmail.com</a>
          <br>
          Made by a <del class="c">De Anza College</del> UC Berkeley student
          <br>
          © 2020 CourseNotify
        </span>
    </footer>
  </div>
</template>

<script>

export default {
  name: 'App',
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
  text-align: center;
}

</style>
