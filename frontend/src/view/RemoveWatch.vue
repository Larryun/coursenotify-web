<template>
  <div>
    <b-row align-h="center">
      <b-col col md="4" sm="12" class="mt-4">
        <b-overlay
            :show="busy"
            rounded="sm"
            opacity="0.6"
            spinner-small
            spinner-variant="primary"
        >
          <b-alert show aria-hidden :variant="alertVariant">
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
      if (this.removeStatus === "ok") {
        return `Class <b>${this.class_name}</b> for
               <b>${this.email}</b> is removed successfully
               with remove key ${this.removeID}!<br>We will stop notifying you.`;
      } else if (this.removeStatus === "failed") {
        if (this.reason === "remove key not found") {
          return `The remove key <b>${this.removeID}</b> is invalid.
                  If you think this is a mistake, you can try adding the class and remove again.`;
        } else if (this.reason === "removed key is used") {
          return `The remove key <b>${this.removeID}</b> is removed/used.
                  If you think this is a mistake, you can try adding the class and remove again.`;
        } else {
          return "Server Error..."
        }
      }
      return "Loading...";
    },
    alertVariant() {
      if (this.removeStatus === "loading") {
        return "info"
      } else if (this.removeStatus === "ok") {
        return "success"
      } else if (this.removeStatus === "failed") {
        return "danger"
      }
      return "info"
    }
  },
  data() {
    return {
      removeStatus: "info",
      class_name: "",
      reason: {},
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
        this.removeStatus = "ok"
        this.class_name = res.data.class_name
        this.email = res.data.email
      }).catch((error) => {
        this.busy = false;
        this.removeStatus = "failed"
        this.reason = error.response.data["msg"];
      })
    },
  }
}
</script>

<style scoped>

</style>