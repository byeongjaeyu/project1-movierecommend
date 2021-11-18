<template>
  <div id="app" class="container ">
    <nav class="navbar navbar-expand-lg navbar-light bg-dark font sticky-top">
      <div class="container-fluid">
        <p class="navbar-brand fw-bold text-white-50 m-auto">
          <router-link :to="{ name: 'Index' }" class="text-decoration-none text-white-50">
            <img src="https://fontmeme.com/permalink/211118/4236136457f6822dd292086626451371.png">
          </router-link>
        </p>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-3">
            <li class="nav-item" v-if="isLogin">
              <a class="nav-link text-white-50" @click="logout">Logout</a>
            </li>
            
            <li class="nav-item" v-if="!isLogin">
              <!-- <router-link :to="{ name: 'Login' }" class="nav-link text-white-50">Login</router-link> -->
              <p @click="openLoginModal" class="text-decoration-none text-white-50">Login</p>
            </li>
            <li class="nav-item" v-if="!isLogin">
              <router-link :to="{ name: 'Signup' }" class="nav-link text-white-50">Signup</router-link>
            </li>
           
            
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle text-white-50" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                영화추천
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
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
            <li class="nav-item">
              <router-link :to="{ name: 'ReviewList' }" class="nav-link text-white-50">Community</router-link>
            </li>
          </ul>
          <form class="d-flex">
            <input class="form-control me-2" v-model="word" type="text" placeholder="검색할 영화를 입력하세요." @input="searchMovie" @keypress.enter="searchMovie">
            <button class="btn btn-outline-success" @click="searchMovie">Search</button>
          </form>
        </div>
      </div>
    </nav>
    <router-view @login="isLogin=true"/>
    <login @closeLoginModal="closeLoginModal" v-if='loginModal'
    style="position:fixed; m-auto; background:none; "
    >
    </login>
  </div>
</template>

<script>
import axios from 'axios'
import Login from './views/accounts/Login.vue'

export default {
  name: 'App',

  components: {
    Login,
  },

  data: function () {
    return {
      word : null,
      isLogin : false,
      loginModal : false,
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
    },
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },
    openLoginModal: function () {
      this.loginModal = true
    },
    closeLoginModal: function () {
      this.loginModal = false
    },
  },
  created: function (event) {
    this.loginModal = false
    const jwtToken = localStorage.getItem('jwt')
    console.log(event)
    if (jwtToken) {
      this.isLogin = true
      this.$router.push({ name: 'Index' })
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

.nav-link {
  color: white;
}

.modal-backdrop{
  height:100%;
}

</style>
