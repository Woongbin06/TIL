## HTTP 메시지

- HTTP에서 교환하는 정보를 HTTP 메시지라고 한다.
- 복수 행(개행 문자는 CR + LF)의 데이터로 구성된 텍스트 문자열이다.
- 메시지 헤더와 메시지 바디로 구성되어 있다.
- 최초에 나타나는 개행 문자로 메시지 헤더와 바디를 구분한다.

### 리퀘스트 메시지
리퀘스트 메시지의 메시지 헤더에는 리퀘스트 라인, 리퀘스트 헤더 필드, 일반 헤더 필드, 엔티티 헤더 필드 등이 포함되어있다.

- 리퀘스트 라인 : 메소드와 리퀘스트 URI와 HTTP 버전이 포함되어있다.
- 헤더 필드 : 여러 조건과 속성 등을 나타내는 각종 헤더 필드가 포함된다.

### 리스폰스 메시지 
리스폰스 메시지의 메시지 헤더에는 리퀘스트 메시지와 거의 같지만 리퀘스트 라인 대신 상태 라인이 포함되어 있다.

- 상태 라인 : 리스폰스 결과를 나타내는 상태 코드와 설명, HTTP 버전이 포함되어있다.

***

## 인코딩

HTTP로 데이터를 전송할 대 인코딩을 하면 전송 효율을 높일 수 있다.

### 메시지 바디와 엔티티 바디의 차이
- 메시지 : 옥텟 시퀀스 단위로 구성된다.
- 엔티티 : 엔티티 헤더 필드와 엔티티 바디로 구성된다.

HTTP 메시지 바디는 리퀘스트랑 리스폰스에 관한 엔티티 바디를 운반한다.

### 콘텐츠 코딩
콘텐츠 코딩은 파일을 압축하고 보내는 것이 가능한 기능이다.   
콘텐츠 코딩은 엔티티에 적용하는 인코딩을 가리키는데 엔티티 정보를 유지한채로 압축한다.

콘텐츠 압축에는 아래와 같은 것이 있다.
- gzip (GNU zip)
- comporess (UNIX의 표준 압축)
- deflate (zlib)
- identity (인코딩 없음)

### 청크 전송 코딩

사이즈가 큰 데이터를 전송 할 때는 엔티티 바디를 분할해서 전달할 수 있는데 이 기능을 청크 전송 코딩이라고 한다.

***

## 멀티파트

HTTP는 멀티파트에 대응하고 있어 하나의 메시지 바디 내부에 엔티티를 여러개 포함시킬 수 있다.   
주로 이미지나 텍스트 파일 등을 업로드할 때 사용된다.

### 종류

- mulitpart/form-data : Web 폼으로부터 파일 업로드에 사용된다.
- multipart/byeranges : 상태 코드 206 리스폰스 메시지가 복수 범위의 내용을 포함하는 때에 사용된다.

***

## 레인지 리퀘스트

사용자가 데이터를 다운로드 중에 커넥션이 끊기면 처음부터 다운로드 하지 않게 리줌이라는 기능을 사용했다.   
`리줌`은 이전에 다운로드 한 곳에서부터 다시 다운로드를 하는 것이다.   
리줌을 할려면 엔티티의 범위를 지정해서 리퀘스트 해야하는 데 이를 `레인지 리퀘스트`라고 한다.

***

## 콘텐츠 네고시에이션

웹에서 같은 콘텐츠이지만 여러 개의 페이지를 가진 웹 페이지가 있다.

> ex ) 내용은 같지만 영어판과 한국어판이 있는 웹 페이지.

서로 다른 언어를 주로 사용하는 브라우저가 같은 URI에 액세스할 때 각각 영어판 웹 페이지와 한국어판 웹 페이지를 표시하는 구조를 `콘텐츠 네고시에이션(Content Negotitaion)`이라 한다.

- 클라이언트와 서버가 제공하는 리소소의 내용에 대해서 교섭한다.

### 종류

- 서버 구동형 네고시에이션 : 서버 측에서 콘텐츠 네고시에이션을 사용하는 방식이다.
- 에이전트 구동형 네고시에이션 : 클라이언트 측에서 콘텐츠 네고시에이션을 사용하는 방식이다.
- 트랜스페어런트 네고시에이션 : 서버 구동형과 에이전트 구동형을 혼합한 것이다.