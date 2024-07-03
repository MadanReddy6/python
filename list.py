thislist = ['apple','banan','cherry']
print(type(thislist))

#creating list by using list () construction

listmethod= list(('apple','banan','cherry'))
print(listmethod)
print(len(listmethod))


# accessing list items

thislist = ['apple','banan','cherry']
print(thislist[1])
item = (thislist[1])
print(item)
print(thislist[-1])


# check if item exists

if 'banan' in thislist:
    print('yes banana is present in thislist')


# change list item
car_brands=['maruthi','audi','tata','kia']

car_brands[1]= 'toyoto'
print(car_brands)

# change a range of items

car_brands[1:4]= ['benz','benz','benz','benz',]
print(car_brands)

fruits = ['apple','banana','cherry','mango']

fruits.append('pineapple')
print(fruits)
fruits.insert(2,'kiwi')
print(fruits)

# extending list

fruits = ['apple','banana','cherry','mango']
car_brands=['maruthi','audi','tata','kia']


fruits.extend(car_brands)
print(fruits)

# remove specific item

fruits = ['apple','banana','cherry','mango']

fruits.remove('apple')
print(fruits)


#remove specific index

fruits.pop(2)
print(fruits)


bikes = ['hero','yamaha','honda','tvs']
bikes.clear()
print(bikes)
# del bikes
# print(bikes)


# loop through lists 
mobiles= ['realme','oppo','vivo','apple']

for i in mobiles:
    print(i)

k=0
while k < len(mobiles):
    print(mobiles[k])
    k+=1


mobiles.reverse()
print(mobiles)


#CUSTOME SORT FUNCTION

def myfunc(n):
    return abs(n-50)

mylist = [100,50,65,82,23,2]
mylist.sort(key=myfunc)
print(mylist)

#case insensitive sort

alphabets = ['a','K','c','d','A']

alphabets.sort(key=str.lower)
print(alphabets)
alphabets.reverse()
print(alphabets)

#coyp list

abcdlu = alphabets
ABCDLU = alphabets.copy()
ABCdlu = list(alphabets)
print(abcdlu)
print(ABCDLU)
print(ABCdlu)


#join lists


list1 =[100,50,65,82,23,2]
list2 =['a','K','c','d','A']
list3 = list1 + list2
print(list3)

#joining lists by using loops

for x in list2:
    list1.append(x)
print(list1)

#extend method 

list1.extend(list2)
print(list1)