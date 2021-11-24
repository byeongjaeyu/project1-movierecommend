<template>
  <div class="container">
    <br>
    <h1>커뮤니티</h1>
    <hr>
    <table class="table table-hover ">
      <thead>
        <tr>
          <th>번호</th>
          <th>제목</th>
          <th>작성자</th>
          <th>날짜</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="review in reviewList" :key="review.id" @click="goToDetail($event, review)">
            <td>{{ review.id }}</td>
            <td>[{{ review.movie_title }}] {{ review.title }}</td>
            <td>{{ review.username }}</td>
            <td>{{ review.created_at }}</td>
        </tr>
      </tbody>
    </table>
    <router-link :to="{ name: 'CreateReview' }" class="text-decoration-none">리뷰 작성</router-link>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'ReviewList',
  components: {
    
  },
  data: function () {
    return  {
      reviewList : null,
    }
  },
  created: function () {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/review/`
    })
      .then(res => {
        this.reviewList = res.data
        console.log(this.reviewList)
      })
  },
  methods: {
    goToDetail: function (event, review) {
      // console.log(review.id)
      this.$router.push({ name: 'ReviewDetail' , params: {reviewid:review.id, reviewuser:review.username}} )
    }
    },
  }
</script>

<style>

</style>
