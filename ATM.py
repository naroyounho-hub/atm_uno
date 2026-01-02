# 260102 15:15
balance = 0
history = []
his = {"state": "", "amount": 0, "bal": 0}

while True:
    print(
        """
          =====ATM MENU=====
          1. 잔액조회
          2. 입금
          3. 출금
          4. 거래내역 조회
          0. 종료
          """
    )
    input1 = print(input("메뉴 번호를 선택해주세요"))
