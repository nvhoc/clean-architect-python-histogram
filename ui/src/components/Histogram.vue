<template>
  <div class="histogram">
    <h1>{{msg}}</h1>
    <b-container class="bv-example-row">
      <b-row align-h="center">
        <b-form @submit="onSubmit" @reset="onReset"  cols="6">
          <b-form-group
            id="input-group-1"
            label="URL:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="form.url"
              type="url"
              required
              placeholder="Enter URL"
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
      </b-row>
    </b-container>
    <div v-if="items"> 
       <b-table striped hover :items="items"></b-table>
    </div>  
  </div>
</template>

<script>
export default {
  name: 'Histogram',
  props: {
    msg: String
  },
  data() {
      return {
        form: {
          url: ''
        },
        items: null,
      }
  },
   methods: {
      onSubmit(evt) {
        evt.preventDefault()
        this.axios.get(`/histogram-sv/v1/internal/web/unique_words?url=${this.form.url}`)
        .then(response => (this.items = response.data))
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.url = ''
      }
    }
}
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
</style>
