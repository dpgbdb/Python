"""
날짜 : 2023/01/12
이름 : 김동민
내용 : 파이썬 외부 패키지 모듈 실습
"""
from openpyxl import Workbook

# 새로운 엑셀파일 새엇ㅇ
Workbook = Workbook()

# 첫번째 시트 활성화
sheet = Workbook.active

# 데이터 입력
sheet['A1']= '파이썬 엑셀 실습'
sheet.append(['a101','김유신','010-1234-0123',25,'김해시'])
sheet.append(['a102','김춘추','010-1234-0124',26,'부산시'])
sheet.append(['a103','장보고','010-1234-0125',27,'창원시'])
sheet.append(['a104','강감찬','010-1234-0126',28,'마산시'])
sheet.append(['a105','이순신','010-1234-0127',29,'울산시'])
# 저장 닫기
Workbook.save('C:/Users/java2/Desktop/Member.xlsx')
Workbook.close()

print('프로그램 종료...')