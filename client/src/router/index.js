import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '@/views/movies/Index'
import Recommend1 from '@/views/movies/Recommend1'
import Recommend2 from '@/views/movies/Recommend2'
import CreateComment from '@/views/community/CreateComment'
import CreateReview from '@/views/community/CreateReview'
import ReviewUpdate from '@/views/community/ReviewUpdate'
import ReviewDetail from '@/views/community/ReviewDetail'
import ReviewList from '@/views/community/ReviewList'
import Login from '@/views/accounts/Login'
import Signup from '@/views/accounts/Signup'

Vue.use(VueRouter)

const routes = [
  {
    path: '/Index',
    name: 'Index',
    component: Index,
  },
  {
    path: '/accounts/Login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/Signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/movie/recommend1',
    name: 'Recommend1',
    component: Recommend1,
  },
  {
    path: '/movie/recommend2',
    name: 'Recommend2',
    component: Recommend2,
  },
  {
    path: '/community/',
    name: 'ReviewList',
    component: ReviewList,
  },
  {
    path: '/community/create',
    name: 'CreateReview',
    component: CreateReview,
  },
  {
    path: '/community/:reviewid/createcomment',
    name: 'CreateComment',
    component: CreateComment,
  },
  {
    path: '/community/:reviewid/reviewdetail',
    name: 'ReviewDetail',
    component: ReviewDetail,
  },
  {
    path: '/community/:reviewid/reviewupdate',
    name: 'ReviewUpdate',
    component: ReviewUpdate,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
