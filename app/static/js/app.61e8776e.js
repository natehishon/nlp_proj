(function(e){function t(t){for(var r,o,c=t[0],i=t[1],u=t[2],p=0,m=[];p<c.length;p++)o=c[p],Object.prototype.hasOwnProperty.call(a,o)&&a[o]&&m.push(a[o][0]),a[o]=0;for(r in i)Object.prototype.hasOwnProperty.call(i,r)&&(e[r]=i[r]);l&&l(t);while(m.length)m.shift()();return s.push.apply(s,u||[]),n()}function n(){for(var e,t=0;t<s.length;t++){for(var n=s[t],r=!0,c=1;c<n.length;c++){var i=n[c];0!==a[i]&&(r=!1)}r&&(s.splice(t--,1),e=o(o.s=n[0]))}return e}var r={},a={app:0},s=[];function o(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,o),n.l=!0,n.exports}o.m=e,o.c=r,o.d=function(e,t,n){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},o.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)o.d(n,r,function(t){return e[t]}.bind(null,r));return n},o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="/";var c=window["webpackJsonp"]=window["webpackJsonp"]||[],i=c.push.bind(c);c.push=t,c=c.slice();for(var u=0;u<c.length;u++)t(c[u]);var l=i;s.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"353b":function(e,t,n){"use strict";n("d33d")},"408c":function(e,t,n){"use strict";n("870e")},"56d7":function(e,t,n){"use strict";n.r(t);n("cadf"),n("551c"),n("f751"),n("097d");var r=n("2b0e"),a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("router-view"),n("span",{staticClass:"main-title"},[e._v("Is It Sarcasm?")]),n("br"),n("br"),n("b-container",{staticClass:"parent-container"},[n("b-row",[n("b-col",{attrs:{sm:"6","offset-sm":"3"}},[n("b-form",{staticClass:"sentence-form",on:{submit:function(t){return t.preventDefault(),e.submit(t)}}},[n("b-form-group",[n("div",{staticClass:"search-form-container"},[n("b-input",{staticClass:"mb-2 ml-2 mr-sm-2 mb-sm-0 sentence-input",attrs:{placeholder:"try a sentence"},model:{value:e.form.input,callback:function(t){e.$set(e.form,"input",t)},expression:"form.input"}}),n("b-button",{staticClass:"go-button",staticStyle:{width:"130px"},attrs:{size:"md",variant:"info"},on:{click:function(t){return e.submit()}}},[n("i",{staticClass:"fas fa-search"}),e._v(" go!\n                                ")])],1)])],1)],1)],1),n("br"),n("br"),n("b-row",[n("b-col",{attrs:{sm:"12"}},[e.loading?n("b-spinner",{staticStyle:{width:"5rem",height:"5rem"},attrs:{variant:"info",label:"Spinning"}}):e._e(),e.response?n("div",{staticClass:"response-container"},[n("b-card-group",{attrs:{deck:""}},[n("b-card",{staticClass:"text-center",attrs:{"header-html":"Sarcasm Score <img style='display:inline-block' class='emoji-image' src='https://cdn.shopify.com/s/files/1/1061/1924/files/Upside-Down_Face_Emoji.png?9898922749706957214'></img>","header-bg-variant":"info","header-text-variant":"white"}},[n("b-card-text",[n("v-runtime-template",{attrs:{template:"<span>"+e.score+"</span>"}})],1)],1),n("b-card",{staticClass:"text-center",attrs:{"header-html":"Sentiment Score <img style='display:inline-block' class='emoji-thumb' src='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/279/thumbs-up_1f44d.png'></img>","header-bg-variant":"info","header-text-variant":"white"}},[n("b-card-text",[n("v-runtime-template",{attrs:{template:"<span>"+e.senti+"</span>"}})],1)],1),n("b-card",{staticClass:"text-center",attrs:{"header-html":"Feature Importance <img style='display:inline-block' class='emoji-think' src='https://www.dictionary.com/e/wp-content/uploads/2018/03/Thinking_Face_Emoji-Emoji-Island.png'></img>","header-bg-variant":"info","header-text-variant":"white"}},[n("b-card-text",[n("v-runtime-template",{attrs:{template:"<span>"+e.msg+"</span>"}})],1)],1)],1)],1):e._e()],1)],1),n("br"),n("br"),n("b-row",[n("b-col",{attrs:{sm:"6","offset-sm":"3"}},[e.response?n("div",{staticClass:"response-container"},[n("b-card-group",{attrs:{deck:""}},[e.type1?n("b-card",{staticClass:"text-center",attrs:{"header-html":"Recommendation: <img style='display:inline-block' class='emoji-image' src='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/279/check-mark-button_2705.png'></img>","header-bg-variant":"success","header-text-variant":"white"}},[n("b-card-text",[n("span",[e._v("We rate this as positive and not very sarcastic, hooray!")])])],1):e._e(),e.type2?n("b-card",{staticClass:"text-center",attrs:{"header-html":"Recommendation: <img style='display:inline-block' class='emoji-stop' src='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/microsoft/209/cross-mark_274c.png'></img>","header-bg-variant":"danger","header-text-variant":"white"}},[n("b-card-text",[n("span",[e._v("We rate this as positive but pretty sarcastic, proceed with caution!")])])],1):e._e(),e.type3?n("b-card",{staticClass:"text-center",attrs:{"header-html":"Recommendation: <img style='display:inline-block' class='emoji-stop' src='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/microsoft/209/cross-mark_274c.png'></img>","header-bg-variant":"danger","header-text-variant":"white"}},[n("b-card-text",[n("span",[e._v("We rate this as negative and not very sarcastic, boo!")])])],1):e._e(),e.type4?n("b-card",{staticClass:"text-center",attrs:{"header-html":"Recommendation: <img style='display:inline-block' class='emoji-image' src='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/279/check-mark-button_2705.png'></img>","header-bg-variant":"success","header-text-variant":"white"}},[n("b-card-text",[n("span",[e._v("We rate this as negative but pretty sarcastic, proceed with optimism!")])])],1):e._e()],1)],1):e._e()])],1)],1)],1)},s=[],o=n("bc3a"),c=n.n(o),i=c.a.create({baseURL:"/api/",timeout:1e6,headers:{"Content-Type":"application/json"}});i.interceptors.request.use((function(e){return e.headers["Authorization"]="Fake Token",e})),i.interceptors.response.use((function(e){return e}),(function(e){return console.log(e),Promise.reject(e)}));var u={fetchResource:function(){return i.get("resource/1").then((function(e){return e.data}))},postResource:function(e){return i.post("resource/1",{sentence:e}).then((function(e){return e.data}))},fetchSecureResource:function(){return i.get("secure-resource/zzz").then((function(e){return e.data}))}},l=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("button",{staticClass:"Button",on:{click:e.onClick}},[e._t("default",[e._v(" Button ")])],2)},p=[],m={props:{onClick:{type:Function,required:!0}}},d=m,f=(n("353b"),n("2877")),h=Object(f["a"])(d,l,p,!1,null,"43cd99a0",null),b=h.exports,v=n("dd1e"),g=n("205f"),y=n("5cce"),_={name:"app",data:function(){return{loading:!1,response:!1,type1:!1,type2:!1,type3:!1,type4:!1,msg:"",score:"",senti:"",form:{input:""}}},components:{"v-button":b,VRuntimeTemplate:v["a"],BCard:g["a"],BCardGroup:y["a"]},methods:{alertClick:function(){alert("button clicked")},faker:function(){return null},submit:function(){var e=this;console.log("SUB"),this.loading=!0,this.response=!1,u.postResource(this.form.input).then((function(t){e.type1=!1,e.type2=!1,e.type3=!1,e.type4=!1,e.loading=!1,e.response=!0,e.msg=t.sentence,e.score=t.predict,e.senti=t.sentiment.label+" "+t.sentiment.score;var n=parseInt(e.score);n<50&&"POSITIVE"===t.sentiment.label&&(e.type1=!0),n>49&&"POSITIVE"===t.sentiment.label&&(e.type2=!0),n<50&&"NEGATIVE"===t.sentiment.label&&(e.type3=!0),n>49&&"NEGATIVE"===t.sentiment.label&&(e.type4=!0)})).catch((function(t){e.error=t.message}))}}},w=_,k=(n("5c0b"),Object(f["a"])(w,a,s,!1,null,null,null)),x=k.exports,j=n("8c4f"),C=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"hello"},[n("h1",[e._v(e._s(e.msg))])])},S=[],R={name:"HelloWorld",data:function(){return{msg:""}},methods:{fetchResource:function(){var e=this;u.fetchResource().then((function(t){e.msg=t})).catch((function(t){e.error=t.message}))}}},O=R,T=(n("408c"),Object(f["a"])(O,C,S,!1,null,"15e0be23",null)),E=T.exports,I=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"about"},[n("h1",[e._v("Backend Resources Demo")]),n("p",[e._v("Click on the links below to fetch data from the Flask server")]),n("a",{attrs:{href:""},on:{click:function(t){return t.preventDefault(),e.fetchResource(t)}}},[e._v("Fetch")]),n("br"),n("a",{attrs:{href:""},on:{click:function(t){return t.preventDefault(),e.fetchSecureResource(t)}}},[e._v("Fetch Secure Resource")]),n("h4",[e._v("Results")]),e._l(e.resources,(function(t){return n("p",{key:t.timestamp},[e._v("\n    Server Timestamp: "+e._s(e._f("formatTimestamp")(t.timestamp))+"\n  ")])})),n("p",[e._v(e._s(e.error))])],2)},z=[],P={name:"about",data:function(){return{resources:[],error:""}},methods:{fetchResource:function(){var e=this;u.fetchResource().then((function(t){e.resources.push(t)})).catch((function(t){e.error=t.message}))},fetchSecureResource:function(){var e=this;u.fetchSecureResource().then((function(t){e.resources.push(t)})).catch((function(t){e.error=t.message}))}}},F=P,B=Object(f["a"])(F,I,z,!1,null,null,null),D=B.exports;r["default"].use(j["a"]);var $=new j["a"]({routes:[{path:"/",name:"home",component:E},{path:"/api",name:"api",component:D}]}),V=n("2f62");r["default"].use(V["a"]);var W=new V["a"].Store({state:{},mutations:{},actions:{}}),M=n("5f5b"),U=n("b1e0"),A=(n("456d"),n("ac6a"),{formatTimestamp:function(e){var t=new Date(e);return t.toLocaleTimeString("en-US")}});Object.keys(A).forEach((function(e){r["default"].filter(e,A[e])}));n("f9e3"),n("2dd8");r["default"].use(M["a"]),r["default"].use(U["a"]),r["default"].config.productionTip=!1,new r["default"]({router:$,store:W,render:function(e){return e(x)}}).$mount("#app")},"5c0b":function(e,t,n){"use strict";n("5e27")},"5e27":function(e,t,n){},"870e":function(e,t,n){},d33d:function(e,t,n){}});
//# sourceMappingURL=app.61e8776e.js.map