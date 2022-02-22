
'''
* 식별자 (identifier)

1. 식별자: 사용자 정의로 데이터에 이름을 붙인 것
2. 모듈, 패키지, 변수, 함수, 클래스 등의 이름을 식별자라고 함
3. 식별자 이름은 중복해서 지정할 수 없다
'''

# 식별자 이름을 숫자로 지정하거나 숫자로 시작 불가
# 7 = 777 (X)
# 7number = 7 (X)
number7 = 7
num7ber = 7

# 식별자 이름에 공백 포함 불가 
# my birth day = 19950216 (X)
my_birth_day = 19950216

#키워드를 식별자로 지정 불가
# if = '만약에' (X)
If = '만약에' # 권장하지 않음

# print()와 같은 내장함수의 이름을 식별자로 사용할 수 있음
# 더 이상 함수의 기능을 사용할 수 없음
# print = '출력하다'
# print(print)

# 한글, 한자 등 영어 이외의 문자도 가능하긴 하지만
# 사용을 권장하지는 않음
야옹이 = '고양이' #권장하지 않음
print(야옹이)