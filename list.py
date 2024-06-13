# NOTE: lists items are ordered, changeble, allow duplicate values

x=["apple","banana","cherry"]
print(x,type(x))

print(len(x))

# list items - data types : list items can be any data type

a= ["apple","banana","cherry"]
b= [1,2,3,4,5]
c= ['True','False','True']

print(a,type(a))
print(b,type(b))
print(c,type(c))

# the list() construction

d=list(('a','b','c'))
print(d,type(d))

# access items

z=["apple","banana","cherry",'pienapple','mango',"graphs"]
print(z[1])

print(z[-2])

print(z[2:4])

print(z[ :3])


print(z[2: ])

print(z[-4:])

# check if item exists

fruits= ["apple","banana","cherry"]
if 'apple' in fruits:
    print("yes, apple in the fruits")


# changing list item

k=["apple","banana","cherry",'pineapple','mango',"graphs"]

k[3]= 'jackfruit'
print(k)

k[1:3]=["papaya","fragonfruit"]
print(k)

k[4:6]=['draginfruit']
print(k)

k.insert(3,'kiwi')
print(k)

k.append('kiwi')
print(k)

fruits.extend(k)
print(fruits)

thistuple=(1,2)
k.append(thistuple)
print(k)

m=["apple","banana","cherry",'pineapple','mango',"graphs"]

m.remove("graphs")
print(m)
# if there are morethan one itsm with the same value, the remove ()method removes the first occurance

# remove specific index (pop)
t=["apple","banana","cherry",'pineapple','mango',"graphs"]

t.pop(3)
print(t)

t.pop()
print(t)


# NOTE : this "del" keyword deletes entire lils, so it will through error as out put
u=["apple","banana","cherry",'pineapple','mango',"graphs"]
del u

#clear list 

o=["apple","banana","cherry",'pineapple','mango',"graphs"]
o.clear()
print(o)
