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
      userId: {
        id: null
      },
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    var decoded = jwt_decode(token)
    this.userId.id = decoded.user_id
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/movies/recommend2/',
      data: this.userId.id,
      headers:this.setToken()
    })
      .then(res => {
        console.log(res)
      })
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
        }
      return config
    }
  },
}
</script>

<style>

</style>
