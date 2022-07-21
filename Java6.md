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
```
위 코드는 localhost:8080/hello-mvc url로 들어갈 시 실행되는 메소드인데 @RequestParam으로 사용자로부터 값을 입력받고, hello-template.html파일을 실행한다.
> **HOW INPUT?**    
localhost:8080/hello?name=입력할 값.

``` html
<html xmlns:th = "http://www.thymeleaf.org">
<body>
  <p th:text="'hello ' + ${name}">hello! empty</p>
</body>
```
hello-template.html 코드인데, 사용자로부터 입력받은 값 name을 사용해 입력에 따라 출력이 바뀌는 코드인다.   
> ex ) localhost:8080/hello-mvc?name=spring을 입력하면 hello spring을 출력한다.

# API
html파일을 거치지 않고, 바로 데이터를 내리는 것.

``` java
@GetMapping("hello-string")
@ResponseBody // Body 응답 부분에 값을 직접 넣어주겠다는 의미.
public String helloString(@RequestParam("name") String name) {
  return "hello " + name; // spring 입력시 hello spring출력
}
```
위 코드는 html파일을 거치지 않고 바로 출력하는 방식이다.

``` java
@GetMapping("hello-api")
@ResponseBody
public Hello helloApi(@RequestParam("name") String name) {
  Hello hello = new Hello();
  hello.setName(name);
  return hello;
}

static class Hello {
  private String name;

  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name
  }
}
```
위 코드는 localhost:8080/hello-api url을 입력하면 실행되는데 객체를 이용한 api방식이다.   
private으로 name이라는 변수를 생성했기 때문에 외부에서 사용할 수 있게 getter와 setter 메소드를 이용하여 입력과 출력을 할 수 있게 한다.
> ex ) localhost:8080/hello-api?name=spring!!을 입력하면 { "name" : "hello spring!!" }을 출력한다.   
**{ }로 묵이는 이유는 객체이기 때문.**