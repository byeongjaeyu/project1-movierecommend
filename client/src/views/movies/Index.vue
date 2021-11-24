<template>
  <div>
    <hr>
    <div class="row row-cols-3 g-4" id="app" v-if="!searchMovies.length">
      <div v-for="movie in movies" :key="movie.pk">
          <div class="col">
            <div class="card" @click="showModal(movie)">
              <img :src="movie.poster_path" class="card-img-top" alt="..." >
              <div class="card-body">
                <h5 class="card-title fw-bold">{{ movie.title }}</h5>
              </div>
            </div>
        </div>
      </div>
    </div>
    <div class="row row-cols-3 g-4" id="app" v-else>
      <div v-for="movie in searchMovies" :key="movie.pk">
          <div class="col">
            <div class="card" @click="showMsgOk(movie)">
              <img :src="movie.poster_path" class="card-img-top" alt="..." >
              <div class="card-body">
                <h5 class="card-title fw-bold">{{ movie.title }}</h5>
              </div>
            </div>
        </div>
      </div>
    </div>

    <b-modal ref="movieModal" hide-footer title='test'>
      <div class="text-center">
        <div>
        <img width="400" height="600" src="https://image.tmdb.org/t/p/original//1Lh9LER4xRQ3INFFi2dfS2hpRwv.jpg" alt="">
        </div>
        <div>
          줄거리
        </div>
        <div>
        <iframe width="400" height="300" src="https://www.youtube.com/embed/uiIIyepK6XY" frameborder="0">트레일러 영상이 없어요.</iframe>
        </div>
      </div>
    </b-modal>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Index',
  props: {
    searchMovies: Array
  },
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
    methods : {
    showMsgOk: function(movie) {
        const h = this.$createElement
        // Using HTML string
        const titleVNode = h('div', { domProps: { innerHTML: movie.title } })
        // More complex structure
        const messageVNode = h('div', { class: ['foobar'] }, [
          h('b-img', {
            props: {
              src: movie.poster_path,
              thumbnail: true,
              center: true,
              fluid: true,
            }
          }),
          h('br'),
          h('p', { class: ['text-center'] }, [
            movie.overview, 
          ]),
          h('p', {class : ['text-center']},[
            movie.youtube_url,
          ]),
        ])
        // We must pass the generated VNodes as arrays
        this.$bvModal.msgBoxOk([messageVNode], {
          title: [titleVNode],
          buttonSize: 'sm',
          centered: true, size: 'md'
        })
      },
      showModal() {
        this.$refs['movieModal'].show()
      }
    }
  }
</script>

<style>

</style>