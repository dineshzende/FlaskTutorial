from flask import Flask
from flask_restful import Api,reqparse
from flask_jwt import JWT
from security import authenticate,identity
from user import UserRegister
from item import Item, Itemlist

app = Flask(__name__)
app.secret_key = "helloworld"


api = Api(app)



jwt = JWT(app,authenticate,identity ) #/auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist,'/items')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    app.run(port=5000,debug=True)