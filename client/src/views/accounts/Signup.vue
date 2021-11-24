<template>
  <transition name="modal" appear >
    <!-- <div class="modal" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true"> -->
      <div class="modal-dialog container">
        <div class="modal-content border border-3 border-dark rounded">
          <div class="modal-header d-flex justify-content-between">
            <h5 class="modal-title fw-bold fs-3">Signup</h5>
            <button class="bg-white" @click="$emit('closeSignupModal')">Close</button>
          </div>
          <div class="modal-body">
            <div>
              <label class="fw-bold me-2 my-2" for="username">사용자 이름: </label>
              <input type="text" id="username" v-model="credentials.username">
            </div>
            <div>
              <label class="fw-bold me-2 my-2" for="password">비밀번호: </label>
              <input class="fw-bold me-2 my-2" type="password" id="password" v-model="credentials.password">
            </div>
            <div>
              <label class="fw-bold me-2 my-2" for="password">비밀번호 확인: </label>
              <input type="password" id="password" v-model="credentials.passwordConfirmation">
            </div>
          </div>
          <div class="modal-footer">
            <button @click="signup" class="btn btn-primary fw-bold">회원가입</button>
          </div>
        </div>
      </div>
    <!-- </div> -->
  </transition>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      console.log(this.credentials)
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then( () => {
          this.$router.push( { name: 'Login' } )
          this.$emit('signup')
        })
        .catch( err => {
          console.log(err)
        })
    }
  }
}
</script>
