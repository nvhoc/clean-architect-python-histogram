<template>
  <div class="home">
    <Histogram msg="Please input your url to get histogram!"/>
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
