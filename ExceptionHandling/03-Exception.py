def atm():
    totalBal = 5000
    pin = input("Enter your PIN : ")
    if pin == "1234":
        print("Login Success")
    else:
        # print("Login Failed")
        raise ValueError("Login Failed")

    amount = int(input("Enter the amount : "))
    if amount < totalBal:
        totalBal -= amount
        print("Remaining Balance is",totalBal)
    else:
        raise ValueError("Insufficient Balance")

try:
    atm()
except ValueError as err:
    print(err)
    atm()