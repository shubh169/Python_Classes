class User():
    def __init__(self,user_name,user_id):
        self.name = user_name
        self.id = user_id
        self.follors=0
        self.following=0

    def follow(self,user):
        self.follors+=1
        self.following += 1

user_1=User("John",1)
user_2=User("Shubham",2)

user_1.follow(user_2)

print(user_1.follors)
print(user_1.following)
print(user_2.follors)
print(user_2.following)