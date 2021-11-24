<template>
  <div>
    <b-modal ref="movieModal" hide-footer title='test'>
      <div class="text-center">
        <div>
        <img width="400" height="600" src="https://image.tmdb.org/t/p/original//1Lh9LER4xRQ3INFFi2dfS2hpRwv.jpg" alt="">
        </div>
        <div>
          줄거리
        </div>
        <div>
        <iframe width="400" height="300" src="https://www.youtube.com/embed/uiIIyepK6XY" frameborder="0">트레일러 영상이 없어요.</iframe>
        </div>
      </div>
    </b-modal>
  </div>
</template>

<script>

export default {
  name : "Modal",
  components: {Index},
  data : function () {
    return {
      movie: null,
    }
  },
  props: {
    movie: Object,
  },

}
</script>

<style>

</style>