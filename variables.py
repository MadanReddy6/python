a = "madan"
print (a,type(a))

b = 656
print(b, type(b)) 

c = 40.3
print(c,type(c))

d = 3 + 7j
print(d,type(d))
# The complex data type in python consists of two values, 
# the first one is the real part of the complex number, 
# and the second one is the imaginary part of the complex number. 
# We usually denote the real part using i and the imaginary part with j. 
# For example, (3 + 7j) or (3i + 7j).

e = ['apple','banan','cherry']
[x,y,z] = e
print(x, type(e))
print(y, type(e))
print(z, type(e))
print(e, type(e))


f= ('apple','banan','cherry')
(x,y,z)=f
print(x, type(f))
print(y, type(f))
print(z, type(f))
print(f,type(f))

g= range(10)
print(g, type(g))
for x in g:
     print(x)
# Python range is a function that returns a sequence of numbers.
# By default, range returns a sequence that begins at 0 and increments in steps of 1.
# The range function only works with integers. Other data types like float numbers cannot be used.

h={'apple','banana','cherry'}
[x,y,z] = h
print(x, type(h))
print(y, type(h))
print(z, type(h))
print(h, type(h))

