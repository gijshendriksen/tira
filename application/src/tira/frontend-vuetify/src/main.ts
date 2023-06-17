/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'
import Home from './Home.vue'
import Tasks from './Tasks.vue'
import TaskOverview from './TaskOverview.vue'
import RunUpload from './RunUpload.vue'

// Composables
import { createApp } from 'vue'
import { createRouter,createWebHistory} from 'vue-router'

// Plugins
import { registerPlugins } from '@/plugins'

export default function register_app() {
  const app_selector = '#app'

  const app_elem = document.querySelector(app_selector)
  if (app_elem && '__vue_app__' in app_elem && app_elem.__vue_app__) {
    console.log('TIRA app is already mounted.')
    return;
  }

  console.log('Mount TIRA vue app to location: ' + window.location)
  const routes = [
    {path: '/', component: Home},
    {path: '/tasks', component: Tasks},
    {path: '/task-overview/:task_id?/:dataset_id?', component: TaskOverview},
    {path: '/run-upload', component: RunUpload},
    // TODO: Temporary additional routes for transition form previous TIRA UI version.
    {path: '/frontend-vuetify/landing', component: Home},
    {path: '/frontend-vuetify/tasks', component: Tasks},
    {path: '/frontend-vuetify/task-overview/:task_id?/:dataset_id?', component: TaskOverview},
    {path: '/frontend-vuetify/run-upload', component: RunUpload},

    // Fallback: everything matches to home.
    { path: '/:pathMatch(.*)*', component: Home },
  ]
  const router = createRouter({
    history: createWebHistory(),
    routes: routes,
  })

  const app = createApp(App)
  app.use(router)

  registerPlugins(app)
  app.mount(app_selector)
}

declare global { interface Window { register_app: any; push_message: any}}
window.register_app = register_app;

register_app()
