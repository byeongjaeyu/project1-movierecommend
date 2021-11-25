<template>
  <div>
    <div>
      <input v-model="newReview.content" type="text" class="m-1" placeholder="댓글을 입력하세요.">
      <button class="m-1 bg-white" @click="createComment">작성</button>
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
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createComment: function () {
      const token = localStorage.getItem('jwt')
      var decoded = jwt_decode(token)
      console.log(decoded)
      this.newReview.user = decoded.user_id
      console.log(this.newReview)
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/community/review/${this.id}/comment/`,
        headers: this.setToken(),
        data: this.newReview,
      })
        .then(() => {
          this.newReview.content=null
          this.$emit('commentComplete')
        })
    }
  }

}
</script>

<style>

</style>
