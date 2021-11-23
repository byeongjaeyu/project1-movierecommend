<template>
  <div></div>
</template>

<script>
import jwt_decode from 'jwt-decode'
import axios from 'axios'

export default {
  name: 'Recommend2',
  data: function () {
    return {
      userId: null,
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    var decoded = jwt_decode(token)
    this.userId = decoded.user_id
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/movies/recommend2/',
      data: this.userId
    })
      .then(res => {
        console.log(res)
      })
  },
}
</script>

<style>

</style>