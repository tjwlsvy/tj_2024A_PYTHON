# 네이버api 블로그에서 월드컵에 대한 검색결과 크롤링하여 파일로 저장
import json
import urllib.request

# 개발자 개발자센터에서 애플리케이션 신청후 발급받은 키 와 비밀번호
네이버키 = 'OSlBD4LFnlP4TPplI24V'
네이버비밀번호 = 'M2tva3NqRZ'


#[code 2]
def getRequestUrl(url):
    요청객체 = urllib.request.Request(url)
    요청객체.add_header("X-Naver-Client-Id", 네이버키)
    요청객체.add_header('X-Naver-Client-Secret', 네이버비밀번호)

    try:
        응답객체 = urllib.request.urlopen(요청객체)
        print(f'>>> code2 요청 URL 상태 : {응답객체.getcode()}')
        if 응답객체.getcode() == 200:   # 만약 응답의 상태가 2xx이면
            return 응답객체.read().decode('utf-8') # 실행된 url내 모든 내용물 읽음.
    except Exception as e:
        return None # 아니면 none

# [code 3] 매개변수로 검색대상 , 검색어 , 사직번호  , 한번에 표기할 개수
def getNaverSearch( node , srcText , page_start , display ) :
    base = "https://openapi.naver.com/v1/search"
    node = f'/{node}.json'
    parameters = f'?query={urllib.parse.quote(srcText)}&start={page_start}&display={display}'  # 3. 요청url의 파라미터
    url = base + node + parameters
    print(f'>>> code3 요청 URL : {url}')
    responseDecode = getRequestUrl(url)
    if responseDecode == None : return None
    else: return json.loads(responseDecode)

# [code 4]
def getPostData( post , jsonResult , cnt ):
    title = post['title']
    description = post['description']
    bloggerlink = post['bloggerlink']
    link = post['link']

    dic = {'cnt' : cnt , 'title' : title , 'description' : description , 'bloggerlink' : bloggerlink , 'link' : link}
    jsonResult.append( dic )

# [code 1]
def main():
    node = 'blog'   # 크롤링할 대상
    srcText = input('검색어 입력하세요 :')  # 사용자 입력으로 받은 검색어 변수
    cnt = 0 # 검색 결과 개수
    jsonResult = [] # 검색 결과를 정리하여 저장할 리스트 변수

    jsonResponse = getNaverSearch( node , srcText , 1 , 100 )
    print(f'>>> code1 jsonResponse: {jsonResponse}')
    total = jsonResponse['total']

    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post , jsonResult , cnt)
        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch( node , srcText , start ,100)
    print( f'전체 검색 : { total }건')
    print( f'가져온 데이터(무료기준) : { cnt }건')

    with open(f'{srcText}-naver-{node}.json' , 'w' , encoding='utf-8') as file:
        jsonFile = json.dumps(jsonResult , indent=4 , sort_keys=True , ensure_ascii= False)
        file.write(jsonFile)

if __name__ == "__main__":
    main()



