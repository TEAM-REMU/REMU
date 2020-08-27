from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv
import re

file_name = 'data'

# csv 파일 열기
f = open(f'{file_name}.csv','w', newline='')
wr = csv.writer(f, lineterminator='\n')

# 뮤하이브 URL에 접근해서 HTML을 파싱한다
url = 'http://muhive.net/'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
main_html = urlopen(req).read()
soup = BeautifulSoup(main_html, 'html.parser')

# 초성 자음과 감독 이름을 뽑아내자
# URL 상에 그렇게 접근해야 감독별 뮤비 데이터를 추출할 수 있음 ex) http://muhive.net/k-pop-music-video-directors/ㄱ/고유정/
directors_with_html = soup.find_all("a", {"class" : "fusion-bar-highlight"})
spell_pattern = r"<span class=\"menu-text\">.*</span>"
director_pattern = r"<span>.*</span>"

spell = ''
director = ''
for director_with_html in directors_with_html:
    spell_with_span_tag = re.findall(spell_pattern, str(director_with_html))
    if (len(spell_with_span_tag) != 0) :
        if ('Home' not in spell_with_span_tag[0] and 'About Us' not in spell_with_span_tag[0]) :
            spell = spell_with_span_tag[0][24:len(spell_with_span_tag) - 8]

    director_with_span_tag = re.findall(director_pattern , str(director_with_html))
    if (len(director_with_span_tag) != 0) :
        director = director_with_span_tag[0][6:len(director_with_span_tag) - 8]

    if (spell != '' and director != ''):
        url = f'http://muhive.net/k-pop-music-video-directors/{spell}/{director}/'
        print(url)

########################################################################################################################
# 이후 작업은 위에서 진행한 것처럼, 추출하고자 하는 데이터가 있는 URL에 접근해서, 관련 데이터가 가지고 있는 규칙(태그명, 정규표현식 등)을 찾아내야 합니다 #
########################################################################################################################

################
# 최종 데이터 예시 #
################

# CSV 헤더 예시
wr.writerow(['감독 이름','프로덕션 이름', '감독 이미지 주소', '뮤비 제목', '아티스트', '발매 날짜'])

# 데이터 저장 예시
wr.writerow(['유인근','중앙대 멋사', '내 사진', '세훈이가 부르는 노래', '인세훈', '2020-08-27'])

f.close()