# REMU
뮤직비디오 추천 및 리뷰 공유 서비스

## 팀 리뮤
| **Name** |**맡은 역할**|
|:--------:|:-----------:|
|정현조|팀장, 디자인, 개발(Home)|
|오지영|개발(Accounts)|
|윤종원|개발(MV, Search)|
|이주연|개발(Director, Search)|
|유인근|전체 총괄|


## 초기 설정

Window
```bash
git clone https://github.com/TEAM-REMU/REMU.git
python -m venv venv
source venv/scripts/activate
cd remu
pip install
python manage.py runserver
```
Mac
```bash
git clone https://github.com/TEAM-REMU/REMU.git
python3 -m venv venv
source venv/bin/activate
cd remu
pip3 install
python3 manage.py runserver
```

## 커밋 규칙

`[TYPE]: 제목`

|Type|설명|
|:-:|:-:|
|feat|새로운 기능을 추가했을 때|
|fix|버그를 수정했을 때|
|docs|문서를 수정했을 때|
|style|코드 포맷을 바꾸거나 세미콜론 추가하거나 등등 코드에 대한 직접적인 변경이 없는 경우|
|refactor|코드를 리팩토링 한 경우|
|chore|패키지를 수정한 경우 예를 들어 우리 프로젝트에 새로운 thirdparty 모들을 추가한 경우 pip install ~~ 등등|

Ex) 

`[feat]: 로그인 html 추가`

`[fix]: 회원가입 때 form 채우지 않고 전송해도 회원가입 가능하던 버그 수정`
    

