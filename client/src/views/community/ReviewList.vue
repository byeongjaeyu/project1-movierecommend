<template>
  <div>커뮤니티</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewList',
  data: function () {
    return  {
      reviewList : null,
    }
  },
  created: function () {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/`
    })
      .then(res => {
        console.log(res)
      })
  }
}
</script>

<style>

</style>