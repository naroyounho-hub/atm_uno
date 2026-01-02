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
    input1 = input("메뉴 번호를 선택해주세요")
    print(input1)
    if input1 == "0":
        print("이용해주셔서 감사합니다.유노은행")
        break
    elif input1 == "1":
        print(f" 현재 잔액은 {balance} 입니다.")
    elif input1 == "2":
        input2 = int(
            input(
                """
        입금 하실 금액을 입력하세요.
        입금액 :  """
            )
        )
        balance = balance + input2
        print(f" 현재 잔액은 {balance} 입니다.")
        his = {"state": "입금", "amount": input2, "bal": balance}
        history.append(his)
    elif input1 == "3":
        input3 = int(
            input(
                """
        출금 하실 금액을 입력하세요.
        출금액 : """
            )
        )
        balance = balance - input3
        print(f" 현재 잔액은 {balance} 입니다.")
        his = {"state": "출금", "amount": input3, "bal": balance}
        history.append(his)
    elif input1 == "4":
        for h in history:
            print(f"[{h['state']}],  {h['amount']}, {h['bal']}")
    else:
        print("잘못입력하셨습니다")
