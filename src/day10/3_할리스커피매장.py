
# 1. 모듈
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

# [code 1]
def hollys_store(result):
    for page in range(1, 51):  # 1 ~ 50 까지 반복
        # 할리스 매장 정보 url
        url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}'
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, "html.parser")
        tbody = soup.select_one('tbody')
        for row in tbody.select('tr'):
            if len(row) <= 3: break
            tds = row.select('td')
            store_sido = tds[0].string;  # print(store_sido)
            store_name = tds[1].string;  # print(store_name)
            store_address = tds[3].string;  # print(store_address)
            store_phone = tds[5].string;  # print(store_phone)
            store = [store_name, store_sido, store_address, store_phone] # 매장 정보 1개당 리스트 1개
            result.append(store)  # 리스트 안에 리스트요소 추가 : 2차원 리스트 # [ [] , [] , [] ]

# [code 0]
def main():
    result = []  # 할리스 매장정보 리스트를 여러개 저장하는 리스트 변수 , 2차원 리스트
    print('>>>> 할리스 매장 크롤링 중 >>>>')
    hollys_store(result)
    print(result)
    # py 2차원 리스트 객체를 DataFrame 객체로 변환
    tbl = pd.DataFrame( result , columns = (  'store' , 'sido-gu' , 'address' , 'phone'))
    # DataFrame 객체를 csv파일로 생성
    tbl.to_csv('hollys.csv' , encoding="cp949" , mode= 'w' , index=False)


if __name__ == "__main__":
    main()











