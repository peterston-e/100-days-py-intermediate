class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1  # updates attribute of parameter
        self.following += 1  # updates the object itself


user_1 = User("001", "pete")
user_2 = User("002", "dave")

user_1.follow(user_2)  # calls the method attached to the object
print(f"User 1 - {user_1.followers}")
print(f"User 1 - {user_1.following}")
print(f"User 2 - {user_2.followers}")
print(f"User 2 - {user_2.following}")
