<template>
  <div>
    <hr>
    <div class="row row-cols-3 g-4" id="app">

      <div v-for="movie in movies" :key="movie.pk">

          <div class="col">

            <div class="card" @click="showMsgOk(movie)">
              <img :src="movie.poster_path" @error="replaceByDefault" class="card-img-top" alt="...">
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

  name: 'Recommend1',
  data: function () {
    return {
      movies : [],
    }
  },
  created: function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/recommend1/'
    })
      .then(res => {
        this.movies = res.data
        console.log(this.movies)
      })
      .catch(err => {
        console.log(err)
      })
  },
  methods: {
    replaceByDefault(e) {
      e.target.src = require("../../assets/Default.png")
  },
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
        ])
        // We must pass the generated VNodes as arrays
        this.$bvModal.msgBoxOk([messageVNode], {
          title: [titleVNode],
          buttonSize: 'sm',
          centered: true, size: 'md'
        })
      }
    }
}
</script>

<style>

</style>