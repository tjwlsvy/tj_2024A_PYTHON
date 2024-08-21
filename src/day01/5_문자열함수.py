# 5_문자열함수.py
# 문자열 관련 함수/기능 들

# (0) 문자열을 저장하고 있는 변수
a = '코딩도 헤매는 만큼 자기 땅이야'

# (1) "문자열".count('찾을문자') : 문자열내 찾을 문자가 존재하면 개수 반환 함수
print( a.count('자') )   # 1 , 문자열내 '자' 인 문자 개수
print( a.count('가') )   # 0 , 만일 존재하지 않으면 0

# (2) "문자열".find('찾을문자')    : 문자열내 찾을 문자가 존재하면 인덱스 반환 함수
print( a.find('자') )    # 11 , 문자열내 '자'인 인덱스 위치
print( a.find('가') )    # -1 , 만일 존재하지 않으면 -1

# (3) "문자열".index('찾을문자')   : 문자열내 찾을 문자가 존재하면 인덱스 반환 함수
print( a.index('자') )   # 11 , 문자열내 '자' 인 인덱스 위치
# print( a.index('가') )   # ValueError: substring not found , 만일 존재하지 않으면 예외발생

# (4) "특정문자".join( "문자열" 또는 리스트)      : 문자열내 문자 사이의 특정문자를 삽입 해서 반환 함수
print( ','.join( a ) )  # 코,딩,도, ,헤,매,는, ,만,큼, ,자,기, ,땅,이,야
b = [ "자바" , "파이썬" , "C언어" , "자바스크립트"]
print( '<->'.join( b ) ) # 자바<->파이썬<->C언어<->자바스크립트 , 리스트 요소 마다의 특정문자를 삽입 해서 반환 함수

c = 'AbCd'
# (5) .upper() : 문자열내 소문자를 대문자로 치환해서 반환 함수
print( c.upper() )
# (6) .lower() : 문자열내 대문자를 소문자로 치환해서 반환 함수
print( c.lower() )

d = '    python    '    # 앞뒤로 공백이 4개씩 존재하는 문자열
# (7) .lstrip() : 문자열내 왼쪽 여백 제거 해서 반환
print( d.lstrip() )
# (8) .rstrip() : 문자열내 오른쪽 여백 제거 해서 반환
print( d.rstrip() )
# (9) .strip()  : 문자열내 양쪽 여백 제거 해서 반환
print( d.strip() )

# (10) .replace( '기존문자' , '새로운문자' ) :
# 문자열내 기존문자가 존재하면 새로운문자로 치환해서 반환 함수
print( a.replace( '코딩' , '파이썬') ) # 파이썬도 헤매는 만큼 자기 땅이야

# (11) .split( )
# 문자열내 특정문자가 나누기 해서 리스트 반환 함수
print( a.split(' ') )       # ['코딩도', '헤매는', '만큼', '자기', '땅이야']
print( a.split(' ')[1] )    # '헤매는'
print( a.split(' ')[3] )    # '자기'

# 컴퓨터(파이썬,자바,자바스크립트,c언어)에서 문자는 불변 이다.!!!!!
    # 문자열/정수/실수(리터럴) 은 수정이 불가능하다. [불변!!!]
e = 'Python Program'
e.upper()
print( e )
e.replace( 'Program' , '프로그램')
print( e )
f = e.replace( 'Program' , '프로그램')
print( f )
# 새로운 문자열을 변수명 대입했다[O] , 변수가 참조하는 문자열이 변경되었다.[O]
e = 'Python 프로그램' # 기존의문자열을 수정했다[x]








