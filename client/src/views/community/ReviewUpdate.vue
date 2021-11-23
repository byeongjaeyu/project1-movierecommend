<template>
  <div>
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">리뷰 제목</label>
      <input v-model="updateReview.title" type="text" class="form-control" id="exampleFormControlInput1" :placeholder="this.oldReviewTitle">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">영화 제목</label>
      <input v-model="updateReview.movie_title" type="text" class="form-control" id="exampleFormControlInput1" :placeholder="this.oldReviewMovieTitle">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label">내용</label>
      <textarea v-model="updateReview.content" class="form-control" id="exampleFormControlTextarea1" rows="3" :placeholder="this.oldReviewContent"></textarea>
    </div>
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label">점수</label>
      <input v-model="updateReview.rank" type='number' :placeholder="this.oldReviewRank">
    </div>
    <div class="mb-3">
      <button @click="UpdateReview">리뷰 수정</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'ReviewUpdate',
  data: function () {
    return {
      reviewId : this.$route.params.reviewid,
      oldReviewTitle : this.$route.params.oldReviewTitle,
      oldReviewMovieTitle : this.$route.params.oldReviewMovieTitle,
      oldReviewContent : this.$route.params.oldReviewContent,
      oldReviewRank : this.$route.params.oldReviewRank,
      oldReviewUser : this.$route.params.oldReviewUser,
      oldReviewLikeUser : this.$route.params.oldReviewLikeUser,
      updateReview : {
        title:null,
        movie_title:null,
        content:null,
        rank:null,
        user:null,
        like_user:null,
      },
    }
  },
  methods: {
    UpdateReview: function () {
      this.updateReview.user = this.oldReviewUser,
      this.updateReview.like_user = this.oldReviewLikeUser
      axios({
        method:'put',
        url:`http://127.0.0.1:8000/community/review/${this.reviewId}/`,
        data:this.updateReview,
      })
        .then(() => {
          this.$router.push({name:'ReviewDetail',params:{reviewid:this.reviewId}})
        })
        .catch(() => {
          console.log(this.updateReview)
        })
    }
  }
}
</script>

<style>

</style>