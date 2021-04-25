<template>
    <div id="app">
        <router-view/>
        <h1>Sarcasm detector</h1>

        <b-form class="way-form" @submit.prevent="submit">
            <b-form-group
                    id="input-group-1"
                    label="sentence input:"
                    label-for="input-1"
                    description=""
            >
                <b-form-input
                        id="input-1"
                        v-model="form.input"
                        type="text"
                        required
                        placeholder="enter sentence"
                ></b-form-input>
            </b-form-group>
<!--            <v-button :onClick="alertClick">Alert</v-button>-->
            <v-button :onClick="faker">Predict</v-button>
        </b-form>

        <br>
        Sarcasm Score:
        <v-runtime-template :template="'<span>' + score + '</span>'"/>
        <br>
        Sentiment:
        <v-runtime-template :template="'<span>' + senti + '</span>'"/>
        <br>
        Sentence:
        <v-runtime-template :template="'<span>' + msg + '</span>'"/>
    </div>
</template>

<script>

import $backend from './backend'
import Button from './components/Button.vue'
import VRuntimeTemplate from 'v-runtime-template'

export default {
  name: 'app',
  data () {
    return {
      msg: '',
      score: '',
      senti: '',
      form: {
        input: ''
      }
    }
  },
  components: {
    'v-button': Button,
    VRuntimeTemplate
  },
  methods: {
    alertClick () {
      alert('button clicked')
    },
    faker () {
      return null
    },
    submit () {
      $backend.postResource(this.form.input)
        .then(responseData => {
          console.log(responseData)
          this.msg = responseData.sentence
          this.score = responseData.predict
          this.senti = responseData.sentiment.label + ' ' + responseData.sentiment.score

          console.log(responseData)
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
