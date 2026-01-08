input1 = ""
balance = 0
acount = []

while True:

    print(
        """
           1. 잔액조회
           2. 입금
           3. 출금
           4. 거래내역 조회
           0. 종료"""
    )
    input1 = input("번호를 입력하세요")
    print(input1)

    if input1 == "1":
        print(f"{balance}입니다")

    elif input1 == "2":
        input2 = int(input("입금액 : "))
        print(input2)
        if input2 < 0:
            print("잘못입력하셨습니다")
            balance = balance + input2
            in_cash = {"state": "입금", "amount": input2, "bal": balance}
            acount.append(in_cash)

    elif input1 == "3":
        input3 = int(input("출금액 : "))
        print(input3)
        if input3 < 0:
            print("잘못입력하셨습니다.")
            balance = balance - input3
        elif input3 > balance:
            print("잔액이 부족합니다.")
            out_cash = {"state": "출금", "amount": input2, "bal": balance}
            acount.append(out_cash)

    elif input1 == "4":
        for i in acount:
            print(f"{i["state"]}{i["amount"]}{i["bal"]} ")

    elif input1 == "0":
        break
