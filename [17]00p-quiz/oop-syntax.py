class User:
    def __init__(self,username, userid):#initialize attributes
        print("Welcome to instagram")
        self.username = username#makes an attribute username for the object and sets its value to username
        self.id = userid
        self.followers = 0#we can also set attribute values here itself
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("Vanshav", 1)

user_2 = User("Keshav", 2)
user_2.follow(user_1)

print(f"user_1's followers = {user_1.followers}")
print(f"user_1's followings = {user_1.following}")
print(f"user_2's followers = {user_2.followers}")
print(f"user_2's followings = {user_2.following}")