# import random

# #Building a list

# def create_list_of_uniquie_numbers():
#     my_list = []
#     while len(my_list) < 4:
#         x = random.randint(1, 9)
#         if x not in my_list:
#             my_list.append(x)
#     return(my_list)

# create_list_of_uniquie_numbers()
# empty1=[]
# empty2=[]

# def count_exact_mathces(a, b):
#     pairs =zip(a, b)
#     counter = 0
#     for c, d in pairs:
#         if a ==b:
#             counter =+ 1
#     return(counter)

# def count_common_entries(a_list, b_list):
#     pairs = 0
#     for number in a_list:
#         if number in b_list:
#             pairs = pairs + 1
#     return(pairs)

# def parse_numbers(a):
#     a = int(a)
#     converted_digits = []
#     for number in a:
#         number = int(number)
#         converted_digits.append(numbers)
#     return converted_digits
# parse_numbers("1234")
