from django.db import models
#딱히 키값을 주지 않아도 키값을 자동으로 재너레이션 시켜버린다.
from django.contrib.auth.models import User

#질문 클래스 / 질문 테이블
class Question(models.Model): #첫글자만 대문자 형식 장고의 모델형식을 받아야 한다.
    subject = models.CharField(max_length=200) #200크기만큼의 varchar가 만들어진다.
    content = models.TextField() #글자수 제한이 없는 경우
    create_date = models.DateTimeField() #날짜 + 시간
    
    #author필드 추가: 글쓴이
    author = models.ForeignKey(User,on_delete=models.CASCADE) #회원 테이블에 사용자 정보가 삭제되면 Question테이블에 질문 정보도 동일하게 삭제

    #수정일시 추가
    modify_date = models.DateTimeField(null=True,blank=True) #데이터 베이스에서 null 허용, form.is_valid() 입력값 검증시 값이 없어도 된다. blank = True

    def __str__(self):
        return self.subject #이렇게 주면 아이디 값으로 리턴해준다.


#답변 클래스 / 답변 테이블
class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)#답변에 연관된 질문이 삭제되면 답변도 모두 삭제해라
    content = models.TextField() #글자수 제한 x
    create_date = models.DateTimeField() #날짜 + 시간
    modify_date = models.DateTimeField(null=True, blank=True) #답변에 대한 수정일시
    author = models.ForeignKey(User, on_delete=models.CASCADE) #author 필드 추가
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #입력값 Null처리

