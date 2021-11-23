# 영화사이트 프로젝트





## 매일 매일 처리한 부분 기록!



### 11/17(수요일)

- 허영민
  - movies.model.py 에 있는 장르 데이터베이스에 넣기완료
  - movies 에서 index 창에 나올 최근 trend 픽 20개 parsing해서 데이터 받는 코드 완료
  - accounts 및 community 모델과 serializers.py 작성. but 아직 완성은 아님!
  <<<<<<< Updated upstream
  - +(20:28 추가) api로 serializer 받아올 때 manytomanyfield 인 movie 모델의 genres에서 attribute error가 발생했는데 genres를 listfield로 정의하여 받아왔음!

- 유병재
  - vue 프로젝트 생성
  - component 생성 및 라우터 설정 완료





### 11/18(목요일)
허영민

- 검색기능 및 영화선택하면 비슷한 영화를 평점순으로 추천해주는것 구현.
- 모델 재정리 및 데이터베이스 구축
- 리뷰쪽 view 데이터가 잘흐르는지 확인

유병재

- app.vue -> 네브바 변환
- 로그인시, 로그인 아닐시 보이는거 
- index.vue -> grid
- community 구현



### 11/19(금요일)

- 오늘 할일 
  - 커뮤니티쪽 마무리짓기
  - movie 검색 및 알고리즘 추가 및 다듬기
  - 추천 알고리즘 template 만들기
  - 글 쓴사람 id 찾아서 데이터보내기! (완료)





### 11/20~21 (주말)

- 할 예정
  - 허영민 : 데이터베이스 구축했으니까 이를 토대로 검색알고리즘 + 장르로 추천해주는 알고리즘 2개 작성. (완료)



### 11/22(월요일)

- 게시글 검색 및 영화 알고리즘구현
- admin 홈페이지 연결
- community 버튼구현
- 리뷰를 토대로 추천해주는 알고리즘 구현



허영민

- 포스터 이미지 없을 때 대체이미지 넣기
- 리뷰 작성 조회 함수
- 리뷰 토대로 추천해주는 기능 user id 받아와서 처리하기만 하면됨!
- 관리자인지 아닌지 확인해주는 함수 구현
- 리뷰 글쓴 사람인지 아닌지 확인해주는 함수구현



유병재

- 커뮤니티 게시판 작성 기능 구현
- 로그인, 회원가입 modal 이용해서 구현
- 커뮤니티 게시판 detail 구현중



(내일 할 일)

1. recomment2 기능 구현
2. 리뷰 디테일 마무리
3. 영화 디테일(영화 이름 받아서 포스터 출력), 좋아요, 코멘트
4. 영화 리뷰 쓸때 movie_title modal이용해서 우리 데이터베이스에 있는 영화만 선택 할 수 있도록



### 11/23~24(화요일~수요일)

- 기능부분은 거의 다 구현

- but 처음 DB를 잘못 추출하여 youtube URL을 노가다로 가져와야해서 로딩시간이 꽤김 ㅠㅠ

- bootstrap-vue 설치법 !!

  - ```
    npm install vue bootstrap bootstrap-vue
    ```

    위의 패키지 설치

  - ```javascript
    import Vue from 'vue'
    import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
    
    // Import Bootstrap an BootstrapVue CSS files (order is important)
    import 'bootstrap/dist/css/bootstrap.css'
    import 'bootstrap-vue/dist/bootstrap-vue.css'
    
    // Make BootstrapVue available throughout your project
    Vue.use(BootstrapVue)
    // Optionally install the BootstrapVue icon components plugin
    Vue.use(IconsPlugin)
    ```

    main.js 또는 app.js 파일에 위의 코드를 넣어줌

    ```javascript
    // ex) main.js
    
    import Vue from 'vue'
    import App from './App.vue'
    
    import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
    
    // Make BootstrapVue available throughout your project
    Vue.use(BootstrapVue);
    // Optionally install the BootstrapVue icon components plugin
    Vue.use(IconsPlugin);
    
    // Import Bootstrap an BootstrapVue CSS files (order is important)
    import "bootstrap/dist/css/bootstrap.css";
    import "bootstrap-vue/dist/bootstrap-vue.css";
    
    Vue.config.productionTip = false
    
    new Vue({
      render: h => h(App),
    }).$mount('#app')
    ```

    

