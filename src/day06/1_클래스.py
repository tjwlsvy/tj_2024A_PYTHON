
'''
    객체란? 논리적/물리적 정의한 실체물
    클래스란? 객체를 물리적으로 표현하기 위한 설계도
    인스턴스란? 클래스를 이용해서 객체를 물리적[메모리]으로 만든 실체물

    - java 클래스
    class Calculator{
        int result; // 필드
        Calculator(){}  // 생성자
        int add(int num){   // 메소드
            this.result += num
            return this.result
        }
    }
    - java 객체
    Calculator cal1 = new Calculator();
    Calculator cal2 = new Calculator();
    - 객체가 메소드 호출
    cal1.add(3)
'''
# [1] 파이썬 클래스 만들기 . class 클래스명 :
class Calculator:
    def __init__(self): # 생성자
        self.result = 0
    def add(self, num): # 메소드
        self.result += num
        return self.result
# [2] 파이썬 객체 만들기 , 변수명 = 클래스명()
cal1 = Calculator(); print(cal1)
cal2 = Calculator(); print(cal2)
# [3] 파이썬 객체내 메소드 호출
print(cal1.add(3))  # 3
print(cal1.add(4))  # 3 + 4 = 7
print(cal2.add(3))  # 3
print(cal2.add(7))  # 3 + 7 = 10

# [4] 클래스의 생성자 정의
# (1) 과자 클래스 정의
class 과자틀 :
    # 파이썬은 기본적으로 다중생성자를 지원하지 않는다 # 단일 생성자 #__init__
    # def __init__(self):
    #     self.과자재료1 = None
    #     self.과자재료2 = None
    # 생정자1 : 매개변수 2개 갖는 생성자
    def __init__(self , 재료1 , 재료2 ): # __init__ 생성자 역할을 하는 메소드
        # self : 해당 메소드를 실행하는 객체 생성
        self.과자재료1 = 재료1    # self.필드명 = 매개변수 # 매개변수로 필드 값 초기화 하기
        self.과자재료2 = 재료2    # self.필드명 = 매개변수 # 매개변수로 필드 값 초기화 하기

# (2) 과자 객체 생성
var1 = 과자틀('밀가루' , '초코'); print(var1)   # <__main__.과자틀 object at 0x000001CDECFDE150>
var2 = 과자틀('밀가루' , '치즈'); print(var2)   # <__main__.과자틀 object at 0x000001CDECFDE150>

#(3) 객체의 필드 호출 , 객체변수명.필드명
print(var1.과자재료1) # 밀가루 # 첫번째 객체/과자의 과자재료1 필드 값 출력
print(var1.과자재료2) # 초코 # 첫번째 객체/과자의 과자재료2 필드 값 출력
print(var2.과자재료1) # 밀가루 # 첫번째 객체/과자의 과자재려1 필드 값 출력
print(var2.과자재료2) # 치즈 # 첫번째 객체/과자의 과자재려1 필드 값 출력

# (4) 객체의 필드 값 수정 , 객체변수명.필드명 = 새로운값
# var3 = 과자틀(); print(var3)
var2.과자재료2 = '녹차'
print(var2.과자재료2) # 녹차



