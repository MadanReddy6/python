# def full_name(fname, lname):
#     print("full_name is" , fname , lname)

# full_name('mohan' , 'reddy')
# 


# x = (1,2,3,4,5,6)
# for i in x :
#     print(i+i)

def multiply(*num):

    c = 1
    for i in num:
        c = i*c
    print(c)

multiply(1,5,5,3)