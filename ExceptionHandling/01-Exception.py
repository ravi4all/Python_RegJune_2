try:
    f_num = int(input("Enter first number : "))
    s_num = int(input("Enter second number : "))

    a = f_num + s_num
    print("Sum is",a)

    b = f_num - s_num
    print("Diff is",b)

    c = f_num / s_num
    print("Div is",c)

    d = f_num * s_num
    print("Mul is",d)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid Input, Please provide a digit 0-9")
except BaseException as err:
    print(err)
# except (ZeroDivisionError, ValueError) as err:
#     print(err)