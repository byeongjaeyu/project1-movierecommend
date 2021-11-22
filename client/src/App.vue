<template>
  <div id="app" class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-secondary font sticky-top">
      <div class="container-fluid">
        <p  @click="indexIn" class="navbar-brand fw-bold text-white-50 m-auto">
          <router-link :to="{ name: '/' }" class="text-decoration-none text-white-50">
            <img src="https://fontmeme.com/permalink/211118/4236136457f6822dd292086626451371.png">
          </router-link>
        </p>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-3">
            <li class="nav-item" v-if="isLogin">
              <a class="nav-link text-white-50" @click="logout">Logout</a>
            </li>
            
            <li class="nav-item" v-if="!isLogin">
              <!-- <router-link :to="{ name: 'Login' }" class="nav-link text-white-50">Login</router-link> -->
              <p @click="openLoginModal" class="text-decoration-none text-white-50" style="margin:8px;">Login</p>
            </li>
            <li class="nav-item" v-if="!isLogin">
              <router-link :to="{ name: 'Signup' }" class="nav-link text-white-50">Signup</router-link>
            </li>
           
            
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle text-white-50" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                영화추천
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li @click="indexOut">
                  <router-link :to="{ name: 'Recommend1' }" class="dropdown-item">랜덤영화 20</router-link>
                </li>
                <li @click="indexOut">
                  <router-link :to="{ name: 'Recommend2' }" class="dropdown-item">추천2</router-link>
                </li>
                <li @click="indexOut">
                  <router-link :to="{ name: 'Recommend3' }" class="dropdown-item">추천3</router-link>
                </li>
              </ul>
            </li>
            <li  @click="indexOut" class="nav-item">
              <router-link :to="{ name: 'ReviewList' }" class="nav-link text-white-50">Community</router-link>
            </li>
          </ul>
          <form class="d-flex">
            <input 
            class="form-control me-2" 
            v-model="word" 
            type="text" 
            placeholder="검색할 영화를 입력하세요." 
            @input="searchMovie"
            >
            <button class="btn btn-outline-success" @click="searchMovie">Search</button>
          </form>
        </div>
      </div>
    </nav>
    <router-view />
    <login 
    @closeLoginModal="closeLoginModal" 
    @login="login" v-if='loginModal'
    style="position: fixed; top: 30%; left: 0; right: 0; bottom: 0; z-index:1050;"
    >
    </login>
    <Index :searchMovies="searchMovies" v-show="showIndex">
    </Index>
  </div>
</template>

<script>
import axios from 'axios'
import Login from './views/accounts/Login.vue'
import Index from './views/movies/Index.vue'
// import $ from 'jquery'

export default {
  name: 'App',

  components: {
    Login,
    Index,
  },

  data: function () {
    return {
      word : null,
      isLogin : false,
      loginModal : false,
      searchMovies: [],
      showIndex : true,
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
            this.searchMovies = res.data
          })
      }
    },
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      localStorage.removeItem('username')
      this.$router.push({ name: 'Index' })
    },
    login: function () {
      this.isLogin = true
      this.closeLoginModal()
      this.$router.push({ name: 'Index' })
    },
    openLoginModal: function () {
      this.loginModal = true
    },
    closeLoginModal: function () {
      this.loginModal = false
    },
    indexOut: function () {
      this.showIndex = false
    },
    indexIn: function () {
      this.showIndex = true
    },
    // modalOut: function () {
    //   if (this.loginModal===true){
    //     this.loginModal = false
    //   }
    // },
  },
  created: function (event) {
    console.log(event)
    this.loginModal = false
    const jwtToken = localStorage.getItem('jwt')
    console.log(event)
    if (jwtToken) {
      this.isLogin = true
      this.$router.push({ name: 'Index' })
    }
  },
  computed: {},
};
// $('#Modal').modal({
//    backdrop: 'static',
//    keyboard: false
// });
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

</style>
