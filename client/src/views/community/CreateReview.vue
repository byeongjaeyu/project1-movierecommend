<template>
  <div>
    <h1>게시판 등록</h1>
    <div class="AddWrap">
      <form>
        <table class="tbAdd">
          <colgroup>
            <col width="15%"/>
            <col width="*"/>
          </colgroup>
          <tr>
            <th>제목</th>
            <td><input type="text" v-model="newReview.title"/></td>
          </tr>
          <tr>
            <th>영화제목</th>
            <td><textarea v-model="newReview.movie_title"></textarea></td>
          </tr>
          <tr>
            <th>내용</th>
            <td><textarea v-model="newReview.content"></textarea></td>
          </tr>
          <tr>
            <th>점수</th>
            <td><textarea v-model="newReviewRank"></textarea></td>
          </tr>
        </table>
      </form>
    </div>
    <div class="btnWrap">
      <a href="#" class="btn">목록</a>
      <a href="#" @click="createReview" class="btnAdd btn">등록</a>
    </div>
	</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateReview',
  data: function () {
    return {
      newReview: {
        title: null,
        movie_title: null,
        content: null,
        rank: null,
        // created_at: null,
        // updated_at: null,
        user: null,
        // like_user: null,
      },
      newReviewRank: null,
    }
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createReview: function () {
      // const reviewCreatedAt = new Date()
      // const year = reviewCreatedAt.getFullYear() 
      // const month = reviewCreatedAt.getMonth()+1
      // const date = reviewCreatedAt.getDate()
      // const formatDate = `${year}-${month >= 10 ? month : '0' + month}-${date >= 10 ? date : '0' + date}`
      this.newReviewRank = Number(this.newReviewRank)
      // this.newReview.created_at = formatDate
      // this.newReview.updated_at = formatDate
      this.newReview.user = localStorage.getItem('username')
      this.newReview.rank = this.newReviewRank
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/community/review/',
        data: this.newReview,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'ReviewList' })
        })
        .catch(err => {
          console.log(this.newReview)
          console.log(err)
        })
    }
  }


}
</script>

<style>
h1{color:#43b984;}
table{width:100%; border-collapse:collapse;}
.wrap{width:100%;}
.container{width:800px; margin:0 auto;}
a{text-decoration:none;}
.btn{padding:10px; background:#34445c; color:#fff;}
</style>