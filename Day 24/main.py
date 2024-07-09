# Read a file.
# with open("my_file.txt") as file:
#     contents=file.read()
#     print(contents)

# Mode r--> read  w--> write a--> append
# Write in a file.
with open("my_file.txt",mode='a') as file:
    file.write("\nnew tex t")