# JPQL

# 특징

- JPQL은 객체지향 쿼리 언어이다.
- 테이블을 대상으로 쿼리하는 것이 아닌 엔티티 객체를 대상으로 쿼리한다.
- JPQL은 SQL을 추상화해서 특정 데이터베이스 SQL에 의존하지 않는다.
- JPQL은 결국 SQL로 변환된다.

이번 절에서 사용할 도메인 모델이다.

![](https://img1.daumcdn.net/thumb/R750x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FKHuB3%2FbtrJWnEN1rX%2FAEpmhO6uAKniHdzAOoS8Bk%2Fimg.png)


# 기본 문법과 쿼리 API

## SELECT 문

```sql
SELECT m FROM Member AS m where m.username = 'Hello'
```

- **대소문자 구분** : 엔티티와 속성은 대소문자를 구분한다.
- **엔티티 이름** : JPQL에서 사용하는 엔티티는 클래스 명이 아니라 엔티티 명을 적어야 한다.
- **별칭은 필수** : Member As m을 보면 Member에 m이라는 별칭을 주었다.

## TypeQuery, Query

작성한 JQPL은 실행하려면 쿼리 객체를 만들어야 한다.

- 쿼리 객체는 TypeQuery와 Query가 있다.
- 반환 타입을 명확하게 지정할 수 있으면 TypeQuery 객체 사용
- 반환 타입을 명확하게 지정할 수 없으면 Query 객체 사용

```java
TypedQuery<Memebr> query = em.createQuery("SELECT m FROM Member m", Member.class);

Query query = em.createQuery("SELECT m.username, m.age from Member m");
```

### 결과 조회

- query.getResultList( ) : 결과를 예제로 반환한다. 만약 결과가 없으면 빈 컬렉션을 반환한다.
- query.getSingleResult( ) : 결과가 정확히 하나일 때 사용한다.
    - 결과가 없거나 1개보다 많으면 예외가 발생한다.

# 파라미터 바인딩

## 이름 기준 파라미터

JPQL은 이름 기준 파라미터 바인딩 지원한다.

```java
TypedQuery<Member> query =
	em.createQuery("SELECT m FROM Member m where m.username = :username", Member.class);
query.setParameter("username", "User1");
List<Member> resultList = query.getResultList();
```

1. :username이라는 **이름 기준 파마리터**를 정의.
2. query.setParameter( )에서 username이라는 이름으로 파라미터 바인딩.

## 위치 기준 파라미터

JPQL은 위치 기준 파라미터 방식도 지원한다.

```java
List<Member> members =
	em.createQuery("SELECT m FROM Member m where m.username = ?1", Member.class)
		.setParameter(1, "User1")
		.getResultList();
```

💡 **위치 기준 파라미터 방식보다는 이름 기준 파라미터 바인딩 방식을 사용하는 것이 더 명확하다.**

# 프로젝션

SELECT 절에 조회할 대상을 지정하는 것을 프로젝션이라 한다.

- 프로젝션 대상은 엔티티, 엠비디드 타입, 스칼라 타입(숫자, 문자 등 기본 데이터)이 있다.

## 엔티티 프로젝션

```java
SELECT m FROM Member m
```

엔티티 프로젝션은 쉽게 말해 원하는 객체를 바로 조회한 것이다. 

- **조회한 엔티티는 영속성 컨텍스트에 저장된다.**

## 임베디드 타입 프로젝션

- JPQL에서 임베디드 타입은 엔티티와 거의 비슷하게 사용된다.
- 임베디드 타입은 조회의 시작점이 될 수 없다.

```java
String query = SELECT o.address FROM Order.o";
List<Address> addresses = em.createQuery(query, Address.class)
														.getResultList();
```

- 임베디드 타입은 엔티티 타입이 아닌 값 타입이다.
    
    → **직접 조회한 임베디드 타입은 영속성 컨텍스트에서 관리되지 않는다.**
    

## 스칼라 타입 프로젝션

숫자, 문자, 날짜와 같은 기본 데이터 타입들을 스칼라 타입이라 한다.

```java
List<String usernames = em.createQuery("SELECT username FROM Member, m", String.class)
													.getResultList();
```

위 코드는 회원의 이름만 조회하는 코드이다. 중복 데이터를 제거하려면 DISTINCT를 사용하면 된다.

## 여러 값 조회

프로젝션에 여러 값을 선택하면 Query를 사용해야 한다.

```java
Query query = em.createQuery("SELECT m.username, m.age FROM Member m");
List resultList = query.getResultList();

Iterator iterator = resultList.iterator();
while (iterator.hasNext()) {
	Object[] row = (Object[]) iterator.next();
	String username = (String) row[0];
	Integer age = (Integer) rows[1];
}
```

스칼라 타입 뿐만 아니라 엔티티 타입도 여러 값을 함께 조회할 수 있다.

# 페이징 API

JPA는 페이징을 다음 두 API로 추상화했다.

- setFirstResult (int startPosition) : 조회 시작 위치 (0부터 시작)
- setMaxResults (int maxResult) : 조회할 데이터 수

```java
TypedQuery<Member> query = 
	em.createQuery("SELECT m FROM Member m ORDER BY m.username DESC",
	Member.class);

query.setFirstResult(10);
query.setMaxResults(20);
qeury.getResultList();
```

위 코드를 실행하면 시작 지점은 10이므로 **11번째부터 시작해서 총 20건**의 데이터를 조회한다. 즉 11~30번 데이터를 조회한다.

# 집합과 정렬

집합은 집합함수나 통계 정보를 구할 때 사용한다.

## 집합 함수

| 함수 | 설명 |
| --- | --- |
| COUNT | 결과 수를 구한다. 반환 타입 : Long |
| MAX, MIN | 최대, 최소 값을 구한다. 문자, 숫자, 날짜 등에 사용한다. |
| AVG | 평균값을 구한다. 숫자타입만 사용할 수 있다. 반환 타입 : Double |
| SUM | 합을 구한다. 숫자타입만 사용할 수 있다. |

## 집합 함수 사용 시 참고사항

- **NULL 값**은 무시하므로 통계에 잡히지 않는다.
- 만약 값이 없는데 SUM, AVG, MAX, MIN 함수를 사용하면 NULL 값이 된다. 단 COUNT는 0이 된다.
- DISTINCT를 집합 함수 안에 사용해서 중복된 값을 제거하고 나서 집합을 구할 수 있다.
- DISTINCT를 COUNT에서 사용할 때 임베디드 타입은 지원하지 않는다.

## GROUP BY, HAVING

- GROUP BY는 통계 데이터를 구할 때 특정 그룹끼리 묶어준다.
- HAVING은 GROUP BY와 함께 사용하는데 그룹화한 통계 데이터를 기준으로 필터링한다.

## 정렬 (ORDER BY)

ORDER BY는 결과를 정렬할 때 사용한다.

- **ASC** : 오름차순 (기본값)
- **DESC** : 내립차순

# JPQL 조인

## 내부 조인

내부 조인은 INNER JOIN을 사용한다. ( INNER는 생략 가능 )

```java
String query = "SELECT m FROM Member m INNER JOIn m.team t WHERE t.name = :teamName";
List<Member> members = em.createQuery(query, Member.class)
	.setParameter("teamName", "팀A")
	.getResultList();
```

- JPQL 조인의 가장 큰 특징은 **연관필드를 사용**한다.

## 컬렉션 조인

일대다 관계나 다대다 관계처럼 **컬렉션을 사용하는 곳에 조인**하는 것을 컬렉션 조인이라 한다.

```java
SELECT t, m FROM team t LEFT JOIN t.members m
```

이 코드는 팀과 팀이 보유한 회원목록을 **컬렉션 값 연관 필드**로 외부 조인한 코드 이다.

## 세타 조인

WHERE 절을 사용해서 세타 조인을 할 수 있다.

- 세타 조인은 **내부 조인만** 지원한다.

```java
select count(m) from Member m, Team t
where m.username = t.name
```

# 페치 조인

페치 조인은 JPQL에서 **성능 최적화**를 위해 제공하는 기능이다. 

- 연관된 엔티티나 컬렉션을 한 번에 같이 조회하는 기능이다.
- join fetch 명령어로 사용할 수 있다.

```java
String jpql = "select m from Member m join fetch m.team";
List<Member> members = em.createQuery(jpql, Member.class).getResultList();

for(Member member : members) {
	// 페치 조인으로 회원과 팀을 함계 조회해서 지연 로딩 발생 안 함
	System.out.println("username = " + member.getUsername() + ", " +
		"teamname = " + member.getTeam().name());
}
```

회원과 팀을 지연 로딩으로 설정했을 때, 회원을 조회할 때 **페치 조인**을 사용해서 팀도 함께 조회했으므로 연관된 팀 엔티티는 **프록시가 아닌 실제 엔티티**가 된다.

- 연관된 팀을 사용해도 **지연로딩**이 일어나지 않는다.
- 회원 엔티티가 **중영속 상태가 되어도** 연관된 팀을 조회할 수 있다.

# 페치 조인과 DISTINCT

JQPL의 **DISTINCT** 명령어는 SQL에 DISTINCT를 추가하고 **애플리케이션에서 한 번 더 중복**을 제거한다.

# 페치 조인과 일반 조인의 차이

- 일반 조인의 JQPL은 결과를 반환할 때 **연관관계까지 고려하지 않는다.** 단지 SELECT 절에 지정한 엔티티만 조회한다.
- 페치 조인은 연관된 엔티티도 함께 조회한다.

# 페치 조인의 특징과 한계

- **글로벌 로딩 전략**은 될 수 있으면 지연 로딩으로 사용하고 **최적화가 필요한 시점**에 페치 조인을 적용하는 것이 효과적이다.
- 페치 조인 대상에는 **별칭**을 줄 수 없다.
- **둘 이상**의 컬렉션을 페치할 수 없다.
- 컬렉션을 페치 조인하면 **페이징 API**를 사용할 수 없다.

# 경로 표현식

경로 표현식은 쉽게 말해 .(점)을 찍어 **객체 그래프를 탐색**하는 것이다.

# 경로 표현식의 용어 정리

- 상태 필드 : 단순히 값을 저장하기 위한 필드
- 연관 필드 : 연관관계를 위한 필드, 임베디드 타입 포함
    - 단일 값 연관 필드 : @ManyToOne, @OneToOne, 대상이 엔티티
    - 컬렉션 값 연관 필드 : @OneToMany, @ManyToMany, 대상이 컬렉션

# 경로 표현식과 특징

- **상태 필드 경로** : 경로 탐색의 끝이다. 더는 탐색할 수 없다.
- **단일 값 연관 경로 : 묵시적으로 내부 조인**이 일어난다. 단일 값 연관 경로는 계속 탐색할 수 있다.
- **컬렉션 값 연관 경로 : 묵시적으로 내부 조인**이 일어난다. 더는 탐색할 수 없다.

단일 값 연관 필드로 경로 탐색을 하면 SQL에세 **내부 조인**이 일어나는데 이것이 묵시적 조인이라 한다. 묵시적 조인은 모두 내부 조인인다.

- **명시적 조인** : JOIN을 직접 적어주는 것
- **묵시적 조인** : 경로 표현식에 의해 묵시적으로 조인이 일어나는 것