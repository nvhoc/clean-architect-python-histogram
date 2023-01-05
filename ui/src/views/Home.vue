<template>
  <div class="home">
    <Histogram />
  </div>
</template>

<script>
// @ is an alias to /src
import Histogram from '@/components/Histogram.vue'

export default {
  name: 'home',
  components: {
    Histogram
  }
}
</script>
