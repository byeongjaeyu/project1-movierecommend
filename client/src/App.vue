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
    <index></index>
  </div>
</template>

<script>
import Index from '@/views/movies/Index'

export default {
  name: 'App',
  components: {
    'Index' : Index,
  },
  // data: function () {
  //   return {}
  // },
  // created: function () {

  // },
  // methods: {

  // },
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
