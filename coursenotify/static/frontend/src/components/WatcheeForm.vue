<template>
  <div id="watch_form">
    <b-form @submit="submitWatcheeForm">
      <b-form-group
          id="email-input-group"
          label="Email address:"
          label-for="email-input"
      >
        <b-form-input
            id="email-input"
            v-model="form.email"
            type="email"
            required
            placeholder="Enter email"
            :state="state['email_input']"
        ></b-form-input>
        <b-form-text :text-variant="mutedOrDanger(state['email_input'])">
          I'll notify you through this email
        </b-form-text>
        <b-form-invalid-feedback :state="state['email_input']">
          The email {{ form.email }} is not a valid email
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group id="school-input-group" label="School:">
        <b-form-radio-group id="school-checkbox-group"
                            v-model="form.school"
                            name="school"
                            required
                            @change="resetSelect"
                            :state="state['school_input']"
        >
          <b-row>
            <b-col>
              <b-form-radio value="DA">De Anza</b-form-radio>
            </b-col>
            <b-col>
              <b-form-radio value="FH">Foothill</b-form-radio>
            </b-col>
          </b-row>
        </b-form-radio-group>
        <b-form-text :text-variant="mutedOrDanger(state['school_input'])">
          The school where the course is provided
        </b-form-text>
        <b-form-invalid-feedback :state="state['school_input']">
          Invalid school choice {{ form.school }}!! WTF?
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group id="crn-input-group" label="School:">
        <v-select label="crn"
                  v-model="form.crn"
                  :filterable="false"
                  :options="courseOptions"
                  :reduce="course => course.crn"
                  @search="onSearchCRN"
                  @search:focus="updateNoOpMsg"
        >
          <template #search="{attributes, events}">
            <input
                class="vs__search"
                :required="!selected"
                v-bind="attributes"
                v-on="events"
            />
          </template>
          :

          <template slot="no-options">
            {{ noOptionsMsg }}
          </template>
          <template slot="option" slot-scope="option">
            <div class="d-center">
              {{ `${option.crn} - ${option.name} - ${option.title}` }}
            </div>
          </template>
          <template slot="selected-option" slot-scope="option">
            <div class="selected d-center">
              {{ option.crn }}
            </div>
          </template>
        </v-select>
        <b-form-text>
          The course that you want to watch
        </b-form-text>

      </b-form-group>
      <b-button type="submit" variant="primary" :disabled="submitBtnDisabled">Submit</b-button>
    </b-form>
    <div :class='"mt-3 alert alert-" + alertType' role="alert" v-if="showAlert">
      {{ alertMessage }}
    </div>
  </div>
</template>

<script>
import axios from "axios";
import vSelect from "vue-select";
import _ from 'lodash'

export default {
  name: "WatcheeForm",
  components: {
    vSelect,
  },
  data() {
    return {
      form: {
        email: "",
        crn: "",
        school: ""
      },
      alertMessage: "",
      alertType: "",
      showAlert: false,
      submitBtnDisabled: false,
      state: {
        email_input: null,
        crn_input: null,
        school_input: null,
      },
      courseOptions: [],
      noOptionsMsg: "Please choose a school",
      selected: false,
      selectedValue: "",
    }
  },
  methods: {
    submitWatcheeForm(e) {
      e.preventDefault();
      console.log(this.form)
      this.submitBtnDisabled = true;
      this.alertType = "";
      this.alertMessage = "";
      this.showAlert = false;
      this.state = {
        email_input: null,
        crn_input: null,
        school_input: null,
      }
      axios.post(process.env.VUE_APP_API_URL + "/add", this.form).then((res) => {
        this.updateAlert(res.data);
        this.submitBtnDisabled = false;
        this.selected = false;
      })
    },
    updateAlert(result) {
      this.showAlert = true;
      console.log(result)
      if (result["status"] === "ok") {
        this.alertType = "success";
        this.alertMessage = `Added ${this.form.email} for course ${this.form.crn}`;
      }
      if (result["crn"] === "not valid") {
        this.state.crn_input = false;
      }
      if (result["school"] === "not valid") {
        this.state.school_input = false;
      }
      if (result["email"] === "not valid") {
        this.state.email_input = false;
      }
      if ("server_error" in result) {
        this.alertType = "danger";
        this.alertMessage = "Server Error";
      }
    },
    onSearchCRN(crn, loading) {
      loading(true);
      this.courseOptions = [];
      if (this.form.school === "") {
        this.noOptionsMsg = "Please choose a school";
      } else if (crn === "") {
        this.noOptionsMsg = "Please enter a crn";
      } else if (crn.length < 3) {
        this.noOptionsMsg = "Please enter more digits";
      } else {
        this.searchCRN(crn, loading, this);
      }
      loading(false)
    },
    searchCRN: _.debounce((crn, loading, vm) => {
      vm.noOptionsMsg = "Loading...";
      axios.post(process.env.VUE_APP_API_URL + "/query", {school: vm.form.school, crn: crn}).then((res) => {
        if (res.data["status"] !== "ok" || res.data["course"].length === 0) {
          vm.noOptionsMsg = "CRN not found in the database, let me know if you believe this is an error";
        } else {
          vm.courseOptions = res.data["course"];
          vm.selected = true;
        }
      })
    }, 500),
    mutedOrDanger(s) {
      return s === false ? "danger" : "muted";
    },
    updateNoOpMsg() {
      this.courseOptions = [];
      if (this.form.school === "") {
        this.noOptionsMsg = "Please choose a school";
      } else {
        this.noOptionsMsg = "Please enter a crn";
      }
    },
    resetSelect() {
      this.selectedValue = "";
      this.form.crn = "";
    }
  }
}
</script>

<style scoped>
#watch_form {
  width: 100%;
}

</style>