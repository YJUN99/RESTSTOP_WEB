from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, datetime
from typing import Annotated, Union, Optional


import logging
import sys
mylogger = logging.getLogger("mylogger")
formatter = logging.Formatter("[%(levelname)s] %(message)s")
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
mylogger.addHandler(handler)
mylogger.setLevel(logging.DEBUG)
app = FastAPI()
## temporay db table
_sample_users = [
    { "id": 1, "nickName": "james1", "created_at": date.today()},
    { "id": 2, "nickName": "james2", "created_at": date.today()},
    { "id": 3, "nickName": "james3", "created_at": date.today()}
]

class Users(BaseModel):
    UserID: str
    Password: str
    NickName: str
    Email : str
    ProfileImage : str
    is_verified : bool = False
    createAt : Union[datetime,None] = datetime.now()
    
class UserUpdate(BaseModel):
    Password: Optional[str] = None
    ProfileImage: Optional[str] = None
    is_verified: Optional[bool] = None

class LoginUser(BaseModel):
    UserID: str 
    Password : str
    
class News(BaseModel):
  postID: int
  Title: str
  author: str
  createdAt: Union[str,None] = datetime.now() 
  Summary: str
  likes: int
  views : int
  comments: int

class Likes(BaseModel):
    UserID: str
    PostID: int

class Comments(BaseModel):
    UserID: str
    Content : str
    
class CommentsUpdate(BaseModel):
    UserID: str
    Content : str

class Boards(BaseModel):
    Title: str
    UserID: str
    Image : str
    Content : str
    Category : int
    CreatedAt: Union[str,None] = datetime.now() 
    likes : int = 0
    views : int = 0
    
@app.post("/users")
async def CreateUser(user: Users):
    mylogger.debug(user)
    return {"message": "회원가입 완료"}

@app.get("/users/{userID}")
async def ReadUser(userID):
    mylogger.debug(userID)
    return {"message": "회원정보 가져오기 성공"}

@app.patch("/users/{userID}")
async def ChangeInfoUser(userID: str, user_update : UserUpdate):
    mylogger.debug(user_update)
    return {"message": "회원정보 변경 성공"}

@app.delete("/users/{userID}")
async def deleteUser(userID: str):
    mylogger.debug(userID)
    return {"message": "회원정보 삭제 성공"}

@app.post("/login")
async def LoginUser(user: LoginUser):
    mylogger.debug(user)
    return {"message": "로그인 완료"}

@app.get("/news")
async def getNews():
    # DB query를 통한 뉴스 목록을 리스트화 하여 리턴할 것
    return {"message" : "뉴스 전체 목록 가져오기 성공"}


@app.delete("/news/{newsID}")
async def delNews(newsID : int):
    mylogger.debug(newsID)
    # 삭제하는 user가 관리자 권한을 가지고 있는지 체크할 것
    return {"message" : "newsID 에 해당하는 뉴스 정보 삭제"}

@app.post("/news/{newsID}/likes")
async def addLikes(newsID : int, user:Likes):
    mylogger.debug(user)
    return {"message" : "news에 좋아요 추가 완료"}

@app.post("/news/{newsID}/comments")
async def createNewsComments(newsID : int, comment : Comments):
    mylogger.debug(comment)
    return {"message" : "newsComment 추가 완료"}
    
@app.patch("/news/{newsID}/comments/{commentsID}")
async def patchNewsComments(newsID : int, commentsID: int, comment : CommentsUpdate):
    mylogger.debug(newsID , "기사에 대한", commentsID, "번 댓글을" , comment , "로 수정합니다.")
    return {"message" : "newsComment 수정완료"}

@app.delete("/news/{newsID}/comments/{commentsID}")
async def deleteNewsComments(newsID : int, commentsID : int):
    mylogger.debug("댓글삭제완료")
    return {"message" : "댓글 삭제완료"}

### 아래는 board 관련 

@app.post("/boards")
async def createBoard(board : Boards):
    mylogger.debug(board, "자유게시글 포스팅완료")
    return {"message" : "자유게시글 포스팅 완료"}
    

@app.get("/boards")
async def getBoard():
    # DB query를 통한 뉴스 목록을 리스트화 하여 리턴할 것
    return {"message" : "자유게시글 전체 목록 가져오기 성공"}


@app.delete("/boards/{boardID}")
async def delBoards(boardID : int):
    mylogger.debug(boardID)
    return {"message" : "boardID 에 해당하는 뉴스 정보 삭제"}

@app.post("/boards/{boardID}/likes")
async def addBoardsLikes(boardID : int, user:Likes):
    mylogger.debug(user)
    return {"message" : "boards에 좋아요 추가 완료"}

@app.post("/boards/{boardID}/comments")
async def createBoardsComments(boardID : int, comment : Comments):
    mylogger.debug(comment)
    return {"message" : "Comment 추가 완료"}
    
@app.patch("/boards/{boardID}/comments/{commentsID}")
async def patchBoardsComments(boardID : int, commentsID: int, comment : CommentsUpdate):
    mylogger.debug(boardID , "게시글에 대한", commentsID, "번 댓글을" , comment , "로 수정합니다.")
    return {"message" : "boardIDComment 수정완료"}