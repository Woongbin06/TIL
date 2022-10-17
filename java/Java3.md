ERROR : 프로그램이 동작하는 환경이 문제인 것.
**EXCEPTION** : 사용자가 원하는 것과 다른 상황에 직면한 것.

# 예외
사용자가 원하는 값과 다른 경우이 나오는 경우
``` java
System.out.println(1);
System.out.println(2 / 0); // 예외적 상황이 발생함.
```
## 예외처리
사용자가 원하는 값과 다른 경우가 나오는 경우에 해결해 주는 것   
try와 catch를 사용하여 예외처리를 한다. 여러개의 catch를 사용할 수 있다.

※ 상속받은 자식 익셉션의 부모 익셉션이 자식 익셉션을 다 포함하기 때문에 예외가 두개라면 두 자식의 부모 하나만 쓰면 통합 할 수 있음.

# Checked vs Unchecked Exception
예외 구분은 간단하게 상속하지 않는 클래스를 Checked Exception이라고 하고, 상속한 클래스는 Unchecked Exception이라고 한다.
![](https://velog.velcdn.com/images/woongbin06/post/f398b086-c816-4249-9281-ddbb4af91a77/image.png)

## finally
finally는 try에서 익셉션이 발생하든 않하든 무조건 실행한다.   
try{} -> catch{} -> finally{} 순으로 진행 된다.

## 정리 
예외는 사용자가 원하는 값이 아닌 다른 상황이 발생했을 때고 예외가 발생했을 때 예외처리를 한다. 예외에는 Checked와 Unchecked가 있다. finally를 사용하면 예외가 발생하든 않하든 무조건 실행한다.