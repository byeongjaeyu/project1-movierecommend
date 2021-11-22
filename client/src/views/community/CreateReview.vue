<template>
  <div>
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">리뷰 제목</label>
      <input v-model="newReview.title" type="text" class="form-control" id="exampleFormControlInput1" placeholder="title">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">영화 제목</label>
      <input v-model="newReview.movie_title" type="text" class="form-control" id="exampleFormControlInput1" placeholder="movie_title">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label">내용</label>
      <textarea v-model="newReview.content" class="form-control" id="exampleFormControlTextarea1" rows="3" placeholder="content"></textarea>
    </div>
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label">점수</label>
      <input v-model="newReview.rank" type='number' placeholder="rank">
    </div>
    <div class="mb-3">
      <button @click="CreateReview">리뷰 작성</button>
    </div>
  </div>
</template>

<script>
import jwt_decode from 'jwt-decode'
import axios from 'axios'

export default {
  name: 'CreateReview',
  data: function () {
    return {
      newReview: {
        user : null,
        title: null,
        movie_title: null,
        content: null,
        rank: null,
      }
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
    CreateReview: function () {
      const jwtToken = localStorage.getItem('jwt')
      var decoded = jwt_decode(jwtToken)
      console.log(decoded)
      this.newReview.user = decoded.user_id
      this.newReview.rank = Number(this.newReview.rank)
      if (this.newReview.title && this.newReview.movie_title && this.newReview.user && this.newReview.content && this.newReview.rank) {
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/community/review/',
        data: this.newReview,
        headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            this.$router.push({ name: 'ReviewList' })
          })
      } else {
        alert("빈칸 채워라.");
      }
      
      },
    }
}
</script>

<style>

</style>