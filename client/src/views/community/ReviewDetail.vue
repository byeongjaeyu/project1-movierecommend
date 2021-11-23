<template>
  <div>
    <table class="table">
      <thead>
      </thead>
      <tbody>
        <tr>
          <td>{{ this.review.title }}</td>
        </tr>
        <tr>
          <td>{{ this.review.movie_title }}</td>
        </tr>
        <tr>
          <td>{{ this.review.rank }}</td>
        </tr>
        <tr>
          <td>{{ this.review.content }}</td>
        </tr>
        <tr>
          <button v-if="showEdit">수정하기</button>
          <button v-if="showEdit">삭제하기</button>
        </tr>
      </tbody>
    </table>
    <create-comment :id="id"></create-comment>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import CreateComment from './CreateComment.vue'

export default {
  components: { CreateComment },
  name: 'ReviewDetail',
  data: function () {
    return {
      id : this.$route.params.reviewid,
      review: null,
      showEdit: false,
      comments: null,
    }
  },
  props: {
    reviewid : Number,
  },
  created: function () {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/review/${this.id}`
    })
      .then(res => {
        // console.log(res.data)
        this.review = res.data
      })
        .then(() => {
          const jwtToken = localStorage.getItem('jwt')
          var decoded = jwt_decode(jwtToken)
          if (decoded.username === this.review.username) {
            this.showEdit = true
          }
        })
        .then(() => {
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/community/review/${this.id}/comment`
          })
            .then((res) => {
              console.log(res)
              this.comments = res.data
            })
        })
  }
}
</script>

<style>

</style>
