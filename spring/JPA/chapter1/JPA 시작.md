# 엔티티 매핑

## Member.class

```jsx
@Entity
@Table(name = "MEMBER")
public class Member {
	@Id
	@Column(name = "ID")
	private String id;

	@Column(naem = "NAME")
	private String username;

	// 매핑 정보가 없는 필드
	private Integer age;
}
```

- **@Entity** : 이 어노테이션을 붙인 클래스를 테이블과 **매핑**한다고 JPA에게 알려준다.
- **@Table** : 엔티티 클래스에 매핑할 테이블 정보를 알려준다. 여기서는 **name** 속성을 사용해 Member 엔티티를 MEMBER 테이블에 매핑한다.
- **@Id** : 필드를 테이블 **기본 키(PK)**에 매핑한다.
- **@Column** : 필드를 컬럼에 매핑한다. 여기서는 **name** 속성을 이용해 username 필드를 NAME 컬럼에 매핑한다.
- 매핑 정보가 없는 필드 : 매핑 어노테이션을 생성하면 자동으로 필드명을 사용해서 컬럼명으로 매핑한다.

# 데이터베이스 방언

데이터베이스마다 데이터 타입이나 같은 기능을 하지만 함수명이 다른 것이 있다.

이처럼 SQL 표준을 지키지 않거나 특정 데이터베이스만의 **고유한 기능**을 JPA에서는 **방언**이라고 한다.

### JPA의 해결법

JPA는 이런 방언을 해결하기 위해 방언 클래스를 만들어 특정 데이터베이스에 **의존적인 SQL은 방언**이 처리해준다.

![](https://blog.kakaocdn.net/dn/cunU3I/btqEGTU1B8W/cEefmBqjuHKKbsSgQykj7k/img.png)