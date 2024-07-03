a = 33
b= 300
if b > a:
    print("b is greaterthan a ")

if a < b:
    print("a is lessthan b ")

c = 33
d = 33

if c > d:
    print("c is greaterthan d")
elif c < d:
    print("c is not lessthan d")

else :
    print("c and d both are equal")

# short hane if statements
print( "c is less than d") if c > d else   print("c not less than d")



a = 15
 
if a > 10:
    print("a is greater than ten")
    if a > 20:
        print("greater than 20")
    else:
        print("not greater than 20")