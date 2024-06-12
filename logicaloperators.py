name = input("enter your name: ")
hight= float(input("hight(m):" ))
weight= float(input("weight(kg):"))

bmi = (weight / (hight**hight))
print(bmi)

# bmi = float(input(("enter your weight:")))

if bmi <= 18.5:
    print( "under weight")
elif bmi >= 18.6 and bmi <= 24.9:
    print("normal weight")
elif bmi >= 25 and bmi <= 29.9:
    print("over weight")
elif bmi > 30:
    print("obisuty")

print("ok , {} your {} with a bim of {}".format(name,print,bmi) )


# print("{} your bmi is {}".format(name,bmi))


