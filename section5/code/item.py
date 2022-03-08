import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('price',
            type=float,
            required=True,
            help = "This field can not be left blank!"
        )
    
    @classmethod
    def find_by_name(cls,name):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        select_query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(select_query,(name,))
        row = result.fetchone()
        conn.close()

        if row:
            return {'item':{'name' : row[0], 'price': row[1]}}
        
        

    @jwt_required()
    def get(self,name):
        try:
            item = self.find_by_name(name)
        except:
            return {"Message" : "Excpetion in getting values from database"}, 500

        if item:
            return item
        return {"Message": "Item not found in the database"}
        
    @classmethod
    def insert(self,item):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        insert_query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(insert_query,(item['name'],item['price']))
        
        conn.commit()
        conn.close()

 
    def post(self,name):
        item = Item.find_by_name(name)
        if item:
            return {"Message" : "Item already in the database"}

        data = Item.parser.parse_args()
        item  = {'name': name , 'price' : data['price']}
        
        try:
            self.insert(item)
        except:
            return {"Message" : "Error occured while inserting item"},500

        return item,201
        
    def update(self,item):
        print("in update")
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        update_query = "UPDATE items SET price=? WHERE name=?"
        print(item['price'], " ", item['name'])
        cursor.execute(update_query,(item['price'],item['name']))
        
        conn.commit()
        conn.close()
       
    def delete(self,name):
        item = Item.find_by_name(name)
        if item:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()

            delete_query = "DELETE FROM items WHERE name=?"
            cursor.execute(delete_query,(name,))
            conn.commit()
            conn.close()

            return {'Message' : "Item Deleted"}
        else:
            return {"Message": "Item not found in the database"}
    
    def put(self,name):
        
        data = Item.parser.parse_args()

        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}

        if item is None:
            try:
                self.insert(updated_item)
            except:
                return{"Message" : "An error is occured"}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return{"Message" : "An error is occured"}, 500
            
        return updated_item

        


class Itemlist(Resource):
    def get(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        select_query = "SELECT * FROM items"
        result = cursor.execute(select_query)
        
        items= []

        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        
        conn.close()
        return {'items' : items}
    

        
