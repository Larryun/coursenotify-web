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
          <b-alert show aria-hidden :variant="removeStatus">
            <div v-html="alertText"></div>
          </b-alert>
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
    alertText() {
      if (this.removeStatus === "success") {
        return `Class <b>${this.class_name}</b> for
               <b>${this.email}</b> removed successfully
               with remove key ${this.removeID}!`;
      } else if (this.removeStatus === "danger") {
        if (this.res["msg"] === "remove key not found") {
          return `The remove key <b>${this.removeID}</b> is invalid`
        } else if (this.res["msg"] === "removed key is used") {
          return `The remove key <b>${this.removeID}</b> is removed/used.
                  If you think this is a mistake, you can try adding the class and remove again.`;
        } else {
          return "Server Error..."
        }
      }
      return "Loading...";
    },
  },
  data() {
    return {
      removeStatus: "info",
      class_name: "",
      response: {},
      email: "",
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
      axios.post(process.env.VUE_APP_API_URL + "/remove", data).then((res) => {
        this.busy = false;
        this.removeStatus = "success"
        this.class_name = res.data.class_name
        this.email = res.data.email
      }).catch((error) => {
        this.res = error.response.data;
        this.busy = false;
        this.removeStatus = "danger"
      })
    },
  }
}
</script>

<style scoped>

</style>