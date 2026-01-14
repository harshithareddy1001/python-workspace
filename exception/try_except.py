
try:
    num=int(input("enter the number"))
    print("........")
    print(10/num)
    print("phase1 completed")
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("invalid input")
finally:
    print("execution completed")
