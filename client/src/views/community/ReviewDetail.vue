<template>
  <div class="container">
    <br>
    <div class="text-start fs-4 fw-bold text-secondary">
      &nbsp;영화 리뷰
      <br>
    </div>
    <div class="border-top border-bottom border-3 bg-light p-2">
      <div class="d-flex justify-content-between">
        <div class="fs-5 fw-bold">
          [{{ review.movie_title }}] &nbsp;&nbsp;
          {{ review.title }}
        </div>
        {{ review.created_at }}
      </div>
    </div>
<<<<<<< Updated upstream
    <div class="border-bottom border-3 text-start px-2">
      {{ review.username }}
=======
    <div class="fw-bold border-bottom border-3 text-start px-2 py-1">
      작성자 : &nbsp;{{ review.username }}
>>>>>>> Stashed changes
      <br>
    </div>
    <div class='border-bottom border-3 text-start p-2'>
      <br>
      {{ review.content }}<br><br>
      <div class="border border-1 bg-secondary text-white" style="width:30%">
      {{ review.movie_title }}&nbsp;영화에&nbsp;{{ review.rank }}점을 주셨습니다.
      </div>
      <div class='d-flex justify-content-center'>
        <i class="far fa-heart"></i>&nbsp;&nbsp;
        <i class="fas fa-heart"></i>&nbsp;&nbsp;
        좋아요 10000
        <br>
      </div>
    </div>
    <div class="p-2 d-flex justify-content-end">
      <button id="btn-edit" v-if="showEdit" @click="reviewUpdate"><i class="fas fa-edit"></i></button>
      <button id="btn-delete" v-if="showEdit" @click="reviewDelete"><i class="far fa-trash-alt"></i></button>
    </div>
    

    <div class="p-2 bg-light border border-1 rounded-pill">
        댓글 {{review.comments.length}} 개
        <br>
    </div>
    
    <div v-for="key in review.comments" :key="key" class="pt-3">
      <div>
        <div class="d-flex justify-content-center align-content-center">
          <div class="border rounded-pill ps-2 py-1 bg-light">
            {{ key.username }}&nbsp;&nbsp;
          </div>
          <!-- <div class="border" style="background-color:black; border:0.1px solid black; width:0.1px; height:22px;"></div> -->
          <div class="py-1" :id="key.id" v-if="!(selectedComment==key.id)">
            &nbsp;&nbsp;{{ key.content }}
          </div>
<<<<<<< Updated upstream
          <div v-if="key.username === nowUser">
=======
          <span class="py-1" :id="key.id" v-if="showCommentUpdate && selectedComment==key.id">
            <input v-model="UpdateComment.content" type="text" :placeholder="key.content">
            <button  @click="commentUpdate($event, key.user, key.id)"><i class="fas fa-check"></i></button>
          </span>
          <div class="d-flex py-1" v-if="key.username === nowUser">
>>>>>>> Stashed changes
            &nbsp;&nbsp;<div :id="key.id" @click="showCommentUpdateBox(key.id)"><i  class="fas fa-edit"></i></div>
            &nbsp;<div @click="commentDelete($event, key.id)"><i  class="far fa-trash-alt"></i></div>
          </div>
        </div>
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
          this.selectedComment = null
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
<<<<<<< Updated upstream
=======
      if (this.showCommentUpdate === false) {
        this.selectedComment = null
      }
>>>>>>> Stashed changes
    },
  },
}
</script>

<style>
  #btn-edit{
    margin-right:3px;
    margin-left:3px;
    padding: 5px;
    background-color: white;
    border:2px solid rgb(21, 218, 87);
  }
  #btn-delete{
    margin-right:3px;
    margin-left:3px;
    padding: 5px;
    background-color: white;
    border:2px solid rgb(228, 14, 67);
  }
</style>