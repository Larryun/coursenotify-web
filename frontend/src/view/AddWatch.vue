<template>
  <div id="form-container" class="mt-5">
    <h1 id="form-header" class="display-4">CourseNotify</h1>
    <div id="form-header-description" class="font-weight-light mb-2">
      <span>I will notify you when a course is available to add.</span>
    </div>
    <b-alert variant="info" show>
      Current course database: <b>2021 Winter</b><br>
    </b-alert>
    <WatcheeForm id="watch-form"></WatcheeForm>
  </div>
</template>

<script>
import WatcheeForm from "../components/WatcheeForm";

export default {
  name: "AddWatchPage",
  components: {
    WatcheeForm
  },
}
</script>

<style scoped>

</style>