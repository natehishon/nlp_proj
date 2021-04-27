<template>
    <div id="app">
        <router-view/>
        <span class="main-title">Is It Sarcasm?</span>
        <br>
        <br>
        <b-container class="parent-container">
            <b-row>
                <b-col sm="6" offset-sm="3">

                    <b-form class="sentence-form" @submit.prevent="submit">
                        <b-form-group>
                            <div class="search-form-container">
                                <b-input
                                        v-model="form.input"
                                        class="mb-2 ml-2 mr-sm-2 mb-sm-0 sentence-input"
                                        placeholder="try a sentence"
                                ></b-input>
                                <b-button style="width: 130px;" size="md" @click="submit()" variant="info"
                                          class="go-button">
                                    <i class="fas fa-search"></i>&nbsp;go!
                                </b-button>
                            </div>

                        </b-form-group>
                        <!--            <v-button :onClick="alertClick">Alert</v-button>-->
                        <!--                        <v-button :onClick="faker">Predict</v-button>-->
                    </b-form>
                </b-col>
            </b-row>

            <br>
            <br>

            <b-row>
                <!--                <b-col sm="8" md="6" lg="4" offset-sm="2" offset-md="3" offset-lg="4">-->
                <b-col sm="12">
                     <b-spinner style="width: 5rem; height: 5rem;" variant="info" label="Spinning" v-if="loading"></b-spinner>
                    <div v-if="response" class="response-container">
                        <b-card-group deck>
                            <b-card header-html="Sarcasm Score <img style='display:inline-block' class='emoji-image' src='https://cdn.shopify.com/s/files/1/1061/1924/files/Upside-Down_Face_Emoji.png?9898922749706957214'></img>" class="text-center" header-bg-variant="info"
                                    header-text-variant="white">
                                <b-card-text>
                                    <v-runtime-template :template="'<span>' + score + '</span>'"></v-runtime-template>

                                </b-card-text>
                            </b-card>

                            <b-card header-html="Sentiment Score <img style='display:inline-block' class='emoji-thumb' src='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/279/thumbs-up_1f44d.png'></img>" class="text-center" header-bg-variant="info"
                            header-text-variant="white">
                                <b-card-text>
                                    <v-runtime-template :template="'<span>' + senti + '</span>'"/>
                                </b-card-text>
                            </b-card>

                            <b-card header-html="Feature Importance <img style='display:inline-block' class='emoji-think' src='https://www.dictionary.com/e/wp-content/uploads/2018/03/Thinking_Face_Emoji-Emoji-Island.png'></img>" class="text-center" header-bg-variant="info"
                            header-text-variant="white">
                                <b-card-text>
                                    <v-runtime-template :template="'<span>' + msg + '</span>'"/>
                                </b-card-text>
                            </b-card>
                        </b-card-group>
                    </div>
                </b-col>
            </b-row>
            <br>
            <br>
            <b-row>
                <!--                <b-col sm="8" md="6" lg="4" offset-sm="2" offset-md="3" offset-lg="4">-->
                <b-col sm="6" offset-sm="3">
                    <div v-if="response" class="response-container">
                        <b-card-group deck>
                            <b-card v-if="type1" header-html="Recommendation: <img style='display:inline-block' class='emoji-image' src='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/279/check-mark-button_2705.png'></img>" class="text-center" header-bg-variant="success"
                                    header-text-variant="white">
                                <b-card-text>
<!--                                    hi there-->
                                    <span>We rate this as positive and not very sarcastic, hooray!</span>
                                </b-card-text>
                            </b-card>
                            <b-card v-if="type2" header-html="Recommendation: <img style='display:inline-block' class='emoji-stop' src='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/microsoft/209/cross-mark_274c.png'></img>" class="text-center" header-bg-variant="danger"
                                    header-text-variant="white">
                                <b-card-text>
                                    <span>We rate this as positive but pretty sarcastic, proceed with caution!</span>
<!--                                    You are so smart-->

                                </b-card-text>
                            </b-card>
                            <b-card v-if="type3" header-html="Recommendation: <img style='display:inline-block' class='emoji-stop' src='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/microsoft/209/cross-mark_274c.png'></img>" class="text-center" header-bg-variant="danger"
                                    header-text-variant="white">
                                <b-card-text>
