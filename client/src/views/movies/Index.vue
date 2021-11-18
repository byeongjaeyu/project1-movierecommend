<template>
  <div id="app">
    <h1>최신영화20개</h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Index',
  created: function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/'
    })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style>

</style>