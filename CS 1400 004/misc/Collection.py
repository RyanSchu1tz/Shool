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
lists[0] # calls the second item in the list (programers don't know how to count so 1 is 2, 0 is 1)
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
#####################################################################################################







