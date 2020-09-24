from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import csv
import re

file_name = 'data'

# spell = ''

director_urls=[]
director_sns_urls=[]
director = ''
upload_date = ''
artist = ''
title = ''
production = ''
video_link = ''


# csv 파일 열기
f = open(f'{file_name}.csv','w', encoding="UTF-8", newline='')
wr = csv.writer(f, lineterminator='\n')


# CSV 헤더 
wr.writerow(['감독 이름', '감독 이미지 주소', '감독 SNS 링크', '프로덕션 이름', '프로덕션 이미지 주소', '뮤비 제목', '뮤비 주소', 
            '아티스트', '뮤비 업로드 날짜', '감독이 바뀌는 지점'])


# 뮤하이브 URL에 접근해서 HTML을 파싱한다   
url = 'http://muhive.net/'
req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
main_html = req.text
soup = BeautifulSoup(main_html, 'html.parser')

# 초성 자음과 감독 이름을 뽑아내자
# URL 상에 그렇게 접근해야 감독별 뮤비 데이터를 추출할 수 있음 ex) http://muhive.net/k-pop-music-video-directors/ㄱ/고유정/
#directors_with_html = soup.find_all("a", {"class" : "fusion-bar-highlight"})
directors_with_html = soup.select('.sub-menu > li > a')

#ㄱ,ㄴ,ㄷ 이런거 가져오려고 
# spell_pattern = re.compile('<span class="menu-text">.*</span>')

#감독 이름 가져오려고 
director_pattern = re.compile('<span>.*</span>')


#감독별 페이지 가져오려고
for director_with_html in directors_with_html:
    director_url = director_with_html['href']
    director_urls.append(director_url)
    # spell_with_span_tag = spell_pattern.findall(str(director_with_html))

    # if (len(spell_with_span_tag) != 0) :
    #     if ('Home' not in spell_with_span_tag[0] and 'About Us' not in spell_with_span_tag[0]) :
    #         #spell에는 ㄱ,ㄴ,ㄷ,~ 이런거 들어간대
    #         spell = spell_with_span_tag[0][24:len(spell_with_span_tag) - 8]

    # director_with_span_tag = director_pattern.findall(str(director_with_html))

    # if (len(director_with_span_tag) != 0) :
    #     director = director_with_span_tag[0][6:len(director_with_span_tag) - 8]
    # else : 
    #     director = ''

    # if (spell != '' and director != ''):
    #     director_urls.append(f'http://muhive.net/k-pop-music-video-directors/{spell}/{director}/')


#감독별 페이지 들어가서 노래별 페이지 들어가고 그 안에서 mv 관련 데이터 뽑아내기 
for director_url in director_urls:


    req = requests.get(director_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    #감독 개인페이지에서 sns링크 뽑아내기
    director_sns_htmls = soup.select('.fusion-social-links > .fusion-social-networks > .fusion-social-networks-wrapper > a')
    #감독 개인 페이지에 있는 곡 목록중에 하나씩 링크 뽑아내기
    mv_list_page_html = soup.select('.lcp_catlist > li > a')

    del director_sns_urls[:]
    for director_sns_html in director_sns_htmls:
        #감독의 개인 sns 종류는 굳이 따로 뽑아내지 말고 그냥 도메인으로 나중에 처리하장
        #director_sns_name = director_sns_html['data-title'] 
        director_sns_urls.append(director_sns_html['href'])

   
    for mv_page_html in mv_list_page_html:
        #mv_url에는 곡 하나당 링크가 들어감 
        mv_url = mv_page_html['href']
        req = requests.get(mv_url, headers={'User-Agent': 'Mozilla/5.0'})
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        #뮤비 링크 뽑아내기
        mv_link_html = soup.select('.post-content > .video-shortcode > iframe')
        mv_link_pattern = re.compile('https://www.youtube.com/embed/.*?feature=oembed')
        mv_link = mv_link_pattern.findall(str(mv_link_html))


        #mv_link_pattern에 안맞는 뮤비는 그냥 링크 없다고 취급
        #ex)고태민 감독님의 박재정-두남자
        if(len(mv_link) == 0) :
            video_link = ''
        else :
            video_link = mv_link[0][30:-15]
        

        #곡별 링크 타고 들어가서 감독, 아티스트, 발매일 등 정보 뽑아내기
        mv_info_html = soup.select('.post-content > ul')
        mv_info_pattern = re.compile('<li>.*')
        mv_infos = mv_info_pattern.findall(str(mv_info_html))

       
        for mv_info in mv_infos:
            if('Date' in mv_info):
                #뮤하이브에 뮤비 업로드 날짜 형식이 각각 달라서 형식 맞춰주기 위한 코드
                #ex)2020.01.12 → 2020-01-12
                upload_date = mv_info[11:-5].strip().replace('.','-')
                #ex)2020-1-12 → 2020-01-12 
                #if(len(upload_date) != 10):
                   #upload_date = upload_date[0:5]+'0'+upload_date[5:]
          
            elif('Artist' in mv_info):  
                artist = mv_info[12:-5].strip()
    
            elif('Song Title' in mv_info):
                title = mv_info[16:-5].strip()
     
            elif('Director' in mv_info):
                director = mv_info[14:-5].strip()

            elif('Production' in mv_info):
                if('</li>' not in mv_info):
                    production = mv_info[16:].strip()
                else:
                    production = mv_info[16:-5].strip()
         
        #print(director, '', ','.join(director_sns_urls), production, '', title, video_link, artist, upload_date)
        wr.writerow([director, '', ','.join(director_sns_urls), production, '', title, video_link, artist, upload_date])
        

        director = ''
        production = ''
 
########################################################################################################################
# 이후 작업은 위에서 진행한 것처럼, 추출하고자 하는 데이터가 있는 URL에 접근해서, 관련 데이터가 가지고 있는 규칙(태그명, 정규표현식 등)을 찾아내야 합니다 #
########################################################################################################################

################
# 최종 데이터 예시 #
################




f.close()
