
# 튜플 활용 , p.89 ~ p.92
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 하나의 이름을 입력받아 여러명의 이름을 저장
#          2. 저장된 여려명의 이름을 모두 출력
#          3. 수정할 이름과 새로운 이름을 입력받아 수정
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 추가적인 전역변수 생성하지 말기
# [조건4] : 최대한 리스트타입 사용하지 않기

# 튜플이란? 리스트와 비슷 , 차이점 : 요소의 삽입/삭제가 불가능
    # 튜플은 불면성을 가진다. 리터럴과 같다.
    # a = 3 + 2         , 5
    # a = 'py' + '3'    , py3
    # a = (1 , 2) + (3) , (1,2,3)

# 전역변수
names = ('유재석','강호동','신동엽') # 샘플 데이터

# 함수정의 , def 함수명(매개변수 , 매개변수):
def nameCreate():
    global names
    newName = input('newName :')
    names += (newName , ) # 기존 튜플과 입력받은 값의 튜플 더하기 해서 새로운 튜플 반환
    return

def nameRead():
    for name in names:  # for 반복변수 in 튜플/리스트/문자열 :
        print(f'name :{name}')
    return

def nameUpdate():
    global names    # 전역변수 호출
    oldName = input('oldName :')
    if names.count(oldName) == 0 : return
    else:
        newName = input('newName :')
        newNames = ( )
        for name in names:
            if name == oldName:
                newNames += (newName ,) # 새로운 이름 대입
            else:
                newNames += (name ,) # 기존 이름 대입
        names = newNames
    return

def nameDelete():
    global names
    deleteName = input('deleteName :')
    if names.count(deleteName) == 0 : return
    else:
        newName = ()                    # 새로운 튜플
        for name in names:              # 튜플에서 하나씩 요소 반복
            if name == deleteName:      # 만약에 삭제할 요소값과 같으면
                continue                # 생략
            else:                       # 같지 않으면
                newName +=(name ,)      # 새로운 튜플에 기존요소를 누적
        names = newName              # 반복문이 종료되면 새로운 튜플을 전역변수에 대입
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