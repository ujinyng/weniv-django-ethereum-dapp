# weniv-django-ethereum-dapp
klaytn/django/web 이더리움 스마트컨트랙트를 이용한 대안대학 사이트  

### 프로젝트 내용
###### jeju blockchain hackerthon 에서 진행한 weniv라는 대안대학 서비스 웹사이트
###### 본인은 smart contract 를 맡아 solidity와 caver.js 부분을 구현 
- 현재는 가상환경을 생성하여 개발한 django, html, bootstrap 등 서버 및 프론트만 포함되어 있음.
- 컨트랙트 코드는 후에 klaytn이 정식 출시되면 추가로 업데이트할 예정
###### react만 사용하다가 django를 처음 접해, 생성, 실행방법을 알게되어 의미가 있었음.


### 실행방법(os : ubuntu 14.04 에서 개발)
#### 사전설치
- python3 
- 기타 

```pip3 install django-taggit```

```pip3 install django-bootstrap4```

```pip3 install Pillow```

#### 가상환경 생성 및 실행

```python3 -m venv my venv```

```source myvenv/bin/activate```

#### 장고 설치(ver. 1.18.0)

- pip 최신버전 확인

```(myvenv) ~$ python3 -m pip install --upgrade pip```

- django 설치

```(myvenv) ~$ pip install django```

- 본 repository를 받으면 이미 django 프로젝트가 생성되어 있어 설치후 별도 생성 필요없음

#### 웹서버 실행

```(myvenv) ~$python manage.py runserver 0:8000```

#### 사이트 접속

- http://localhost:8000 에 접속

### 참고사항
- klaytn 베타 버전에서 실행하여 웹 상단의 klay가 제대로 나오지 않을수 있음 
- 현재 해커톤에서 사용하던 서버가 중지되어 메뉴클릭시 사이트접속 불가능, 아래의 주소로 접속해야함
- main :http://localhost:8000/
- about :http://localhost:8000/about/
- 강의목록 : http://localhost:8000/lecture/
- 강의설명 : http://localhost:8000/lecture/1/lecturedetails/
- 강의로드맵 : http://localhost:8000/roadmap
- 컨트랙트내용 : http://localhost:8000/contractcode/
