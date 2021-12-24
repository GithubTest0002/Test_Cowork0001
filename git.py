# 1. git 설치 및 github 가입
# 2. git bash 환경설정
# git config --global user.name "원하는 이름"
# git config --global user.email "github 가입한 이메일"
# git config --list # 정보 확인 : 유저이름, 가입 이메일 나옴
# github 처음 코드 업로드
# git init  # 현재 위치에 저장소 생성. (초기화)
# git add .  # 모든 파일 추가  / git add 파일이름  # 특정 파일 추가
# git status   # 상태확인
# git commit -m "first commit"  # 히스토리 만들기. m 은 메세지란 의미. 즉 히스토리 이름
# git remote add origin ~~~ # github repository와 내 PC 연결.
#                             이부분은 처음에 github에 나오는 부분 그대로 복붙
# git remote -v   # 잘 연결된것 확인. 주소값이 나옴
# git push origin master  # github 올리기

# Github에 계속 업데이트 할 때
# git add .  #  파일 추가
# git commit -m ""
# git push origin master  # github로 올리기

# Github 팀프로젝트 할 때 - 이게 주 목적 중 하나
# git clone 주소 폴더이름(지정하고 싶을 경우)   # 주소는 github에 잇음
# git checkout -b "브랜치이름"    # Github에 내 브ㅐㄴ치 만들기
# git add "파일이름"
# git commit -m "히스토리명"
# git push origin "브랜치이름"
# git pull origin master    # 마스터 브랜치서 소스 가지고 온다
# git checkout "브랜치이름"   # 브랜치에서 이동할 때.
