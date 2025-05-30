from flask import Flask,request

app = Flask(__name__)

stores = [
    {
        "name":"My Store",
        "items":[
            {
                "name":"chair",
                "price":15.99
            }
        ]
    }
]


@app.get('/store')
def get_stores():
    return {"stores":stores}

@app.post('/store')
def create_stores():
    request_data = request.get_json()
    new_store = {"name":request_data["name"],"item":[]}
    stores.append(new_store)
    return new_store,201

@app.post('/store/<string:name>/item')
def create_item(name):
    request_date = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_date["name"],"price":request_date["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message":"store not found"},404

@app.post('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message":"store not found"},404

@app.post('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message":"store not found"},404