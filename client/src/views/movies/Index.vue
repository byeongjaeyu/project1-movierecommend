<template>
  <div>
    <hr>
    <div class="row row-cols-3 g-4" id="app">

      <div v-for="movie in movies" :key="movie.movie_id">

          <div class="col">

            <div class="card">
              <img :src="movie.poster_path" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title fw-bold">{{ movie.title }}</h5>
              </div>
            </div>
          

        </div>

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

</style>