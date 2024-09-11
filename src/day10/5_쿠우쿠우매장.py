
# 전국 쿠우쿠우 매장 정보(번호 , 매장명 , 연락처 , 주소 , 영업시간)
# pandas 이용한 csv 파일로 변환
# 플라스크 이용한 쿠우쿠우 전국 매장 정보 반환하는 http 매핑 정의
    # HTTP(GET) 본인ip:5000/qooqoo
    # (3) 생성된 csv 파일 읽어서( pandas DataFrame ) json 형식을 반환

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from flask import Flask

# [code 1]
def qooqoo_store(result):
    for page in range(1, 7):
        url =  f'http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&page={page}'
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response , "html.parser")
        tbody = soup.select_one('tbody')
        if not tbody:
            continue  # 현재 페이지에 tbody가 없으면 다음 페이지로.
        for row in tbody.select('tr'):
            tds = row.select('td')
            if len(tds) < 5:
                continue
            num = tds[0].text.strip(); #print(num)
            name = tds[1].select('a')[1].text.strip(); #print(name)
            phone = tds[2].text.strip(); #print(phone)
            address = tds[3].text.strip(); #print(address)
            time = tds[4].text.strip(); #print(time)
            store = [ num , name , phone , address , time]
            result.append(store)

# [code 0]
def main():
    result = []
    print('>>> 쿠우쿠우 매장 크롤링 중 >>>>')
    qooqoo_store(result)
    print(result)
    tbl = pd.DataFrame( result , columns=('num' , 'name' , 'phone' , 'address' , 'time'))
    tbl.to_csv("qooqoo.csv" , mode= "w" , index=False)

    return result

# Flask 모듈 가져오기
from flask import Flask
import pandas as pd

# Flask 객체 생성
app = Flask( __name__ )

# HTTP GET 매핑 설정
@app.route('/')
def index() : # 매핑 함수
    result = main()
    return result

# Flask 프레임워크 실행
if __name__ == '__main__' :
    app.run( debug=True ) # debug=True 디버그(콘솔에 정보및오류 출력) 모드





