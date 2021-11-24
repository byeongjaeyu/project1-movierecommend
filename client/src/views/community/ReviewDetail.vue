<template>
  <div>
    <table class="table">
      <thead>
      </thead>
      <tbody>
        <tr>
          <td>{{ review.title }}</td>
        </tr>
        <tr>
          <td>{{ review.movie_title }}</td>
        </tr>
        <tr>
          <td>{{ review.rank }}</td>
        </tr>
        <tr>
          <td>{{ review.content }}</td>
        </tr>
        <tr>
          <button v-if="showEdit" @click="reviewUpdate">수정하기</button>
          <button v-if="showEdit" @click="reviewDelete">삭제하기</button>
        </tr>
      </tbody>
    </table>
    <div v-for="key in review.comments" :key="key">
      <div class="">
        <div class="d-flex justify-content-center">
          <div>
            {{ key.username }}&nbsp;&nbsp;
          </div>
          <div class="border" style="border:0.01px solid black; width:0.01px; height:22px;"></div>
          <div>
            &nbsp;&nbsp;{{ key.content }}
          </div>
          <div v-if="key.username === nowUser">
            &nbsp;&nbsp;<button :id="key.id" @click="showCommentUpdateBox(key.id)">Edit</button>
            &nbsp;<button @click="commentDelete($event, key.id)">X</button>
          </div>
        </div>

        <span :id="key.id" v-if="showCommentUpdate && selectedComment==key.id">
          <input v-model="UpdateComment.content" type="text">
          <button  @click="commentUpdate($event, key.user, key.id)">댓글수정</button>
        </span>

      </div>
    </div>
    <create-comment :id="id" @commentComplete="commentComplete"></create-comment>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import CreateComment from './CreateComment.vue'
// import $ from 'jquery'
// import ReviewUpdate from './ReviewUpdate.vue'

export default {
  components: { CreateComment },
  name: 'ReviewDetail',
  data: function () {
    return {
      id : this.$route.params.reviewid,
      nowUser : null,
      review: null,
      showEdit: false,
      showCommentEdit: false,
      showCommentUpdate: false,
      selectedComment:null,
      UpdateComment: {
        content:null, //v-model
        review:null, //this.id
        user:null, //key.user
      },
    }
  },
  props: {
    reviewid : Number,
  },
  created: function () {
    this.getComment()
  },
  methods: {
    getComment: function () {
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
          this.nowUser = decoded.username
          if (decoded.user_id === this.review.user) {
            this.showEdit = true
          }
        })
    },
    reloadDetail: function () {
      window.location.reload(`/community/${this.id}/reviewdetail`)
    },
    reviewDelete: function () {
      axios({
        method:'delete',
        url:`http://127.0.0.1:8000/community/review/${this.id}`
      })
        .then(() => {
          this.$router.push({name:'ReviewList'})
          alert(`${this.id}번 게시글이 삭제됐습니다.`)
          this.getComment()
        })
    },
    reviewUpdate: function () {
      this.$router.push({
        name:'ReviewUpdate', 
        params:{
          reviewid:this.id,
          oldReviewTitle:this.review.title,
          oldReviewMovieTitle:this.review.movie_title,
          oldReviewContent:this.review.content,
          oldReviewRank:this.review.rank,
          oldReviewUser:this.review.user,
          oldReviewLikeUser : this.review.like_user,
          }
        })
    },
    commentDelete: function (event,id) {
      axios({
        method:'delete',
        url:`http://127.0.0.1:8000/community/comment/${id}/`
      })
        .then(() => {
          this.$router.push({name:'ReviewDetail',params:{reviewid:this.id}})
          alert('댓글이 삭제됐습니다.')
          this.getComment()
        })
    },
    commentUpdate: function (event,user,commentId) {
      this.UpdateComment.review = this.id
      this.UpdateComment.user = user
      console.log(this.id)
      axios({
        method:'put',
        url:`http://127.0.0.1:8000/community/comment/${commentId}/`,
        data:this.UpdateComment
      })
        .then(() => {
          this.UpdateComment.content = null
          this.showCommentUpdate = false
          this.getComment()
        })
    },
    commentComplete: function () {
      this.getComment()
    },
    showCommentUpdateBox : function(id) {
      // console.log(id)
      this.showCommentUpdate = !this.showCommentUpdate
      this.selectedComment = id
    },
  },
}
</script>

<style>

</style>