
# 객체/리스트 활용 190p. ~ 207p
# [조건1] : 각 함수 들을 구현 해서 프로그램 완성하기
# [조건2] :  1. 한명의 name , age 를 입력받아 저장 합니다.
#           2. 저장된 객체들을 name , age 을 모두 출력 합니다.
#           3. 수정할 이름을 입력받아 존재하면 새로운 name , age 을 입력받고 수정 합니다.
#           4. 삭제할 이름을 입력받아 존재하면 삭제 합니다.
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능합니다.
# 제출 : git에 commit 후 카톡방에 해당 과제가 있는 링크 제출

class person :
    def __init__(self, name , age): # 생성자
        self.name = name
        self.age = age
# 전역변수
names = [person('유재석',50),
         person('강호동',40),
          person('신동엽',30)
         ] # 샘플 데이터
def nameCreate():
    global names
    newName = input('newName :')
    newAge = int(input('newAge :'))
    names.append(person(newName , newAge))
    return

def nameRead():
    global names
    for person in names:
        print(f'name:{person.name},age:{person.age}')
    return

def nameUpdate():
    global names    # 전역변수 호출
    oldNamae = input('oldNamae : ')
    for person in names:
        if person.name == oldNamae:
            newName = input('newName : ')
            newAge = int(input('newAge :'))
            person.name = newName
            person.age = newAge
            return names
    return

def nameDelete():
    global names
    deleteName = input('deleteName :')
    for person in names:
        if deleteName == person.name:
            names.remove(person)
            return names
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