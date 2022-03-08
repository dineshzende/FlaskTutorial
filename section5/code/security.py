from user import User

def authenticate(username, password):
    print(username," ", password)
    user = User.find_by_username(username)
    print(user.username , "-", user.password)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_ID(user_id)