<!--                                    this sucks so bad-->
                                    <span>We rate this as negative and not very sarcastic, boo!</span>

                                </b-card-text>
                            </b-card>
                            <b-card v-if="type4" header-html="Recommendation: <img style='display:inline-block' class='emoji-image' src='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/279/check-mark-button_2705.png'></img>" class="text-center" header-bg-variant="success"
                                    header-text-variant="white">
                                <b-card-text>
<!--                                    I'm sorry, I totally should have done that! -->
                                    <span>We rate this as negative but pretty sarcastic, proceed with optimism!</span>

                                </b-card-text>
                            </b-card>
<!--                            <b-card header-html="Sarcasm Score <img style='display:inline-block' class='emoji-image' src='https://cdn.shopify.com/s/files/1/1061/1924/files/Upside-Down_Face_Emoji.png?9898922749706957214'></img>" class="text-center" header-bg-variant="info"-->
<!--                                    header-text-variant="white">-->
<!--                                <b-card-text>-->
<!--                                    <v-runtime-template :template="'<span>' + score + '</span>'"></v-runtime-template>-->

<!--                                </b-card-text>-->
<!--                            </b-card>-->
                        </b-card-group>
                    </div>
                </b-col>
            </b-row>

        </b-container>

        <!--        Sarcasm Score:-->
        <!--        <v-runtime-template :template="'<span>' + score + '</span>'"/>-->
        <!--        <br>-->
        <!--        Sentiment:-->
        <!--        <v-runtime-template :template="'<span>' + senti + '</span>'"/>-->
        <!--        <br>-->
        <!--        Sentence:-->
        <!--        <v-runtime-template :template="'<span>' + msg + '</span>'"/>-->
    </div>
</template>

<script>

import $backend from './backend'
import Button from './components/Button.vue'
import VRuntimeTemplate from 'v-runtime-template'
import { BCard, BCardGroup } from 'bootstrap-vue'

export default {
  name: 'app',
  data () {
    return {
      loading: false,
      response: false,
      type1: false,
      type2: false,
      type3: false,
      type4: false,
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
    VRuntimeTemplate,
    BCard,
    BCardGroup
  },
  methods: {
    alertClick () {
      alert('button clicked')
    },
    faker () {
      return null
    },
    submit () {
      console.log('SUB')
      this.loading = true
      this.response = false
      $backend.postResource(this.form.input)
        .then(responseData => {
          this.type1 = false
          this.type2 = false
          this.type3 = false
          this.type4 = false
          this.loading = false
          this.response = true
          this.msg = responseData.sentence
          this.score = responseData.predict
          this.senti = responseData.sentiment.label + ' ' + responseData.sentiment.score

          const sarcasm = parseInt(this.score)

          if (sarcasm < 50 && responseData.sentiment.label === 'POSITIVE') {
            this.type1 = true
          }
          if (sarcasm > 49 && responseData.sentiment.label === 'POSITIVE') {
            this.type2 = true
          }
          if (sarcasm < 50 && responseData.sentiment.label === 'NEGATIVE') {
            this.type3 = true
          }
          if (sarcasm > 49 && responseData.sentiment.label === 'NEGATIVE') {
            this.type4 = true
          }
        }).catch(error => {
          this.error = error.message
        })
    }
  }
}

</script>

<style lang="scss">

    @font-face {
        font-family: 'casino_shadowregular';
        src: url('../src/assets/casinoshadowregular-0wdyp-webfont.woff2') format('woff2'),
        url('../src/assets/casinoshadowregular-0wdyp-webfont.woff') format('woff');
        font-weight: normal;
        font-style: normal;

    }

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

    .main-title {
        font-family: "casino_shadowregular";
        font-size: 120px;
    }

    .sentence-form {
        width: 100%;
    }

    .search-form-container {
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        margin-bottom: 10px;

    }

    .search-button-container {
        width: 105px;
    }

    .sentence-input {
        font-size: 22px !important;
    }

    .go-button {
        font-size: 22px !important;
    }

    .response-container {
        font-size: 22px;
    }

    .bg-warning {
        background-color: #cdab52 !important;
    }

    .emoji-image{
        width: 30px;
        height: 30px;
        margin-top: -4px;
    }

    .emoji-thumb{
        width: 30px;
        height: 30px;
        margin-top: -7px;
    }
    .emoji-think{
        width: 30px;
        height: 30px;
        margin-top: -5px;
    }

    .emoji-stop{
        width: 30px;
        height: 30px;
        margin-top: -5px;
    }

</style>
