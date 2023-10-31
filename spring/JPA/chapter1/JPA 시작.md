# 엔티티 매핑

## Member.class

```java
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

# 애플리케이션 개발

애플리케이션을 개발할 때 크게 코드를 3부분으로 아래와 같이 나눌 수 있다.

- 엔티티 매니저 설정
- 트랜잭션 관리
- 비즈니스 로직

## 엔티티 매니저 설정

### 엔티티 매니저 팩토리 생성

JPA를 사용하려면 엔티티 매니저 팩토리를 생성해야 한다

```java
EntityManagerFactory emf = Persistence.createEntityManagerFactory("jpabook");
```

- 엔티티 매니저 팩토리를 생성하는 비용이 아주 크다.
    
    → 엔티티 매니저 팩토리는 애플리케이션 전체에 딱 **한 번만** 생성하고 **공유**해서 사용해야 한다.
    

### 엔티티 매니저 생성

```java
EntityManager em = emf.createEntityManager();
```

- 엔티티 매니저 팩토리에서 **엔티티 매니저**를 생성한다.
- 엔티티 매니저로 엔티티를 데이터베이스에 **등록/수정/삭제/조회**할 수 있다.
- 엔티티 매니저는 데이터베이스 커넥션과 밀접한 관계가 있어서 **스레드 간에 공유하거나 재사용**하면 안된다.

### 종료

- 사용이 끝난 엔티티 매니저는 반드시 중료해야 한다.
- 애플리케이션을 종료할 때 엔티티 매니저 팩토리도 다음처럼 종료해야 한다.

```java
em.close(); // 엔티티 매니저 종료
emf.close(); // 엔티티 매니저 팩토리 종료
```

## 트랜잭션 관리

- JPA를 사용하면 **항상 트랜잭션 안**에서 데이터를 변경해야 한다.
- 트랜잭션 API를 사용하여 비지니스 로직이 정상 동작하면 **커밋**, 아니면 **롤백**을 한다.

## 비즈니스 로직

- 등록, 수정, 삭제 조회 작업을 엔티티 매니저를 사용하여 수행한다.

# JPQL

**JPQL (Java Persistence Query Language)**는 SQL을 추상화한 **객체지향** 쿼리 언어이다.

## 차이점

- JPQL은 **엔티티 객체**를 대상으로 쿼리한다.
- SQL은 **데이터베이스 테이블**을 대상으로 쿼리한다.