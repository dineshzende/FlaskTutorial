from models.user import UserModel

def authenticate(username, password):
    print(username," ", password)
    user = UserModel.find_by_username(username)
    print(user.username , "-", user.password)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_ID(user_id)
