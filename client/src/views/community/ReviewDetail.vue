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
          <button v-if="showEdit" @click="reviewUpdate">수정하기</button>
          <button v-if="showEdit" @click="reviewDelete">삭제하기</button>
        </tr>
      </tbody>
    </table>
    <div v-for="comment in this.commentsContents" :key="comment.id">
      {{ comment.username }}
      {{ comment.content }}
    </div>
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
      commentsContents: [],
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
        this.comments = this.review.comments
        if (this.comments) {
          for (var key in this.comments) {
            console.log(this.comments[key])
            axios({
              method:'get',
              url:`http://127.0.0.1:8000/community/comment/${this.comments[key]}/`
            })
              .then(res => {
                console.log(res.data)
                this.commentsContents.push(res.data)
              })
          }
        }
      })
        .then(() => {
          const jwtToken = localStorage.getItem('jwt')
          var decoded = jwt_decode(jwtToken)
          if (decoded.username === this.review.username) {
            this.showEdit = true
          }
        })
  },
  methods: {
    reloadDetail: function () {
      window.location.reload(`/community/${this.id}/reviewdetail`)
    },
    reviewDelete: function () {
      axios({
        method:'delete',
        url:`http://127.0.0.1:8000/community/review/${this.id}`
      })
        .then(res => {
          this.$router.push({name:'ReviewList'})
          alert(res.data.delete)
        })
    }
  }
}
</script>

<style>

</style>