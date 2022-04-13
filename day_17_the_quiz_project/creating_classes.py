class User:
    # using constructor to initialize attributes using special function init
    def __init__(self, user_id, username):  # as many parameters can be added here. self is the object being created
        self.id = user_id
        self.username = username
        self.followers = 0  # all objects created from this class starts with zero to begin with.
        # setting default values to parameters might not be good for all problems so assigned an attribute value outside
        self.following = 0
        print("creating new user.......")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("000001", "Neo")
# user_1.id = "0000001"
# user_1.username = "Neo"
# print(user_1.id + ":" + user_1.username)
# print(user_1.followers)


user_2 = User("000002", "Trinity")
# user_2.id = "0000002"
# user_2.username = "Trinity"
# print(user_2.id + ":" + user_2.username)
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
# SYNTAX FOR CREATING A NEW CLASS IS class ClassName:
# CLASS NAME SHOULD BE IN PASCAL CASE
# PASS CAN BE USED TO PASS THR CURRENT LINE AND CONTINUE TO TH NEXT LINE

# ADDING ATTRIBUTES


# user_1 = User()
# user_1.id = "0000001"
# user_1.username = "Neo"
# print(user_1.id + ":" + user_1.username)
#
#
# user_2 = User()
# user_2.id = "0000002"
# user_2.username = "Trinity"
# print(user_2.id + ":" + user_2.username)
