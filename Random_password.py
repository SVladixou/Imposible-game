import random

caracter = "abcdefghijklmnopqrstuvwxyz"
caracter_maj = "ABCDEFGHIJKLMNOPKRSTUVWXYZ"
num = "123456789"
symbol = ",?;.:/!%$^+=})]@^_`-|(['{#}&"

all_ = caracter + caracter_maj + num + symbol
wheight = int(input("What is your wheight for your password ? : "))

print(wheight)
password = []
a = [random.choice(all_) for i in range(wheight)]
password+=a
print("Your password is :",password)