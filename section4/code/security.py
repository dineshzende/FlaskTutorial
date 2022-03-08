from user import User
users = [
    User(1,'bob', 'asdf'),
    User(2, 'alice', 'asdf')
]

username_mapping = {u.username : u  for u in users }
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    print(username," ", password)
    user = username_mapping.get(username, None)
    print(user.username , "-", user.password)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
