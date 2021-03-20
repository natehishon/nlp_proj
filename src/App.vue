<template>
  <div id="app">
    <router-view/>
    <h1>Sarcasm detector</h1>
    <v-button :onClick="alertClick">Alert</v-button>
    <v-button :onClick="fetchResource">Predict</v-button>
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>

import $backend from './backend'
import Button from './components/Button.vue'

export default {
  name: 'app',
  data () {
    return {
      msg: ''
    }
  },
  components: {
    'v-button': Button
  },
  methods: {
    alertClick () {
      alert('button clicked')
    },
    fetchResource () {
      $backend.fetchResource()
        .then(responseData => {
          this.msg = responseData
        }).catch(error => {
          this.error = error.message
        })
    }
  }
}

</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
#plus {
  padding: 0 20px 0 20px;
  display: inline-block;
  font-size: 50px;
  vertical-align: top;
  line-height: 100px;
}

</style>
