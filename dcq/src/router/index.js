import {createRouter, createWebHashHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ContactView from "@/views/ContactView.vue";
import ProjectView from "@/views/ProjectView.vue";
import BlogView from "@/views/BlogView.vue";
import AboutView from "@/views/AboutView.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
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
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
