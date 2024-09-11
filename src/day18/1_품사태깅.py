
'''
    - 형태소 : 의미가 있는 가장 작은 단위
    - 단어 : 의미를 갖는 문장의 가장 작은 단일 요소 , # 문장내 에서 분리 될수 있는 부분 , 형태소 , 접사 구분
    - 품사 태깅 : 형태소의 뜻과 문맥을 고려하여 품사를 붙인것
    - 품사 태깅 패키지 : konlpy ( 자바 기반의 소프트웨어 , 자바 설치가 필요함 )
'''
# [1]
# 1. 모둘 호출
from konlpy.tag import Okt
    # 1. java 버전 확인 : cmd --> java -version 입력후 확인
    # 2. 

# 2. 분석할 한글
text = "나는 사과를 먹었다"

# 3. 품사 태깅
    # 3-1. 품사 태깅 객체 생성
okt = Okt()
    # 3-2 품사 태깅 함수 실행 # okt.pos( 분석할문장 )
tag_words = okt.pos( text )

# 4. 확인
print(tag_words)
# [
# ('나', 'Noun'), # Noun 명사
# ('는', 'Josa'), # Josa 조사
# ('사과', 'Noun'), # Noun 명사
# ('를', 'Josa'), # Josa 조사
# ('먹었다', 'Verb') # Verb 동사
# ]

# [2] 예제 2
# 2. 분석 할 한글
text = '앞으로 조달청의 계약 방법 변경 후 기본 및 실시설계를 진행하고, 2025년 하반기에 가격협상과 본계약을 체결한 후 2025년 말 착공할 계획이다.김인수 인천시 교통국장은 7공구 강화-김포 구간은 강화대교와 초지대교의 상습 정체를 해소하기 위해 우선 착공이 반드시 필요하다며 한국도로공사와 긴밀히 협력해 최대한 착공 시점을 앞당길 수 있도록 노력하겠다고 밝혔다.한편, 계양-강화 고속도로 사업은 공사구간이 총 7개로 구성돼 있으며, 1~6공구는 2022년부터 기본 및 실시설계를 진행 중이다. 올해 안에 설계가 완료될 예정이다.출처 : 인천투데이(http://www.incheontoday.com) '

# 3. 품사 태깅
okt = Okt()

#tag_words = okt.pos(text)
tag_words = okt.nouns(text) # .nouns() 명사 만 반환 분석

# 4. 확인
print(tag_words)
# ['앞', '조달청', '계약', '방법', '변경', '후', '기본', '및', '실시', '설계', '진행', '하반기', '가격', '협상', '본계약', '체결', '후', '말', '착공', '계획', '김', '인수', '인천', '시', '교통', '국장', '공구', '강화', '김포', '구간', '강화대교', '초지대교', '상습', '정체', '해소', '위해', '우선', '착공', '반드시', '한국', '도로공사', '협력', '최대한', '착공', '시점', '수', '노력', '한편', '계양', '강화', '고속도로', '사업', '사구간', '총', '개', '구성', '공구', '기본', '및', '실시', '설계', '진행', '중이', '올해', '안', '설계', '완료', '예정', '출처', '인천', '투데이']

# 5. 요소 중복 수 계산 # Counter() # 요소들의 중복 개수 계산 객체
from collections import Counter
wordCount = Counter(tag_words)
print(wordCount)
# Counter({'설계': 3, '착공': 3, '후': 2, '기본': 2, '및': 2, '실시': 2, '진행': 2, '인천': 2, '공구': 2, '강화': 2, '앞': 1, '조달청': 1, '계약': 1, '방법': 1, '변경': 1, '하반기': 1, '가격': 1, '협상': 1, '본계약': 1, '체결': 1, '말': 1, '계획': 1, '김': 1, '인수': 1, '시': 1, '교통': 1, '국장': 1, '김포': 1, '구간': 1, '강화대교': 1, '초지대교': 1, '상습': 1, '정체': 1, '해소': 1, '위해': 1, '우선': 1, '반드시': 1, '한국': 1, '도로공사': 1, '협력': 1, '최대한': 1, '시점': 1, '수': 1, '노력': 1, '한편': 1, '계양': 1, '고속도로': 1, '사업': 1, '사구간': 1, '총': 1, '개': 1, '구성': 1, '중이': 1, '올해': 1, '안': 1, '완료': 1, '예정': 1, '출처': 1, '투데이': 1})

# 6. 특정 상위 n개 반환 함수 # .most_common(N)  # 상위 N개의 단어 반환 함수
print(wordCount.most_common(4))
# [('설계', 3), ('착공', 3), ('후', 2), ('기본', 2)]








