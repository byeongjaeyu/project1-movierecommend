<template>
  <div id="app" class="container">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark font sticky-top border">
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
              <a class="nav-link text-light" @click="logout">Logout</a>
            </li>
            <li class="nav-item" v-if="!isLogin">
              <!-- <router-link :to="{ name: 'Login' }" class="nav-link text-white-50">Login</router-link> -->
              <p @click="openLoginModal" class="text-decoration-none text-light" style="margin:8px;">Login</p>
            </li>
            <li class="nav-item" v-if="!isLogin">
              <p @click="openSignupModal" class="text-decoration-none text-light" style="margin:8px;">Signup</p>
            </li>
            <li class="nav-item" v-if="isAdmin">
              <a href="http://127.0.0.1:8000/admin" class="nav-link text-decoration-none text-light">관리자페이지</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle text-light" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                영화추천
              </a>
              <ul class="dropdown-menu border bg-dark" aria-labelledby="navbarDropdown">
                <li @click="indexOut">
                  <router-link :to="{ name: 'Recommend1' }" class="dropdown-item bg-dark text-light">랜덤영화추천</router-link>
                </li>
                <li @click="indexOut">
                  <router-link :to="{ name: 'Recommend2' }" class="dropdown-item bg-dark text-light">회원님이 좋아할 만한영화</router-link>
                </li>

              </ul>
            </li>
            <li  @click="indexOut" class="nav-item">
              <router-link :to="{ name: 'ReviewList' }" class="nav-link text-light">Community</router-link>
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
    style="position: fixed; top: 30%; left: 0; right: 0; bottom: 0; z-index:10000;"
    >
    </login>
    <signup 
    @closeSignupModal="closeSignupModal" 
    @signup="signup" v-if='signupModal'
    style="position: fixed; top: 30%; left: 0; right: 0; bottom: 0; z-index:10500;"
    >
    </signup>
    <Index :searchMovies="searchMovies" v-show="showIndex">
    </Index>
  </div>
</template>

<script>
import axios from 'axios'
import Login from './views/accounts/Login.vue'
import Signup from './views/accounts/Signup.vue'
import Index from './views/movies/Index.vue'
// import $ from 'jquery'
// import * as jose from 'jose'
import jwt_decode from 'jwt-decode'
// function randombg(){
//   var random= Math.floor(Math.random() * 6) + 0;
//   var bigSize = [ "url('/src/assets/backgorund/bg1.jpg')",
//                   "url('/src/assets/backgorund/bg2.jpg')",
//                   "url('/src/assets/backgorund/bg3.jpg')",
//                   "url('/src/assets/backgorund/bg4.jpg')",
//                   "url('/src/assets/backgorund/bg5.jpg')",
//                   "url('/src/assets/backgorund/bg6.jpg')",
//                   "url('/src/assets/backgorund/bg7.jpg')",
//                   "url('/src/assets/backgorund/bg8.jpg')",
//                   "url('/src/assets/backgorund/bg9.jpg')",
//                   "url('/src/assets/backgorund/bg10.jpg')",
//                   "url('/src/assets/backgorund/bg11.jpg')",
//                   "url('/src/assets/backgorund/bg12.jpg')",
//                   ];
//   document.getElementById("app").style.backgroundImage=bigSize[random];
//   setTimeout(randombg, 5000);
// }
// randombg()

export default {
  name: 'App',

  components: {
    Login,
    Index,
    Signup,
  },

  data: function () {
    return {
      word : null,
      isLogin : false,
      loginModal : false,
      signupModal : false,
      searchMovies: [],
      showIndex : true,
      userId : null,
      isAdmin : false,
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
      } else {
        this.searchMovies = []
      }
    },
    logout: function () {
      this.isLogin = false
      this.isAdmin = false
      localStorage.removeItem('jwt')
      localStorage.removeItem('username')
      this.$router.push({ name: 'Index' })
    },
    login: function () {
      this.isLogin = true
      this.closeLoginModal()
      const jwtToken = localStorage.getItem('jwt')
      var decoded = jwt_decode(jwtToken)
      // console.log(decoded)
      if (decoded) {
        this.userId = decoded.user_id
        this.isStaff()
      }
      this.$router.push({ name: 'Index' })
    },
    signup: function () {
      this.closeSignupModal()
      this.$router.push({ name: 'Index' })
    },
    openLoginModal: function () {
      this.loginModal = true
    },
    closeLoginModal: function () {
      this.loginModal = false
    },
    openSignupModal: function () {
      this.signupModal = true
    },
    closeSignupModal: function () {
      this.signupModal = false
    },
    indexOut: function () {
      this.showIndex = false
    },
    indexIn: function () {
      this.showIndex = true
    },
    isStaff : function () {
      axios({
        method: 'post',
        url : 'http://127.0.0.1:8000/accounts/isstaff/',
        data : this.userId,
      })
        .then(res => {
          console.log(res)
          this.isAdmin = res.data[0]
        })
    }
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
    var decoded = jwt_decode(jwtToken)
    // const protectedHeader = jose.decodeProtectedHeader(jwtToken)
    // console.log(jwtToken)
    // console.log(window.atob(jwtToken))
    // console.log(protectedHeader)
    // console.log(event)
    if (jwtToken) {
      this.isLogin = true
      this.userId = decoded.user_id
      this.isStaff()
      this.$router.push({ name: 'Index' })
    }
  },
  computed: {},
};
// $(document).on("click",function(event){
//   console.log(event)
//   console.log(this.loginModal)
//   if (this.loginModal==true){
//     console.log(event)
//     this.loginModal = false
//   }
// })
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
