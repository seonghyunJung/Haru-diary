# Haru-diary

## AI 감성분석 일기 서비스 - [Page Link](http://15.165.121.165/)

### 소개
학교 졸업 프로젝트를 Django를 이용해 웹사이트 형태로 재구성하였습니다. <br/>
일기를 작성하면 AI가 해당 일기의 감정을 분석하여 알려주고, 사용자는 달력 및 통계 기능을 통해 지난 감정 추이를 한눈에 볼 수 있습니다. <br/>
[졸업 프로젝트 링크](https://github.com/CSID-DGU/2022-1-CECD3-FRIDAY-5) <br/>

### 개발동기
졸업 프로젝트에서 팀장 및 인공지능 모델 부분을 맡았었는데 프론트엔드 부분과 백엔드 부분을 더 잘 알고 진행했으면 좋았을 걸 하는 아쉬움이 남았습니다. <br/>
그래서 최근에 공부하고 있는 Django를 이용해 프론트부터 백까지 모든 부분을 직접 웹서비스 형태로 구현해 보았습니다.


----------------------------
### 개발 환경
<p>
  <img src = "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
  <img src = "https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
  <img src = "https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white">
  <img src = "https://img.shields.io/badge/Pytorch-EE4C2C?style=for-the-badge&logo=Pytorch&logoColor=white">
  
  <img src = "https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=PostgreSQL&logoColor=white">
  <img src = "https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white">
  <img src = "https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=NGINX&logoColor=white">
  <img src = "https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=Gunicorn&logoColor=white">
  <img src = "https://img.shields.io/badge/Amazone EC2-FF9900?style=for-the-badge&logo=Amazon EC2&logoColor=black">
</p>

----------------------------

<img width="1512" alt="image" src="https://github.com/seonghyunJung/Haru-diary/assets/76807684/d0ca5172-d993-4dc3-8720-2a41c741513e"> <br/>
<div align="center">[로그인 페이지]</div>

<hr/>


<img width="1512" alt="image" src="https://github.com/seonghyunJung/Haru-diary/assets/76807684/71f78bee-6d90-49ee-a4b8-445c3c2b8232"> <br/>
<div align="center">[회원가입 페이지]</div>

<hr/>


<img width="1512" alt="image" src="https://github.com/seonghyunJung/Haru-diary/assets/76807684/3968796e-f67f-4098-984e-e60aa2adeaa2"> <br/>
<div align="center">[일기작성 페이지]</div>

- 일기를 쓰고 저장을 누르면 AI가 해당 일기의 감정을 분석합니다.

<hr/>


<img width="1512" alt="image" src="https://github.com/seonghyunJung/Haru-diary/assets/76807684/1aa0396c-1414-4e95-9930-ca8440559ab1"> <br/>
<div align="center">[일기 감성분석]</div>

- 7 감정의 분포를 보여줍니다.

<hr/>


<img width="1512" alt="image" src="https://github.com/seonghyunJung/Haru-diary/assets/76807684/1e779e96-5917-45cf-b23f-a28674ab3e59"> <br/>
<div align="center">[캘린더 페이지]</div>

- 캘린더 페이지에서는 이전에 작성했던 각 일기의 주요 감정을 이모지 형태로 확인할 수 있습니다.
- 이모지를 클릭하면 해당 날짜에 작성한 일기를 확인, 수정, 삭제할 수 있습니다. 

<hr/>


<img width="1512" alt="image" src="https://github.com/seonghyunJung/Haru-diary/assets/76807684/310a07db-f1c7-4acd-b899-ed22a8c663ae"> <br/>
<div align="center">[통계 페이지]</div>

- 통계 페이지에서는 보고싶은 날짜 범위의 감정 추이를 막대 그래프 형태로 한눈에 확인할 수 있습니다.
- 왼쪽 상단의 날짜 부분을 클릭하여 달력 위젯을 통해 원하는 날짜 범위를 선택할 수 있습니다.


----------------------------

