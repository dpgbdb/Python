"""
날짜 : 2023/01/11
이름 : 김동민
내용 : 파이썬 클래스 실습하기
"""
from Ch06.sub1.Car import Car
from Ch06.sub1.Account import Account

sonata = Car('소나타','흰색',3000)
sonata.speedUp()
sonata.speedDown()
sonata.show()

kb = Account('kb국민은행','1234-1234-1234','김동민',100000)
kb.deposit(20000)
kb.withdraw(20000)
kb.show()



