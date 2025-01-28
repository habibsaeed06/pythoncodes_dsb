#4th
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 3, 7, 8]
common_elements = list(set(list1) & set(list2))
print(common_elements) 


#5TH
names = ['Sohan', 'Mohan', 'Rohan']
first_letters = [name[0] for name in names]
print(first_letters) 


#6th
my_list = ['pandas', 'numpy', 'flask', 'python', 'python']
first= set()
repeated = []
for item in my_list:
    if item in first:
        repeated.append(item)
    else:
        first.add(item)
print(repeated) 


#7th
my_string = "saeed"
length = len(my_string)
print("The length of the string is:",length)


#8th
my_list = [1, 2, 5, 3, 4, 8, 9, "lis", "a"]
length = len(my_list)

print("The length of the list is:",length)



