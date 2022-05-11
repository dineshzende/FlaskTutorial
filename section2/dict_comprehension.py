users = [
    (0, "Bob" , "pass123"),
    (1, "Rolf" , "1234"),
    (2, "Anne", "ann1111")
]

user_mappings = {user[1]: user for user in users }

user_input = input("Enter username :")
password_input = input("Enter password :")

_,username,password = user_mappings[user_input]
print(f"Username : {username} and the password is {password}")
_,username,password = user_mappings[password_input]
print(f"Username : {username} and the password is {password}")