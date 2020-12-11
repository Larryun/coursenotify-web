<template>
  <div>
    <b-row align-h="center">
      <b-col cols="4" class="mt-4">
        <b-overlay
            :show="busy"
            rounded="sm"
            opacity="0.6"
            spinner-small
            spinner-variant="primary"
        >
          <b-alert show aria-hidden :variant="removeStatus">{{ alertText }}</b-alert>
        </b-overlay>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RemoveWatch",
  computed: {
    removeID() {
      return this.$route.params.remove_key;
    },
  },
  data() {
    return {
      removeStatus: "info",
      alertText: "Loading...",
      busy: true
    }
  },
  mounted() {
    this.$nextTick(() => {
          this.removeWatch(this.removeID);
        }
    )
  },
  methods: {
    async removeWatch(removeID) {
      let school = this.$route.params.pathMatch.toUpperCase();
      let data = {school: school, remove_key: removeID};
      axios.post(process.env.VUE_APP_API_URL + "/remove", data).then(() => {
        this.busy = false;
        this.removeStatus = "success"
        this.alertText = `${removeID} removed successfully!`
      }).catch((error) => {
        let res = error.response;
        this.busy = false;
        this.removeStatus = "danger"
        console.log(res)
        if (res.data["msg"] === "remove key not found") {
          this.alertText = `The key ${removeID} is invalid`
        } else if (res.data["msg"] == "removed key is used") {
          this.alertText = `The key ${removeID} is removed/used`;
        } else{
          this.alertText = "Server Error..."
        }
      })
    },
  }
}
</script>

<style scoped>

</style>