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
            :state="inputStates['email_input']"
        ></b-form-input>
        <b-form-text :text-variant="mutedOrDanger(inputStates['email_input'])">
          I'll notify you through this email
        </b-form-text>
        <b-form-invalid-feedback :state="inputStates['email_input']">
          The email {{ form.email }} is not a valid email
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group id="school-input-group" label="School:">
        <b-form-radio-group id="school-checkbox-group"
                            v-model="form.school"
                            name="school"
                            required
                            @change="resetSelect"
                            :state="inputStates['school_input']"
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
        <b-form-text :text-variant="mutedOrDanger(inputStates['school_input'])">
          The school where the course is provided
        </b-form-text>
        <b-form-invalid-feedback :state="inputStates['school_input']">
          Invalid school choice {{ form.school }}!! WTF?
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group id="crn-input-group" label="School:">
        <!-- cannot use this directly because options will be erased and the values become undefined-->
        <!--v-model="selectedCRN"-->
        <v-select label="crn"
                  ref="crn_select"
                  multiple
                  :filterable="false"
                  :options="courseOptions"
                  :reduce="course => course.crn"
                  @search="onSearchCRN"
                  @search:focus="validateCRN"
                  @input="onSelectInput"
        >
          <template #search="{attributes, events}">
            <input
                class="vs__search"
                :required="!selectInputFilled"
                v-bind="attributes"
                v-on="events"
            />
          </template>
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
        crn: [],
        school: ""
      },
      alertMessage: "",
      alertType: "",
      showAlert: false,
      submitBtnDisabled: false,
      inputStates: {
        email_input: null,
        crn_input: null,
        school_input: null,
      },
      typedCRN: "",     // used for validation
      courseOptions: [],
      noOptionsMsg: "Please choose a school",
    }
  },
  computed: {
    selectInputFilled() {
      console.log("input filled", this.form.crn)
      return this.form.crn.length !== 0;
    }
  },
  methods: {
    submitWatcheeForm(e) {
      e.preventDefault();
      // console.log("submitting" + this.form);
      this.submitBtnDisabled = true;
      this.resetAlert();
      this.resetInputStates();
      axios.post(process.env.VUE_APP_API_URL + "/add", this.form).then((res) => {
        this.updateAlert(res.data);
        this.submitBtnDisabled = false;
      }).catch((res) => {
        this.updateAlert(res.response.data);
        this.submitBtnDisabled = false;
      })
    },
    updateAlert(result) {
      this.showAlert = true;
      if (result["status"] === "ok") {
        this.alertType = "success";
        this.alertMessage = `Added ${this.form.email} for course ${this.form.crn}`;
      }
      if (result["crn"] === "not valid") {
        this.inputStates.crn_input = false;
      }
      if (result["school"] === "not valid") {
        this.inputStates.school_input = false;
      }
      if (result["email"] === "not valid") {
        this.inputStates.email_input = false;
      }
      if ("server_error" in result) {
        this.alertType = "danger";
        this.alertMessage = "Server Error";
      }
    },
    onSearchCRN(crn, loading) {
      // console.log(crn)
      loading(true);
      this.courseOptions = [];
      this.typedCRN = crn;
      if (this.validateCRN()) {
        this.noOptionsMsg = "Loading...";
        this.searchCRN(crn, loading, this);
      }
      loading(false)
    },
    /**
     * search for the crn with prefix
     */
    searchCRN: _.debounce((crn, loading, vm) => {
      axios.post(process.env.VUE_APP_API_URL + "/query", {school: vm.form.school, crn: crn}).then((res) => {
        if (res.data["status"] !== "ok" || res.data["course"].length === 0) {
          vm.noOptionsMsg = "CRN not found in the database";
        } else {
          vm.courseOptions = res.data["course"];
        }
      }).catch((error) => {
        let res = error.response;
        if ("server_error" in res.data) {
          vm.noOptionsMsg = "Server error...";
        }
      })
    }, 100),
    /**
     * update validate message for crn select input
     * @returns {boolean}
     */
    validateCRN() {
      this.courseOptions = [];
      if (this.form.school === "") {
        this.noOptionsMsg = "Please choose a school first";
      } else if(this.form.crn.length >= 4) {
        this.noOptionsMsg = "Select maximum 4 course at a time";
      } else if (this.typedCRN === "") {
        this.noOptionsMsg = "Please enter a crn";
      } else if (this.typedCRN.length < 3) {
        this.noOptionsMsg = "Please enter more digits";
      } else {
        return true;
      }
    },
    resetSelect() {
      this.form.crn = [];
      // clear current selected options
      this.$refs.crn_select.clearSelection();
    },
    resetAlert() {
      this.showAlert = false;
      this.alertType = "";
      this.alertMessage = "";
    },
    resetInputStates() {
      this.inputStates = {
        email_input: null,
        crn_input: null,
        school_input: null,
      }
    },
    onSelectInput(e) {
      this.form.crn = e
    },
    mutedOrDanger(s) {
      return s === false ? "danger" : "muted";
    },
  }
}
</script>

<style scoped>
#watch_form {
  width: 100%;
}

</style>

<style>
.vs__search {
  line-height: 1.5 !important;
}
</style>
