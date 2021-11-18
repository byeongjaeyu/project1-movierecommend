<template>
  <div>
    <hr>
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
        <tr v-for="review in reviewList" :key="review.id" @click="goToDetail">
          <td>{{ review.id }}</td>
          <td>[{{ review.movie_title }}] {{ review.title }}</td>
          <td>{{ review.user }}</td>
          <td>{{ review.created_at }}</td>
        </tr>
      </tbody>
    </table>
 

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewList',
  data: function () {
    return  {
      reviewList : null,
    }
  },
  created: function () {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/`
    })
      .then(res => {
        this.reviewList = res.data
        console.log(this.reviewList)
      })
  }
}
</script>

<style>

</style>