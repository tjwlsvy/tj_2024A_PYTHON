

# (1) 사용자 입력 , input() 함수
    # input( '안내문구' )
    # 콘솔에 입력받은 값을 문자열(str)로 반환 해주는 함수
    # 타입 확인 함수 : type(자료)

a = input() # js prompt() java scanner
print(a)

number = a = input('숫자를 입력 하세요')
print(number)
print(type(number))

# (2) print 자세히 보기 , print() 함수
    # print( 리터럴 또는 변수명 또는 연산식 )
    # print( f'문자열{ 리터럴 또는 변수명 또는 연산식 }문자열' : f 퍼메팅
    # print( 리터럴 또는 변수명 또는 연산식 , end=" 출력후 대입 할 문자열") : \n 기본값
print( 123 )        # 숫자 출력
print( "Python")    # 문자열 출력
print( [1,2,3])    # 리스트 출력
# + 연산자를 이용한 문자열 연결
print("Python"+" is fun")
# ,를 이용한 문자열 연결
print("Python","is fun")
# 출력후 결과값 변경하기 , 줄바꿈 대신 다른 문자열 넣을수 있다.
print('python' , end=" ")  # end="\n" 기본값 이지만 변경이 가능하다
print("is fun")








