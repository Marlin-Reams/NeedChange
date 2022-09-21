# Python list

# a sequence of elements

# order matters!!!!!!!!!

basket = ['oragne', 'apple', 'books',]
              #0        #1        #2
# print(basket[1])


# when you see lists in your life
#Your first instinct should be to iterate (loop)
#When i see a list my first instinct is to loop over it

# 1: Data
# 2: Data organization
# 3: Iteration

# next example shows list slicing

# for item in basket[:3 :2]:
#     print(item)
#     # print('upper cassed', item.upper())


# list slicing - creates a new copy of the list

# list[0:2]

# reverse a list

# print(basket[::-1])

#research these methods
# .sort() The sort() method sorts the list ascending by default.
#           You can also make a function to decide the sorting criteria(s).
# .insert()
# and the diffrence between inster and extend
# .extend()
# .remove()
#  and the difference between remove and pop
# .pop()
# .clear()


#1.
# list1 = [100, 200, 300, 400, 500]
# [500, 400, 300, 200, 100]

# print(list1[::-1])

#2.
# numbers = [1, 2, 3, 4, 5, 6, 7]
# [1, 4, 9, 16, 25, 36, 49]

# squared_number = [number ** 2 for number in numbers]
# print(squared_number)

#3.
# list1 = ["Mike", "", "Emma", "Aisha", "", "Dalante"]
# while '' in list1:
#     list1.remove('')
# print(list1)

# list1 = ["Mike", "", "Emma", "Aisha", "", "Dalante"]
# for i in list1:
#     if i == "":
#         list1.remove('')
# print(list1)


#4.
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print(list1[2][2].append(7000))
print(list1)
