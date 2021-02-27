console.log("動いた")
const Counter = {
    data: function () {
        return {
            counter: 0
        }
    }
}

Vue.createApp(Counter).mount('#counter')