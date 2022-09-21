#core of programming

# 1. what is the data?
# 2. Data Organization
#       How is this data organized? How can I organize the data?
# 3. Iterate or manupulate or interact with data

from random import seed
from random import random

value = 0
secret_num = 0
guess = 0
for numbs in range(1):
    value = random()
    secret_num = int(value * 100)
def game():
  print(secret_num)
  guess = int(input('Please enter a number between 1-100: '))
  if guess == secret_num:
    print('you got it')
  elif guess > secret_num:
    print('try again, guess lower')
    game()
  elif guess < secret_num:
    print('try again, guess higher')
    game()
game() # invoked the function


# What data is there? What data type do i have access to?
        # int
        # float
        # String
