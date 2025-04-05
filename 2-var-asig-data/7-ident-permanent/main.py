list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

is_compare1 = list1 is list2
# list1 and list 3 reference the same object
is_compare2 = list1 is list3

print(is_compare1)
print(is_compare2)

# ------

numbers = [1, 2, 3, 4, 5]

three = 3 in numbers
six = 6 in numbers

print(three)
print(six)

