### 주제 : 내 ERD를 보고 REST 형식에 맞게 API 디자인하기
상세내용
1. 파이썬&FastAPI 코드말고 엑셀 혹은 워드 등 문서로 작성할 것
(코드는 본인이 별도로 작성하여 깃허브에 올려도 됨, 본 과제의 필수사항은 아님)
2. API 디자인시에 반드시(!) 포함되어야 할 것
- HTTP 메서드
- 리소스 식별할 수 있는 path
- 리소스의 식별할 수 있는 식별자 아이디 또는 쿼리 파라메터
- 요청 Body가 있다면 요청 Body의 key, value, datatype 기입
- 응답 Body가 있다면 응답 Body의 key, value, datatype 기입
- 복수의(multiple) 응답 결과가 있을 경우 몇건, start-end를 기준할 수 있는 식별자 기입
3. 작성 시 참고사항
- GET : 단수 혹은 복수의 데이터를 조회하도록 됨
( 추상화됨 함수 이름 : findOne(), findAll() )
- POST : 보통 1개의 데이터를 Body를 통해 추가하도록 구현 됨 (복수는 예외사항)
( 추상화됨 함수 이름 : insertOne() )
- DELETE : 1개의 식별자를 통해 특정 데이터를 삭제하도록 됨
( 추상화됨 함수 이름 : deleteOne() )
- PUT :  보통 1개의 데이터를 Body와 식별자id 통해 해당 Body의 전문으로 갱신하도록 됨
( 추상화됨 함수 이름 : updateOne() )
- PATCH : 보통 1개의 데이터를 Body와 식별자id 통해 해당 Body 부분만 갱신하도록 됨
( 추상화됨 함수 이름 : updateOne() )

---
### Users Table
**생성** : `POST /users/`
```json
// 요청body
{
	"UserID" : "abc123",
	"Password" : "qwer1234",
	"NickName" : "하이하이",
	"Email" : "abc123@naver.com",
	"ProfileImage" : "/이미지경로/",
}
```

**조회** : `GET /users/{UserID}` 
- UserID 에 해당하는 유저의 정보를 조회합니다.

**업데이트** : `PATCH /users/{UserID}`

<br>

```json
// 회원의 비밀번호를 변경했을 때
{
	"Password" : "1234qwer"
}
```

```json
// 이메일 인증 등을 완료 했을 때
{
	"is_verified" : 1
}
```

```json
// 프로필사진을 수정하거나 추가할 때
{
	"ProfileImage" : "ImageStorage_URL"
}
```
**삭제** `DELETE /users/{UserID}`
- 해당 유저가 회원탈퇴시, 계정을 삭제합니다.

---
### NEWS Table

**기사 게시글 추가** : `POST /news/`
- 조건에 맞는 뉴스게시글을 포스팅합니다.
```json
{
    "Title": "기사 제목",
    "Content": "기사 내용",
    "Summary": "기사 요약본",
    "NewsCompany": "언론사 이름",
    "NewsCategory": "기사 카테고리",
    "Author": "기자 이름",
    "image_url": "기사에 삽입된 이미지 URL",
    "source_url" : "기사 원문 URL",
}
```

**기사 제목검색** : `GET /news?Title={기사제목}`
<br>
**기사 카테고리별 검색** : `GET /news?category=1,2,3`
- 기사를 카테고리별로 검색합니다.
서버에는 or 연산자로 처리할 것
```sql
SELECT * FROM news WHERE category = 1 OR category = 2;
```
<br>

---
