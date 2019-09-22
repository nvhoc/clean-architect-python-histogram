<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Histogram msg="Please input your url!"/>
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
