<template>
  <div class="home">
    <TextToSpeech />
  </div>
</template>

<script>
// @ is an alias to /src
import TextToSpeech from '@/components/TextToSpeech.vue'

export default {
  name: 'home',
  components: {
    TextToSpeech
  }
}
</script>
