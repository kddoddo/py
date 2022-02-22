
'''
* 문자열 포맷팅

- 포맷팅은 문자열 사이사이에 다른 타입의 데이터를 넣어서 문자열을 조립하는 방식
'''
apple = 3
print('사과가',apple,'개 있습니다')
print('사과가 %d개 있습니다' % apple)

'''
여러개의 데이터를 하나의 문자열에 포맷팅 할 수 있는데, 
이 때 % 연산자 뒤에 나열할 변수를 ()로 묶어줌
'''
month = 12
day = 25
anni = '크리스마스'
print(month,'월',day,'일은',anni,'입니다')
print('%d월 %d일은 %s입니다' % (month, day, anni))

'''
* format함수를 사용한 형식 지정 출력

- 문자열의 farmat함수를 사용하면 서식 문자를 지정하는 것보다 
  좀 더 유용하고 편하게 문자열 포맷을 사용 가능
'''
point = 90
print('수학 점수: {}점'.format(point))
print('{}월 {}일은 {}입니다'.format(month,day,anni))

print('{1}월 {2}일은 {0}입니다'.format(month,day,anni))

# 소수점 표현
pi = 3.141592
print('원주율은 %.2f입니다' % pi)
print('원주율은 {:.2f}입니다'.format(pi))

# f 문자열 포맷팅
# 파이썬 3.6버전 이후로 사용할 수 있는 기능
# 접두어 f를 문자열 앞에 붙여서 사용
print(f'{month}월 {day}일은 {anni}입니다')

# {}안에서는 수식도 사용할 수 있음
print(f'점수는 {point + 10}점 입니다')

print(f'원주율은 {pi:0.4f}입니다')