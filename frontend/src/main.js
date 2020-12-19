import Vue from 'vue'
import VueLodash from 'vue-lodash'
import router from './router'
import lodash from 'lodash'
import App from './App.vue'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import vSelect from 'vue-select'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-select/dist/vue-select.css'


Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueLodash, {lodash: lodash});
Vue.component("v-select", vSelect);

new Vue({
    router,
    render: h => h(App),
}).$mount('#app');
