class User:
    def __init__(self, user_id, username):
        self.id = user_id  # the attribute becomes the parameter passed in
        self.username = username  # self is the object
        self.followers = 0  # default value is zero


user_1 = User("001", "pete")
print(user_1.id)

# the __init__(self, attribute_1, attribute_2)
# this is a constructor that constructs the object
# this runs when the object is initialised from the class and
# runs whatever is below it essentially setting up the attributes

# you can also just add new attributes
#  user_1.home_town = "brighton"

# a function attached to a class is called a method.
# user = User() initialise
#     pass
# self is the actual object that's being created
#
