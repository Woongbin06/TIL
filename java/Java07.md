# 회원 관리 예제

## 비지니스 요구사항 정리
- 데이터 : 회원ID, 이름   
- 기능 : 회원 등록, 조회   

## 회원 도메인
``` java
public classs Member {
  private Long id;
  private String name;

  public Long getId() {
    return id;
  }
  public void setId(Long id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  } 
}
```
회원의 이름과 아이디를 getter와 setter를 이용해서 받는다. 
> **why ?**    
아이디와 이름을 private으로 만들어서 외부에서 접근할려면 getter와 setter를 사용해야 함.

## 회원 리포지토리 / 인터페이스
``` java
public interface MemberRepository {
  Member save(Member member);
  Optional<Member> findById(Long id); // Optional을 사용하면 null 값이 반환 X
  Optional<Member> findByName(String name);
  List<Member> findAll();
}
```
위 코드는 인터페이스로 회원을 조회할 메소드를 정의만 해놓았다.

### 리포지토리 코드
``` java
public class MemoryMemberRepository ijmplements MemberRepsoitory {
  private static map<Long, Member> store = new HashMap<>();
  private static long sequence = 0L;

  @Override // 회원 저장
  public Member save(Member member) {
    member.setId(++sequence); // 1번 회원, 2번 회원 ....
    store.put(member.getId(), member);
    return member; 
  }

  @Override // 아이디로 조회
  public Optional<Member> findById(Long id) { // Optionall을 쓰는 이유 : null 값을 막기 위해
    return Optional.ofNullable(store.get(id));
  }

  @Override // 이름으로 조회
  public Optional<Member> findByName(String name) {
    store.values().stream() // 처음부터 끝까지 돌리기
            .filter(member -> member.getName().equals(name)) 
            // 찾는 회원의 이름과 같은 것을 찾고 반환.
            .findAny(); // 없으면 NULL반환
  }

  @Override // 전체 조회
  public List<Member> findAll() {
    return new ArrayList<>(store.values());
  }
}
```
위 코드는 간단한 회원 조회 코드인데 이름으로 조회에서 stream()을 이용하여 회원을 처음부터 끝까지 돌리면서 찾는 회원과 이름이 같으면 그 값을 반환한다. Optional을 사용한 이유는 반환되는 값에 NULL 값을 방지하기 위해서이다.

## 회원 리포지토리 테스트 케이스
위에서 작성한 회원 리포지토리가 잘 되는지 테스트하기 위해 테스트 케이스를 작성한다.

``` java
class MemoryMemberRespositoryTest() {
  MemberRepository repository = new MemoryMemberRepository();

  @Test // 회원 저장 테스트
  public void save() {
    Member member = new Member();
    member.setName("spring"); // 1번 spring회원

    repository.save(member);
    Member result = repository.findById(member.getId()).get();
    // Assertions를 static으로 임폴트하면 생략가능.
    Assertions.assertThat(member).isEqualTo(result); 
  }

  @Test // 이름으로 조회
  public void findByName() { 
    Member member1 = new Member();
    member1.setName("spring1");
    repository.save(member1); // spring1 이름으로 회원가입.

    // spring1이라는 이름의 회원을 result에 저장
    Member result = repository.findByName("spring1").get(); 
    // member1의 회원의 이름과 result의 이름이 같으면 테스트 성공.
    assertThat(result).isEqualTo(member1);
  }

  @Test // 전체 조회
  public void findAll() {
    Member member1 = new Member();
    member1.setName("spring1");
    repository.save(member1);
    Member member2 = new Member();
    member2.setName("spring2");
    repository.save(member2);

    List<Member> result = repository.findAll();
    assertThat(result.size()).isEqualTo(2); // 전체 회원 수가 2명이면 테스트 성공.
  }
}
```
테스트 케이스 코드인데 여기서 눈여겨 볼점은 assertThat과 isEqualTo를 이용하여 값을 비교해서 테스트가 성공하는지 확인한다.

## 회원 서비스
회원 리포지토리와 도메인을 이용하여 실제 비지니스 로직을 구성하는 것

### 서비스 코드
``` java
public class MemberService {
  private final MemberRepository memberRepository;

  public MemberService(MemberRepository memberRepository) {
    this.memberRepository = memberRepository; // 외부에서 생성하도록 해주는 것.
  }

  // 회원 가입
  public Long join(Member member) {
    // 같은 이름이 있는 중복 회원 X
    memberRepository.findByName(member.getName())
        .ifPresent(m -> { // 이미 회원이 있으면 실행
          throw new IllegalSttateException("이미 존재하는 회원입니다.");
        });

    memberRepository.svae(member);
    return member.getId();
  }

  // 전체 회원 조회
  public List<Member> findMembers() {
    return memberRepository.findAll();
  }

  // 아이디로 조회
  public Optional<Member> findOne(Long memberId) {
    return memberRepository.findById(memberId);
  }
} 
```
회원 서비스를 구현하고 테스트하기 위해 테스트 케이스를 작성한다.

## 회원 서비스 테스트 케이스
``` java
class MemberServiceTest {

  MemberService memberService;
  MemoryMemberRepository memberRepository;

  @BeforeEach
  public void beforeEach() {
      memberRepository = new MemoryMemberrepository();
      memberService = new memberService(memberRepository);
  }

  @AfterEach // 끝날 때마다 초기화
  public void afterEach() {
    memberRepository.clearStore();
  }

  @Test
  void 회원가입() { // 테스트는 한국어로 적어도 됨.
    // given
    Member member = new Member();
    member.setName("hello");
    // when
    Long saveId = memberService.join(member);
    // then
    Member findMember = memberService.findOne(saveId).get();
    // 저장한 회원의 이름과 찾으려는 멤버의 이름이 같으면 테스트 성공
    assertThat(member.getName()).isEqualTo(findMember.getName()); 
  }

  @Test
  public void 중복_회원_예외() {
    // given
    Member member1 = new Member();
    member1.setName("spring");
    Member member2 = new Member();
    member2.setName("spring");

    // when
    memberService.join(member1);
    IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2)); // 예외 발생한 것을 저장

    assertthat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다."); // 예외가 발생하면 테스트 성공.
  }
}
```