<template>
    <div class="hello">
        <h1>{{ msg }}</h1>
    </div>
</template>

<script>

import $backend from '../backend'

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: ''
    }
  },
  methods: {
    fetchResource () {
      $backend.fetchResource()
        .then(responseData => {
          this.msg = responseData
        }).catch(error => {
          this.error = error.message
        })
    }
  },
  mounted () {
    this.fetchResource()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
    h3 {
        margin: 40px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>
