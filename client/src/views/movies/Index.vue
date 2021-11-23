<template>
  <div>
    <hr>
    <div class="row row-cols-3 g-4" id="app" v-if="!searchMovies.length">
      <div v-for="movie in movies" :key="movie.pk">
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
        const titleVNode = h('div', { domProps: { innerHTML: 'Title from <i>HTML<i> string' } })
        // More complex structure
        const messageVNode = h('div', { class: ['foobar'] }, [
          h('p', { class: ['text-center'] }, [
            ' Flashy ',
            h('strong', 'msgBoxOk'),
            ' message ',
          ]),
          h('p', { class: ['text-center'] }, [h('b-spinner')]),
          h('b-img', {
            props: {
              src: movie.poster_path,
              thumbnail: true,
              center: true,
              fluid: true,
            }
          })
        ])
        // We must pass the generated VNodes as arrays
        this.$bvModal.msgBoxOk([messageVNode], {
          title: [titleVNode],
          buttonSize: 'sm',
          centered: true, size: 'sm'
        })
      }
    }
  }
</script>

<style>

</style>