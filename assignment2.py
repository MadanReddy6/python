# initialize an empty dictionary
# now just iterate on the list, and any new element we get, we create a new key in the dictionary.
# if we get an element already present in the dictionary increase the value
# in the end just print out the key with the highest value


x = [2, 4, 5, 2, 6, 7, 3, 6, 1, 3, 8,]

element_counts = {}

for element in x:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1

most_frequent_element = max(element_counts, key=element_counts.get)

print("Most frequent element:", most_frequent_element)
