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
    <div v-for="key in this.review.comments" :key="key">
      <div class="d-flex justify-content-center">
        <div>
          {{ key.username }}&nbsp;&nbsp;
        </div>
        <div class="border" style="border:0.01px solid black; width:0.01px; height:22px;"></div>
        <div>
          &nbsp;&nbsp;{{ key.content }}
        </div>

        <div v-if="key.username===nowUser">
            &nbsp;&nbsp;<button @click="showCommentUpdateBox">Edit</button>
            &nbsp;<button @click="commentDelete($event, key.id)">X</button>
        </div>

        <br>

        <div v-if="showCommentUpdate===true">
          <input v-model="this.UpdateComment.content" type="text">
          <button  @click="commentUpdate($event, key.user)">댓글수정</button>
        </div>

      </div>
    </div>
    <create-comment :id="id"></create-comment>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import CreateComment from './CreateComment.vue'
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
      UpdateComment: {
        content:null, //v-model
        review:null, //this.id
        userid:null, //key.user
      },
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
        console.log(res.data)
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
  methods: {
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
        })
    },
    commentUpdate: function (event,user) {
      this.UpdateComment.review = this.id
      this.UpdateComment.userid = user
      axios({
        method:'put',
        url:`http://127.0.0.1:8000/community/review/${this.id}/comment/`,
        data:this.UpdateComment
      })
        .then(() => {
          this.UpdateComment = null
          this.showCommentUpdate = false
        })
    },
    showCommentUpdateBox : function () {
      this.showCommentUpdate = !this.showCommentUpdate
    }
  }
}
</script>

<style>

</style>