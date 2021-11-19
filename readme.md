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
  - 허영민 : 데이터베이스 구축했으니까 이를 토대로 검색알고리즘 + 장르로 추천해주는 알고리즘 2개 작성.
