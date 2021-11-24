<template>
  <div class="container p-2" style="width:50%">
    <br>
    <div class="mb-3 text-start">
      <label for="exampleFormControlInput1" class="form-label fs-5 fw-bold">리뷰 제목</label>
      <input v-model="newReview.title" type="text" class="form-control" id="exampleFormControlInput1" placeholder="ex) 와 이 영화 재밌네요!">
    </div>
    <div class="mb-3 text-start">
      <label for="exampleFormControlInput1" class="form-label fs-5 fw-bold">영화 제목</label>
      <input @input="searchMovie" v-model="newReview.movie_title" type="text" class="form-control" id="exampleFormControlInput1" placeholder="ex) 신세계">
    </div>
    <div class="mb-3 text-start">
      <label for="exampleFormControlTextarea1" class="form-label fs-5 fw-bold">내용</label>
      <textarea v-model="newReview.content" class="form-control" id="exampleFormControlTextarea1" rows="3" placeholder="ex) 꼭 보세요 댓글로 소통해요!"></textarea>
    </div>
    <div>
      <div class="mb-3 text-start d-flex justify-content-between">
        <div>
          <label for="exampleFormControlTextarea1" class="form-label fs-5 fw-bold">점수</label>
          &nbsp;
          <input v-model="newReview.rank" type='number' placeholder="ex) 100">
        </div>
        <button @click="CreateReview" class="bg-white"><i class="fas fa-plus"></i></button>
      </div>
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
      word : null,
      searchMovies : [],
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
    searchMovie: function () {
      if (this.newReview.movie_title) {
        axios ({
          method: 'get',
          url : `http://127.0.0.1:8000/movies/search/${this.newReview.movie_title}/`
        })
          .then(res => {
            this.searchMovie = []
            for (const movie in res.data) {
              console.log(movie)
              this.searchMovie.push(movie.title)
            }
          })
      }
    },
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
      this.newReview.user = decoded.user_id
      this.newReview.rank = Number(this.newReview.rank)
      console.log(this.newReview)
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