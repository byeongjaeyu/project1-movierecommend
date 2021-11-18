<template>
  <div id="app">
    <span>
      <router-link :to="{ name: 'Login' }">Login</router-link> |
      <router-link :to="{ name: 'Signup' }">Signup</router-link> |
    </span>
    <span>
      <router-link :to="{ name: 'Recommend1' }">랜덤영화 20</router-link> |
      <router-link :to="{ name: 'Recommend2' }">영화추천2</router-link> |
      <router-link :to="{ name: 'Recommend3' }">영화추천3</router-link> |
      <router-link :to="{ name: 'ReviewList' }">Community</router-link>
    </span>
    <span>
      <input type="text" v-model.trim="word" @input="searchMovie" @keyup.enter="searchMovie">
      <button @click="searchMovie"  >Search</button>
    </span>
    <index></index>
  </div>
</template>

<script>
import Index from '@/views/movies/Index'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    'Index' : Index,
  },
  data: function () {
    return {
      word : null,
    }
  },
  // created: function () {

  // },
  methods: {
    searchMovie: function () {
      if (this.word) {
        axios ({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/search/${this.word}/`
        })
          .then(res => {
            console.log(`http://127.0.0.1:8000/movies/search/${this.word}/`)
            console.log(res)
          })
      }
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
