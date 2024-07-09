
sentence=input("Enter your sentence:")
output={word:len(word) for word in sentence.split()}
print(output)