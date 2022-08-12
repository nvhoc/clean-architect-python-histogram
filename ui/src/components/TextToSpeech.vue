<template>
  <div class="text2Speech">
    <h1>{{msg}}</h1>
    <b-container class="bv-example-row">
      
      <v-select v-model="form.voice" :options="voices" />

      <b-textarea v-model="form.text"></b-textarea>
      <b-input v-model="form.rate" type="number" step="0.1" />
      <b-button @click="speakByForm">Speak</b-button>
    </b-container>
    <b-container class="bv-example-row">
      <h3>speak list</h3>
      <!-- <div v-for="item in items" :key="item.text" class="text2speech-clicked-span" @click="checkRandomizeText(item.text)">
          {{item.text}}
      </div>-->
      <b-textarea v-model="randomFormText[0]"></b-textarea>
      <div v-if="showResult">{{currentText[0]}}</div>
      <b-button @click="randomizedSpeak(0)">Randomize</b-button>
      <b-button @click="repeat(0)">Repeat</b-button>
      <b-button @click="checkRandomizeText(randomFormText, 0)">Check</b-button>
    </b-container>
    <b-container class="bv-example-row">
      <span>{{passed[0]}}</span>
    </b-container>
    <b-container class="bv-example-row">
      <h3>Test what you learned</h3>
      <b-textarea v-model="randomFormText[1]"></b-textarea>
      <div v-if="showResult">{{currentText[1]}}</div>
      <b-button @click="randomizedSpeak(1)">Randomize</b-button>
      <b-button @click="repeat(1)">Repeat</b-button>
      <b-button @click="checkRandomizeText(randomFormText, 1)">Check</b-button>
    </b-container>
        <b-container class="bv-example-row">
      <span>{{passed[1]}}</span>
    </b-container>
  </div>
</template>

<script>
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}
import commonWords from "@/components/Text2Speech/5000words.json";
import Vue from 'vue'
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';


Vue.component('v-select', vSelect)


export default {
  name: "Text2Speech",
  props: {
    msg: String
  },
  data() {
    if (!window.localStorage.passedTextList) {
      window.localStorage.passedTextList = [[]]
    }
    const passedTextList = window.localStorage.passedTextList
    return {
      voices: ['Australian Male','Australian Female', 'UK English Male'],
      form: {
        text: "",
        rate: 1.3,
        voice: "Australian Male"
      },
      items: [
        { text: "tell me about your self?" },
        { text: "Why did you apply for this job?" },
        {
          text:
            "What experience do you have that would be relevant to this role?"
        },
        { text: "Why did you decide to apply to this role?" },
        { text: "Tell me about your experience in" },
        { text: "What did you like most about the job description?" },
        { text: "Why are you leaving your current job?" },
        { text: "Why did you leave your previous job?" },
        { text: "What do you know about our company’s product?" },
        {
          text:
            "Describe the workplace where you’ll be most happy and productive"
        },
        { text: "What are your salary expectations?" },
        { text: "What kind of visa have you had?" }
      ],
      resources: [commonWords.map(i => i.split(",").map(j => j.trim())), passedTextList],
      currentText: ["",""],
      randomFormText: ["", ""],
      passed:[window.localStorage.passedTextList, [[]]],
      showResult: false
    };
  },
  methods: {
    speak(text) {
      window.responsiveVoice.speak(text, this.form.voice, {
        rate: this.form.rate
      });
    },
    speakByForm() {
      this.speak(this.form.text)
    },
    checkRandomizeText(randomFormText, passedIndex) {
      const currentRandText = this.currentText[passedIndex]
      const currnetAnswerText = randomFormText[passedIndex];
      if (currnetAnswerText.toLowerCase() === this.currentText[passedIndex].toLowerCase()) {
        this.speak("correct");
        this.passed[passedIndex][0].push(currentRandText)
        this.randomizedSpeak(passedIndex)
        return;
      }
      this.speak("wrong");
      this.showResult = true;
      setTimeout(() => {
        this.showResult = false;
      }, 5000);
    },
    repeat(passedIndex) {
      this.speak(this.currentText[passedIndex]);
    },
    randomizedSpeak(passedIndex) {
      let speakText = "";
      const randomResource = this.resources[passedIndex]
      while (speakText === "" && randomResource.length > 0) {
        const i = getRandomInt(randomResource.length);
        const unit = randomResource[i];
        if (unit.length === 0) {
          randomResource.splice(i, 1);
          continue;
        }
        speakText = unit.splice(getRandomInt(unit.length), 1)[0];
      }
      if (randomResource.length == 0 && speakText === '') {
        alert('done')
        return;
      }
      this.currentText[passedIndex] = speakText;
      this.speak(speakText);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
.text2speech-clicked-span {
  cursor: pointer;
}
</style>
