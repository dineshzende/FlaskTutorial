from flask import Flask,jsonify, request

app = Flask(__name__)
stores = [
    {
        'name': 'mystore',
        'items' :[
            {
                'name' : 'item1',
                'price': 15.99
            }
        ]
    }
]

@app.route("/")
def home():
    return "Hello World"

    
# POST /store data:{name:}
@app.route('/store',methods=['POST'])
def create_store():
    data = request.get_json()
    new_store = {
        'name' : data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'Message': 'store not found in the database'})
    
# GET /store
@app.route('/stores')
def get_stores():
    return jsonify({'stores':stores})
    

# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : data['name'],
                'price' : data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'Message': 'Store not found'}), 404

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        return jsonify({'items': store['items']})
    return jsonify({'Message' : 'Store not found in the database'}), 404




app.run(port=5000,debug=True)