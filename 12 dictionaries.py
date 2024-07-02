mydict = {
   "brand" : "ford",
    "model" : "mustang",
    "year" : 2020
}

thisdict = mydict

# thisdict = mydict.copy()

mydict["brand"] = "TATA"
# print(mydict)
# print(thisdict)


family = {
    "child1" :{
        "name": "madan",
        "year": 2002
    },
    "child2" :{
        "name": "jagan",
        "year": 1998
    },
    "child3" : {
        "name": "mohan",
        "year": 2004
    }
}

print(family)


for x , obj in family.items():
    print(x)

    for y in obj:
        print(y + ':' , obj[y])