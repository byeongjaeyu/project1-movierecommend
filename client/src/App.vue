<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <p class="navbar-brand">MovieKing</p>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link :to="{ name: 'Login' }" class="nav-link">Login</router-link>
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'Signup' }" class="nav-link">Signup</router-link>
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'Logout' }" class="nav-link">Logout</router-link>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                영화추천
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li>
                  <router-link :to="{ name: 'Index' }" class="dropdown-item">Index</router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'Recommend1' }" class="dropdown-item">랜덤영화 20</router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'Recommend2' }" class="dropdown-item">추천2</router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'Recommend3' }" class="dropdown-item">추천3</router-link>
                </li>
              </ul>
            </li>
          </ul>
          <form class="d-flex">
            <input class="form-control me-2" v-model="word" type="text" placeholder="검색할 영화를 입력하세요." @input="searchMovie" @keypress.enter="searchMovie">
            <button class="btn btn-outline-success" @click="searchMovie">Search</button>
          </form>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',

  data: function () {
    return {
      word : null,
      isLogin : false,
    }
  },
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
  created: function (event) {
    const jwtToken = localStorage.getItem('jwt')
    console.log(event)
    if (jwtToken) {
      this.isLogin = true
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
