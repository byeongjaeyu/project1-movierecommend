<template>
  <transition name="modal" appear >
    <!-- <div class="modal" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true"> -->
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Login</h5>
            <button @click="$emit('closeLoginModal')">Close</button>
          </div>
          <div class="modal-body">
            <div>
              <label for="username">사용자 이름: </label>
              <input type="text" id="username" v-model="credentials.username">
            </div>
            <div>
              <label for="password">비밀번호: </label>
              <input type="password" @keypress.enter="login" id="password" v-model="credentials.password">
            </div>
          </div>
          <div class="modal-footer">
            <button @click="login" class="btn btn-primary">로그인</button>
          </div>
        </div>
      </div>
    <!-- </div> -->
  </transition>
</template>


<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt',res.data.token)
          this.$emit('login')
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
