# We impost module (random)
import random

text = "qwerty"
#We choice a random letter
a = random.choice(text)
b = random.choice(text)
c = random.choice(text)
d = random.choice(text)
e = random.choice(text)
f = random.choice(text)
#We check if it corresponds to "qwerty" or not
if a == "q":
    print(a)
else:
    print("Nope ;")
if b == "w":
    print(b)
else:
    print("Nope ;")
if c == "e":
    print(c)
else:
    print("Nope ;")
if d == "r":
    print(d)
else:
    print("Nope ;")
if e == "t":
    print(e)
else:
    print("Nope ;")
if f == "y":
    print(f)
else:
    print("Nope ;")

#We check if the result obtained corresponds to the basic "qwerty" result

user_result = [a,b,c,d,e,f]
original_result = ["q","w","e","r","t","y"]


if user_result == original_result:
    print("WOW GGG")
else:
    print("Sorry try again ;)")

print("Your result : ", user_result)
print("")
print("Original result : ", original_result)