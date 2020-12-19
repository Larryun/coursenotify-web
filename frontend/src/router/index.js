import Vue from 'vue'
import VueRouter from 'vue-router'
import AddWatchPage from "../view/AddWatch";
import RemoveWatch from "../view/RemoveWatch";

Vue.use(VueRouter);

const router = new VueRouter({
    mode: "history",
    routes: [
        {
            path: '/',
            name: 'Index',
            component: AddWatchPage
        },
        {
            path: '/(da|fh)/remove/:remove_key',
            name: 'RemoveWatch',
            component: RemoveWatch
        },
    ]
})

export default router;
