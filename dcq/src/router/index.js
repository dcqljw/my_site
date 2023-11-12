import {createRouter, createWebHashHistory} from 'vue-router'
import IndexView from '../views/IndexView.vue'
import ContactView from "@/views/ContactView.vue";
import ProjectView from "@/views/ProjectView.vue";
import BlogView from "@/views/BlogView.vue";
import AboutView from "@/views/AboutView.vue";
import CoverView from "@/views/CoverView.vue";
import AdminView from "@/views/AdminView.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: IndexView
    },
    {
        path: '/about',
        name: 'about',
        component: AboutView
    }, {
        path: "/contact",
        name: "contact",
        component: ContactView
    }, {
        path: "/project",
        name: 'project',
        component: ProjectView
    }, {
        path: "/blog",
        name: "blog",
        component: BlogView
    }, {
        path: "/cover",
        name: "cover",
        component: CoverView
    }, {
        path: "/dacdqmin",
        name: "admin",
        component: AdminView
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
