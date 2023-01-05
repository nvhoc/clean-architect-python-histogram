<template>
  <div class="Image2Text">
    <h1>{{msg}}</h1>
    <b-container class="bv-example-row">
      <h3>Upload</h3>
      <textarea @paste="onPaste"></textarea>
      <b-row align-h="center">
        <img :src="getImgUrl()" v-bind:alt="paste" width="200" height="200" />
      </b-row>
    </b-container>
    <b-container class="bv-example-row">
       <h3>Text</h3>
        <b-textarea v-model="output"/>
    </b-container>  
  </div>
</template>

<script>

import Tesseract from 'tesseract.js';


export default {
  name: 'Image2Text',
  components: {
  },
  props: {
    msg: String
  },
    data() {
      return {
        file_upload: null,
        upload_src: '',
        items: null,
        output:''
      }
  },
   methods: {
      onPaste(e) {
        e.preventDefault();
        const self = this;
        if (e.clipboardData.files.length) {
          const file = e.clipboardData.files[0];
          var reader  = new FileReader();
          reader.onload = function(e)  {
              const src = e.target.result;
              self.upload_src =  src;
              self.file_upload = file;

              Tesseract.recognize(
                src,
                'eng',
                 { logger: m => console.log(m) }
              ).then(({ data: { text } }) => {
                self.output = text
              })
          }
          reader.readAsDataURL(file);

        } else {
          alert(
            "No image data was found in your clipboard. Copy an image first or take a screenshot."
          );
        }
      },
     getImgUrl() {
       return this.upload_src
     }
    }
}
</script>