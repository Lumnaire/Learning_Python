list1 = [5, 4, 2, 3, 1]
list2 = ['Banana', 'Pineapple', 'Apples', 'Peach', 'Jackfruit', 'Jackfruit']
list1.sort() # used to print in ascending order
list1.extend(list2) # combines two list
list2.append('Cherry') # adds item in the list
list2.insert(1, 'Mango') # inserts a specified item in the list, the first value is the index count and the second value is the item you will insert
list2.remove('Banana') # removes an item in the list
# list2.clear() used to clear the list but it is available in our code to print []

print(list2)
print(list2.index('Pineapple')) # used to define index inside list
print(list2.count('Jackfruit')) # defines if there are duplications to count inside list

print(list1)

data = [1, 2, 3, 4, 5]
data.reverse() # used to print in descending order (last value to the first)
data2 = data.copy() # copies the value 
data.pop() # removes the last value
data.pop(1) # removes a specific index in the list
del data[0] # the same as removing index in the list
# del data # used to delete the variable // there will be no data left
print(data)