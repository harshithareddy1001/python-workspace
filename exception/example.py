balance=5000
def withdraw(amount):
    global balance
    if amount<=0:
        raise ValueError("amount should be greater than zero")
    if amount>balance:
        raise RuntimeError("insufficient balance")
    balance-=amount
    return balance
try:
    print("welcome to ATM")
    user_input=int(input("enter amount to withdraw: "))
    amount=float(user_input)
    new_balance = withdraw(amount)
    print("withdrawal successful")
    print("remaining balance:", new_balance)

except ValueError as ve:
    print("error:", ve)
except RuntimeError as re:
    print("error:", re)
except Exception as e:
    print("unexpected error:", e)


