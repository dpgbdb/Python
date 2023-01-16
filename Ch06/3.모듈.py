"""
날짜 : 2023/01/11
이름 : 김동민
내용 : 파이썬 모듈 실습하기
"""

from Ch06.sub2.calc import plus,minus

import Ch06.sub2.calc as c

r1 = plus(1,2)
r2 = minus(2,3)
r3 = c.multi(3,4)
r4 = c.div(7,3)

print('r1 :',r1)
print('r2 :',r2)
print('r3 :',r3)
print('r4 :',r4)