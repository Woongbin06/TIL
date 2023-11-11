- 부모 클래스는 테이블과 매핑하지 않고 자식 클래스에게만 매핑 정보를 제공한다.

![](https://velog.velcdn.com/images/choidongkuen/post/277e8205-95c1-41f3-b319-65bb6c168791/image.png)

위 테이블을 보면 공통 속성이 존재하기 때문에 **공통 속성**을 부모 클래스로 모으고 객체 상속 관계로 만들 수 있다.

```java
@MappedSuperclass
public abstract class BaseEntity {
	@Id @GeneratedValue
	private Long id;
	private String name;
}

@Entity
@AttributeOverride(name = "id", column = @Column(name = "MEMBER_ID") // Id 컬렴명 재정의
public class Member extends BaseEntity {
	private String email;
}

@Entity
public class Seller extends BaseEntity {
	private String shopName;
}
```

- BaseEntity는 자식 엔티티에게 공통으로 사용되는 **매핑 정보**만 제공한다.
- @AttributeOverride를 사용하면 원하는 **컬럼명을 재정의**할 수 있다

# 특징

- 테이블과 매핑하지 않고 자식 클래스에 엔티티의 매핑 정보를 상속한다.
- 지정한 클래스는 엔티티가 아니므로 em.find( )나 JPQL에서 사용할 수 없다.
- 이 클래스를 직접 생성해서 사용할 일은 거의 없으므로 추상 클래스로 만드는 것을 권장한다.