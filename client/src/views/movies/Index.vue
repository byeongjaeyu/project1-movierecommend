<template>
  <div id="app">
    <h1>최신영화20개</h1>
    <div>
      <div v-for="movie in movies" :key="movie.movie_id">
        {{ movie.title }}
        <img :src="movie.poster_path" alt="">
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Index',
  data: function () {
    return {
      movies : [],
    }
  },
  created: function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/'
    })
      .then(res => {
        this.movies = res.data
        console.log(this.movies)
      })
      .catch(err => {
        console.log(err)
      })
  },
}
</script>

<style>
  img {
    width: 300px;
    height: 150px;
    
  }
</style>