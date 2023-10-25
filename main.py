class User:
    def __init__(self, name):
        self.name = name
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User('Peter')
user2 = User('Trinh')

print(user1.name, user1.followers, user1.following)
print(user2.name, user2.followers, user2.following)

user1.follow(user2)

print(user1.name, user1.followers, user1.following)
print(user2.name, user2.followers, user2.following)