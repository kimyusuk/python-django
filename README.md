우선 기본적으로  
파이참과 db browser for sqlLite가 깔려있어야 한다.  
db는 projects에 mysite에 db.sqlite3을 수정해서 사용하면 된다.  
  
장고 실행 방법.  
장고 가상환경 만드는 법. 
venvs라는 폴더를 만들어서 진행 했다.  
cmd에서 venvs 폴더에 진입한 후 python -m venv mysite 명령어를 쳐 준다.  
이뜻은 venvs 폴더 안에서 mysite라는 가상환경을 만든다 라는 뜻이다.  
  
이후 가상환경에 진입 해준다.  
진입 방법은 C:\venvs\mysite\Scripts>activate.bat 이다.  
진입 후 장고 설치 방법은  
(mysite) C:\venvs\mysite\Scripts>pip install django==4.0.3 이다.  

깃에 올린 projects 폴더를 내려 받은 후  
projects폴더를 c드라이브에 넣은 뒤  
가상환경을 실행 한다. 실행 방법은 아래와 같다.  
C:\projects>C:\venvs\mysite\Scripts\activate 이후  
  
(mysite) c:\projects\mysite> 이런 모양이 됐다면  
python 프로젝트에서 가상환경이 정상적으로 실행 된 것이다.  
이후 python manage.py runserver로 로컬 호스트에 접속 해주면 된다.  
주소값은 http://127.0.0.1:8000 이다. 

기본적으로는 자유 게시판 형태고.  
로그인 기능이 있으며.  
게시판에서 영화 무비차트를   
네이버에서 최신 순으로   
크롤링 하는 bs4 = BeautifulSoup   
기술을 사용했다.  
