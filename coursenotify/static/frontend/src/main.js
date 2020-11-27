import Vue from 'vue'
import App from './App.vue'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import vSelect from 'vue-select'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-select/dist/vue-select.css'
import VueLodash from 'vue-lodash'
import lodash from 'lodash'

// name is optional

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueLodash, {lodash: lodash});
Vue.component("v-select", vSelect);

new Vue({
    render: h => h(App),
}).$mount('#app');
