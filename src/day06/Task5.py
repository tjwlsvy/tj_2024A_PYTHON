
# 딕셔너리/리스트 활용 , 파일처리 p.175 ~ p.182
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 한명의 name , age 입력받아 저장
#          2. 저장된 여려명의 name , age 모두 출력
#          3. 수정할 이름 입력받아 존재하면 name, age 을 입력받고 수정  합니다.
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 추가적인 전역변수 생성 불가
# [조건4] : 프로그램 종료되고 다시 실행되더라도 기존의 names 데이터가 유지되도록 파일처리 하시오.
            # - dataLoad , datasave 함수를 정의하여 적절한 위치에서 호출하시오.

# 파일내 데이터 설계 : 다수의 이름과 나이의 데이터들의 저장하는 방법을 설계
    # CSV : 필드구분 ,(쉼표) , 객체구분 \n
    # 유재석20강호동30 -> CSV 변경 -> 유재석,20 \n 강호동,30

# 리스트 [] 안에 여러개 딕셔너리{ } 저장된 설꼐

# 전역변수
names = [] # 샘플 데이터

# 함수정의
def dataLoad(): # 파일내 데이터 불러오기 # wile True 위에서 실행
    global names
    f = open('names.txt','r' , encoding="utf-8")   # 파일 읽기모드로 객체 반환
    var = f.read()              # 파일내 데이터 전체 읽어오기 # 파일객체.read()
    print(var)                  #확인
    # 문자열 -> 딕셔너리 만들고 리스트에 담기.
    print(var.split('\n'))
    lines = var.split('\n')  # 줄마다(요소)
    for line in lines[ :len(lines)-1 ]: # 일겅온 파일 내용을 \n 분해 # \n으로 객체 구분 # 마지막줄 제외
        print(line)
        dic = {'name' : line.split(',')[0],'age' : line.split(',')[1]} # 해당줄에 ,(쉼표)분해, [0] 이름 [1] 나이
        names.append(dic)   # 해당 딕셔너리를 리스트에 저장
    f.close()
    print(names)
    return

def dataSave(): # 데이터를 파일내 저장하기 # 사용처 nameCreate , nameUpdate , nameDelete 함수 안에서 처리후 실행
    global names
    # 1. 파일에 데이터 쓰기
    f = open('names.txt', "w")  # 파일 쓰기모드로 객체 반환
    # 딕셔너리 -> 문자열 만들고 파일쓰기
    outstr = "" # 파일에 작성할 문자열 변수
    for dic in names:
        outstr += f'{dic['name']},{dic['age']}\n'   # 딕셔너리를 CSV 형식의 문자열로 반환 # ,(쉼표) 필드 구분 # \n(줄바꿈) 객체/딕셔너리 구분
    f.write(outstr)             # 파일객체 이용한 데이터 쓰기 # write(데이터)
    f.close()                   # 파일객체 닫기 , 파일객체.close()
    return

def nameCreate():
    global names
    newName = input('newName :')
    newAge = int(input('newAge :'))
    dic = {'name' : newName , 'age' : newAge} # 딕셔너리 구성
    names.append(dic) # 딕셔너리를 리스트에 삽입
    dataSave()
    return

def nameRead():
    for dic in names:  # 리스트내 딕셔너리 하나씩 호출
        print(f'name :{dic['name']}, age:{dic['age']}')   # 딕셔너리변수명[key] 또는 딕셔너리변수명.get(key)
    return

def nameUpdate():
    global names    # 전역변수 호출
    oldName = input('oldName :')
    for dic in names:
        if dic['name'] == oldName:
            newName = input('newName :')
            dic['name'] = newName   # 해당 딕셔너리의 속성 값 수정하기
            newAge = input('newAge :')
            dic['age'] = newAge
            dataSave()
            break
    return

def nameDelete():
    global names
    deleteName = input('deleteName :')
    for dic in names :
        if dic['name'] == deleteName:  # 만약에 삭제할 이름과 같으면
            names.remove(dic)   # 리스트변수명.remove(삭제할 딕셔너리)
            dataSave()
            return # 1개만 삭제하기 위해서는 삭제후 return
    return

dataLoad() # 프로그램 실행될때 파일내용 읽어오기
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