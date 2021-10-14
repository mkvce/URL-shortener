const app = Vue.createApp({
    data() {
        return {
            host: 'localhost:8000/',
        }
    },
});

const mountedApp = app.mount("#app")