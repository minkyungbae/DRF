# 📘 DRF란?
> **흔히 말하는 RESTful API를 Django로 구축하기 위한 확장 프레임워크이다.**
---
## 기존의 Django랑 무엇이 다를까?
> **✅ 기존의 Django**
- Django는 Web App을 빠르게 개발하기 위한 고수준의 웹 프레임워크이다.
    - Web의 전체 기능이 모두 들어있는 Web Application을 제작
    - 요청에 대해서 html 파일(웹 페이지)을 응답하는 Web Application을 만듦
    - MTV를 활용한 Web
    - 데이터 모델링, URL 라우팅, 템플릿 시스템, 관리자 기능, 세션, 보안 등등

> **✅ DRF에서의 Django**
- 보이는 부분은 처리하지 않고 오직 로직에 집중하는 형태
    - → 요청에 대해 처리한 결과 데이터를 응답하는 형태
- Django REST Framework(DRF)를 이용.
    - → Django + DRF라고 하는 패키지를 살짝 얹은 것(확장)으로 Django를 다룰 수 있다면 무리 없이 할 수 있다.
---
## 🤔 API란?
> **📕 API (Application Programming Interface)** <br>  
**⇒ 쉽게 말해 어플리케이션과 프로그래밍적으로 소통하는 방법**
---
## 🤔 RESTful API란?
> **REST**
**Re**presentational **S**tate **T**ransfer
웹에 대한 소프트웨어 설계 방법론

- 핵심 규칙
    - 자원 : URI로 표현
    - 행위 : HTTP Method로 표현
    - 표현
        - 자원과 행위를 통해 표현되는 결과물로 일반적으로 JSON 형식을 사용
        - URI는 동사가 아닌 명사의 나열로 사용→ POST /articles/ (O)
        - → POST /articles/create/ (X)
- 따르지 않더라도 로직과 동작에는 아무런 이상이 없으나, 이 규칙을 따를 때 얻는 이득 크다.
- 일반적으로 GET, POST, PUT, DELETE (+ PATCH)를 사용한다.