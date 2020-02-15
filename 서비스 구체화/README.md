# share-youtube-music-playlist

<br>

## 있었으면 하는 기능들

* 플레이 리스트 만들기
* 플레이 리스트 공유 (공유 및 좋아요)
* 뮤직 플레이

<br>

## DB 구상

<br>

### 플레이 리스트 만들기

* 유저별로 여러개의 플레이 리스트를 저장해야함
* User, PlayList, Music 모델 필요
  * User는 Django 기본 제공 모델 사용
  * PlayList는 User와 N:1 연결
  * Music은 PlayList와 M:N 연결

