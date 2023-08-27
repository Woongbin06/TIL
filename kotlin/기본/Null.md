## 코틀린의 Null

- 코틀린은 기본적으로 변수 선언 null을 허용하지 않는다.
- 변수 자료형 뒤에 `?`를 붙여서 null을 허용 할 수 있다.

``` Kotlin
var a: Int = null // 에러 O
var b: Int? = null // 에러 X
```

## 세이프콜

``` Kotlin
var str : String? = null
println("str: $str, length: ${ str?.length })
```

위의 코드에서 원래라면 length 부분에서 에러가 나는데 `?`라는 세이프콜을 사용해서 `str`이 `null`이 아닐 경우에만 length를 실행하게 할 수 있다.