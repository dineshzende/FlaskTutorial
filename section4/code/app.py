from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate,identity

app = Flask(__name__)
app.secret_key = "helloworld"
api = Api(app)

jwt = JWT(app,authenticate,identity ) #/auth

items = []

class Item(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('price',
            type=float,
            required=True,
            help = "This field can not be left blank!"
        )
    
    @jwt_required()
    def get(self,name):
        for item in items:
            if item['name'] == name:
                return item
        return {'Message' : 'Item not found in the database'},404

    def post(self,name):
        if next(filter(lambda x: x['name']==name, items),None) is not None:
            return {'Message': "An item with name '{}' already exists".format(name)}, 400
        
        data = Item.parser.parse_args()
        item  = {'name': name , 'price' : data['price']}
        items.append(item)
        return item

        
    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name'] != name,items))
        return {'Message' : "Item Deleted"}
    
    def put(self,name):
        
        data = Item.parser.parse_args()
                
        item = next(filter(lambda x: x['name'] == name,items), None)
        if item is None:
            item = {'name': name, 'price' : data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

        


class Itemlist(Resource):
    def get(self):
        return {'Items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist,'/items')


app.run(port=5000,debug=True)