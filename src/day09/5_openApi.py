import json
import urllib.request

# 서울 열린데이터 광장에서 '상상대로 서울 자유제안 정보' 을 크롤링하여 json 파일로 저장

인증키 = '4c656c6672746a7738304761545253'



# [code 2]
def getRequestUrl(url):
    요청객체 = urllib.request.Request(url)
    try:
        응답객체 = urllib.request.urlopen(요청객체)
        if 응답객체.getcode() == 200 :
            return 응답객체.read().decode('utf-8')
    except Exception as e:
        return None

# [code 3]
def getSeoulItem( start_index , end_index ):
    base = '"http://openapi.seoul.go.kr:8088/'
    parameters = f'?_type=json&serviceKey={인증키}'
    parameters += f'/{start_index}'
    parameters += f'/{end_index}'
    url = base + parameters

    responseDecode = getRequestUrl(url)
    if responseDecode == None : return None
    else: return json.loads(responseDecode)

# [code 4]
def getSeoulService(start_index , end_index ):
    jsonResult = []
    jsonData = getSeoulItem(start_index, end_index)

    if jsonData != None :
        for item in jsonData['ChunmanFreeSuggestions']['row']:
            num = item["SN"]  # 데이터 각각 추출해서 가져옴
            title = item["TITLE"]
            content = item["CONTENT"]
            score = item["VOTE_SCORE"]
            date = item["REG_DATE"]
            dic = {"SN": num, "TITLE": title, "CONTENT": content, "VOTE_SCORE": score, "REG_DATE": date}
            jsonResult.append(dic)
        else:
            return
        return jsonResult


# [code 1]
def main():
    start_index = int(input('제안시작번호: '))
    end_index = int(input('제안끝번호: '))

    jsonResult = []
    # getSeoulService 에 제안번호 , 제안제목 , 제안내용 , 제안특표 , 제안등록일자 저장
    jsonResult = getSeoulService(start_index , end_index  )

    with open(f"ChunmanFreeSuggestion__{start_index}__{end_index}.json","w",encoding="utf-8") as file :
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        file.write(jsonFile)

if __name__ == "__main__" :
    main()