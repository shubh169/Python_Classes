"""
Take a look into file1 and file2. they each contain a bunch of numbers,
each number of new line.
You are going to write a program which contains the numbers that are common on both files.
"""

with open("file1.txt") as file1:
    list1=file1.readlines()

with open("file2.txt") as file2:
    list2=file2.readlines()


output=[int(num) for num in list1 if num in list2]
print(output)