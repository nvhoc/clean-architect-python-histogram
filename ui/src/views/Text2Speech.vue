<template>
  <div class="text2speech">
    <TextToSpeech />
  </div>
</template>

<script>
// @ is an alias to /src
import TextToSpeech from '@/components/TextToSpeech.vue'

export default {
  name: 'text2speech',
  components: {
    TextToSpeech
  }
}
</script>
