print("madan", type('madan'))

#  #assign a strig to a variable

a='madan'
print(a,type(a)) 


# # # # #multiple strings
# # # # you can assign multiple strings to a variable by using three quotes

a= '''this is "madan"
studied at 'jntua'
anantapur'''
print(a, type(a))



# #upper case
a='madan'
b=(a.upper() )
print(b)
print(b.lower())
print(b.capitalize())


#remove whitespace
a = " Hello, World!,,,,***       "
print(a.strip())
print(len(a))
b=(a.rstrip(",* "))
print(b,len(b))


#replace a string
m="Hello, World!"
print(m.replace("H", "l"))

a = "Hello, World!"
print(a.replace("H", "J"))


#split a string

c = "Hello, World!"
print(c.split(sep="e"))

n="hello"
b="world"
v=n+b
t=n+" "+b
print(v)
print(t)

# F-strings

age= int(input("enter your age: "))
name= input("enter your name: ")
txt = "your  name is {}, your {} old".format(name,age)
h=f"your name is {name},your {age} old "
print(txt)
print(h)

prise = 59
sales= f"the price is {prise:.3f} dollars"
print(sales)

d= 89
f="%.5f" %d
print(f)
print(f"{d:.5f}")

txt = f"The price is {20 * 59} dollars"
print(txt)



k="kondreddy gari madan mohan reddy"
for x in k:
   print (x)

import random
print(random.randrange(10,500))

