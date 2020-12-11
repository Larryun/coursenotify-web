<template>
  <div id="form-container" class="mt-5">
    <h1 id="form-header" class="display-4">CourseNotify</h1>
    <div id="form-header-description" class="font-weight-light mb-2">
      <span>Tell me a class and I will notify you when it's available to add.</span>
    </div>
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