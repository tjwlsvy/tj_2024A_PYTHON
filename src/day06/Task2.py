
# 리스트 활용 , p.77 ~ p.88
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 하나의 이름을 입력받아 여러명의 이름을 저장
#          2. 저장된 여려명의 이름을 모두 출력
#          3. 수정할 이름과 새로운 이름을 입력받아 수정
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 추가적인 전역변수 생성하지 말기
# [조건4] : 최대한 리스트타입 사용하지 않기

# 리스트란? 여러개 자료들을 인덱스로 구분하여 하나의 리스트로 자료 구성

# 전역변수
names = ['유재석','신동엽','강호동'] # 샘플 데이터

# 함수정의 , def 함수명(매개변수 , 매개변수):
def nameCreate():
    global names    # 전역변수 호출
    newName = input('추가할 이름 :')
    names.append(newName)   # 리스트변수.append(새로운값) : 리스트내 마지막 요소 뒤에 새로운값 요소 추가
    return

def nameRead():
    global names    # 전역변수 호출
    for name in names:
        print(f'name:{name}')
    return

def nameUpdate():
    global names    # 전역변수 호출
    oldName = input('oldName :')
    # 만약에 수정할 이름이 존재하지 않으면
    if names.count(oldName) == 0 : return
    else: # 존재하면
        # 수정할 이름의 인덱스 찾기 , 리스트변수명.index(찾을값) : 리스트내 찾을값이 존재하면 인덱스 반환
        index = names.index(oldName)
        # 새로운 이름 입력받기
        newName = input('newName :')
        names[index] = newName # 찾을 인덱스에 새로운 값 대입
    return

def nameDelete():
    global names  # 전역변수 호출
    deleteName = input('deleteName :') # 삭제할 이름
    if names.count(deleteName) == 0 : return
    else: # 삭제할 값이 존재하면
        names.remove(deleteName) # 리스트변수명.remove(삭제할 값)
    return

while True: # 무한루프 # {} 대신 : 과 들여쓰기를 사용 # true 소문자가 아닌 True 대문자로 작성
    ch =int(input('1.create 2.read 3.update 4.delete :'))
    # int() 문자열타입 -> 정수타입 변환 함수
    # input() : 입력함수 , 입력받은 데이터를 문자열 반환
    # ch : 'ch' 변수에 특정한 타입을 작성/명시 하지는 않는다.
    if ch == 1 : nameCreate() # 만약에 # 조건문
        # 주의할점 : 들여쓰기
    # 들여쓰기 1번 while 문에 포함
        # 들여쓰기 2번 while문 -> if 문에 포함
    elif ch == 2: nameRead()  # 함수 호출
    elif ch == 3: nameUpdate()
    elif ch == 4: nameDelete()