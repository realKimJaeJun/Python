"""
날짜 : 2023/01/11
이름 : 김재준
내용 : 파이썬 모듈 실습하기
"""

from sub2.calc import plus, minus
import sub2.calc as c

r1 = plus(1, 2)
r2 = minus(2, 1)

r3 = c.multi(2, 3)
r4 = c.div(4, 2)

print('r1 : ', r1)
print('r2 : ', r2)
print('r3 : ', r3)
print('r4 : ', r4)