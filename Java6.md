# Spring 프로젝트 생성 방법
먼저 start.spring.io 홈페이지에 들어가 프로젝트 방식이나 사용할 언어, Spring 버전, 프로젝트 이름 등을 지정한다.
<img src = "https://engineering-skcc.github.io/assets/images/ejchoi/2021-10-14-01.png"
width = "700px" height = "500px">   
설정을 다 하고나서 GENERATE를 클릭해 스프링 프로젝트를 생성한다.

프로젝트를 열고, main 폴더에 있는 java 파일을 실행 시키면 스프링 부트 서버가 열린다. localhost:8080으로 들어가서 확인할 수 있다.

# View 환경설정
main 폴더의 resurces/static 폴더에 들어가서 index.html을 생성하면, 웹의 Welcome page가 생긴다.

Controller 파일을 만들어서 
``` java
@GetMapping("hello")
public String hello(Model model) {
  model.addAttribute("data", "hello!!");
  return "hello";
}
```
위 코드를 입력하게되면, 사용자가 localhost:8080/hello url를 입력했을 때 hello라는 html파일을 실행하게 한다.
``` html 
<html xmlns:th = "http://www.thymeleaf.org">
<head>
  <title>Hello</title>
</head>
<body>
  <p th:text="안녕하세요. ' + ${data}">안녕하세요. 손님</p>
</body>
```
위 코드는 hello.html파일인데 localhost:8080/hello로 들어갈시 안녕하세요 hello!!를 출력한다. hello라는 메소드에서 data라는 key에 hello!!라는 value를 주어 html에서 ${data}를 이용해 불러오기 때문.

# 정적 컨텐츠
static 폴더에 html파일을 만들면 된다.
``` html
<head>
  <title>static content</title>
</head>
<body>
  정적 컨텐츠입니다.
</body>
```
이런식으로 html폴더를 만들어 주고 localhost:8080/파일명 을 입력하면 굳이 @GetMapping을 이용하지 않고도 홈페이지를 실행하게 된다.

# MVC와 템플릿 엔진
MVC : Model, View, Controller

``` java
@GetMapping("hello-mvc")
public String helloMvc(@RequestParam("name") String name, Model model) {
  model.Addattribute("name", name);
  return "hello-template"
}