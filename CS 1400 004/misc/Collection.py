'''
By: Ryan Schultz
Date: ##/##/####
add docstrings to functions the teacher is a slave to that idea
#####################################################################################################
'''
#####################################################################################################  do imports at the top, old cuck programmers are scared of imports not at the top
import turtle
import random
import sys #Unknown or fake
import math # possibly fake
import csv #fake

##################################################################################################### lists ###  have special code dedicated to it
'''
lists = ["entry1", "entry2"]
numbers = [1, 2, 4, 3]
lists.sort()
min(numbers)
max(numbers)
sum(numbers)
lists.pop()
#print(len.numbers())        #not working
#lists.remove()  #broken kinda
'''
##################################################################################################### 2D list
'''
twoD_list = [
            ["entry1.a", "entry2.a"],
            ["entry1.b", "entry2.b"],
            ]
print(twoD_list[0][1])
'''
#####################################################################################################  list special code
'''
lists[1] # calls the second item in the list (programers don't know how to count so 1 is 2, 0 is 1)
lists.append("entry3") # add a new item to the list at the end
numbers.sort()  # sorts the list by alphebet or numbers
'''
#####################################################################################################  misc. codes
'''
# loop commands: break, pass, exit
print("text")
for i in range(3):   # loops 3 times
    pass
chr(65)         # output A
ord("A")        # output 65
a = 'a'
try:
    int(a)                   #type change to int
    float(a)                #type change to float
except ValueError:
    print(a)
print("HelloWorld" * 3)     #print HelloWorldHelloWorldHelloWorld

i = 0                       #while loop
while i < 10:
    print(1)
    i += 1

for i in range(10):
    print(2)
    break #ends the loops

print(random.randint(1, 101))
'''
#####################################################################################################  trash/fake code
'''
output_file = open("student_folder/text/practice1.txt", "w")  #outputing to a file   Broken kinda
output_file.writelines("Hello there")
output_file.close()
with open("student_folder/text/read_practice.txt", "r") as read_file:
    print(read_file.readline())  # readline prints one whole line  readlines prints all the lines 

    while line != "":  #stupid way to make printline to printlines
         print(line)
read_file.seek(30)
'''
'''
def main():
    '''''' main function docstring'''''' #the teacher likes docstrings
    pass
if __name__ == "__main__":
    main()
'''
#####################################################################################################  Tuples
values = (False, True, False, False, False)
print("Are all values true values?:", all(values)) # all = if all are true, any = if any are true

tyson_items_to_purchase = ('clown', 'puppets', 'fans')
ryan_items_to_purchase = ('pinata', 'birthday cake', 'streamers', 'pizza', 'frisbee')
if (any(("birthday cake" or "cake" or "bday cake") in element for element in tyson_items_to_purchase)):
  print("\nTyson has to buy the cake.")
if (any(("cake" or "birthday cake" or "bday cake") in element for element in ryan_items_to_purchase)):
  print("\nRyan has to buy the cake.")
else:
  print("\nNo one is supposed to buy the cake.")

numbers = (9, 5, 3, 11, 14, 9, 7, 2)
numbers_sorted = sorted(numbers)

jobs = ('doctor', 'dentist', 'musician', 'veterinarian', 'computer scientist', 'lawyer', 'electrician')
jobs_sorted = sorted(jobs, key = len, reverse = True) # keys: len = length
print(jobs_sorted)

candy_prices = (1.06, 1.32, 1.99, 1.99, 2.00, 1.02, 1.50, 2.99) # zip and unzip
candy_names = ('Grand Bar', 'Cherry Wurly', 'Almond Milk Crackle', 'Mr. Caramel', 'Dark Ripple', 'Espresso Bark', 'Waffle Day', 'Peanut Butter Sticks')

candy_names_prices = tuple(zip(candy_names, candy_prices))
print("Tuples 'candy_names' and 'candy_prices' zipped together:", candy_names_prices)

candy_names_unzip, candy_prices_unzip = zip(*candy_names_prices)

print("Candy prices after unzipping Tuple 'candy_names_prices':", candy_prices_unzip)
print("Candy names after unzipping Tuple 'candy_names_prices':", candy_names_unzip)



