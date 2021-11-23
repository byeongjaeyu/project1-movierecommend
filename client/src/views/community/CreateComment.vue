<template>
  <div>
    <div>
      <input v-model="newReview.content" type="text" class="m-1" placeholder="댓글을 입력하세요.">
      <button class="m-1" @click="createComment">작성</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'

export default {
  name: 'CreateComment',
  props: ['id'],
  data: function () {
    return {
      newReview: {
        content: null,
        review: this.id,
        user: null,
      },
    }
  },
  methods: {
    createComment: function () {
      const token = localStorage.getItem('jwt')
      var decoded = jwt_decode(token)
      this.newReview.user = decoded.username
      console.log(this.newReview)
      axios({})
    }
  }

}
</script>

<style>

</style>