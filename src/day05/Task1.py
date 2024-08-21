
# 문자열 활용 , p.50 ~ p.76
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 하나의 이름을 입력받아 여러명의 이름을 저장
#          2. 저장된 여려명의 이름을 모두 출력
#          3. 수정할 이름과 새로운 이름을 입력받아 수정
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 추가적인 전역변수 생성하지 말기
# [조건4] : 최대한 리스트타입 사용하지 않기

# 하나의 변수에 여러가지 정보 # 1.json[몇 가지 필드를 key로 구분] 2.csv[몇 가지 필드를 쉼표로 구분], 주로 문자열 타입 사용

names = "유재석,강호동,신동엽"  # 여러개 name들을 저장하는 문자열 변수

def nameCreate() :
    name = input("이름을 입력해주세요. \n")
    return names + " " + name
def nameRead() :
    for name in names.split(','): # 문자열내 ,쉼표 기준으로 분해
        print(name)
    return
def nameUpdate() :
    name = input("수정할 이름을 입력해주세요. \n")
    if names.count(name) :
        newName = input("새로운 이름을 입력해주세요. \n")
        return names.replace(name,newName)
    return

def nameDelete() :
    return

while True: # 무한루프
    ch = input('1.create 2.read 3.update 4.delete :')
    if ch == "1":
        nameCreate()
        print(names)
    elif ch == "2":
        nameRead()

    elif ch == "3":
        nameUpdate()
    elif ch == "4":
        nameDelete()


