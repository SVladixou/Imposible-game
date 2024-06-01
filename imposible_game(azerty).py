#We import random
import random

#We choose a random letter from the word "azerty"

text = "azerty"
a = random.choice(text)
b = random.choice(text)
c = random.choice(text)
d = random.choice(text)
e = random.choice(text)
f = random.choice(text)

#We check if it corresponds to "azerty" or not

if a == "a":
    print(a)
else:
    print("Nope ;)")
if b == "z":
    print(b)
else:
    print("Nope ;)")
if c == "e":
    print(c)
else:
    print("Nope ;)")
if d == "r":
    print(d)
else:
    print("Nope ;)")
if e == "t":
    print(e)
else:
    print("Nope ;)")
if f == "y":
    print(f)
else:
    print("Nope ;)")

#We check if the result obtained corresponds to the basic “azerty” result

list1 = ["a","z","e","r","t","y"]

list2 = [a,b,c,d,e,f]

if list1 == list2:
    print("WOW GGGGGGG")
else:
    print("Sorry try again ;)")
your_result = list2
result = list1

#We display the result

print("Your result : ",list2)
print("") #For a line break
print("Result : ",list1)