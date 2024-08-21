
# 딕셔너리/리스트 활용 , p.93 ~ p.101
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 하나의 이름을 입력받아 여러명의 이름을 저장
#          2. 저장된 여려명의 이름을 모두 출력
#          3. 수정할 이름과 새로운 이름을 입력받아 수정
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 추가적인 전역변수 생성하지 말기
# [조건4] : 최대한 리스트타입 사용하지 않기

# 딕셔너리 란? {} 안에 key : value 쌍으로 저장하는 자료 ,json 비슷하다
# 리스트 [] 안에 여러개 딕셔너리{ } 저장된 설꼐

# 전역변수
names = [{'name' : '유재석'} , {'name' : '강호동'} , {'name' : '신동엽'}] # 샘플 데이터

# 함수정의 , def 함수명(매개변수 , 매개변수):
def nameCreate():
    global names
    newName = input('newName :')
    dic = {'name' : newName} # 딕셔너리 구성
    names.append(dic) # 딕셔너리를 리스트에 삽입
    return

def nameRead():
    for dic in names:  # 리스트내 딕셔너리 하나씩 호출
        print(f'name :{dic['name']}')   # 딕셔너리변수명[key] 또는 딕셔너리변수명.get(key)
    return

def nameUpdate():
    global names    # 전역변수 호출
    oldName = input('oldName :')
    for dic in names:
        if dic['name'] == oldName:
            newName = input('newName :')
            dic['name'] = newName   # 해당 딕셔너리의 속성 값 수정하기
            return
    return

def nameDelete():
    global names
    deleteName = input('deleteName :')
    for dic in names :
        if dic['name'] == deleteName:  # 만약에 삭제할 이름과 같으면
            names.remove(dic)   # 리스트변수명.remove(삭제할 딕셔너리)
            return # 1개만 삭제하기 위해서는 삭제후 return
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