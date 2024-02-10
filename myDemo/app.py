from flask import Flask, request

app = Flask(__name__)

stores =[{
    
    "name"  : "Furniture",
    
    "Items" :  [
        
        {
            "name"  : "chair",
            "price"  : "19.09"            
            
        }
    ]  },
         
         {
    
    "name"  : "Toys",
    
    "Items" :  [
        
        {
            "name"  : "Transformers",
            "price"  : 20.09            
            
        }
    ]   
    
}
    
]




@app.get("/stores")
def get_stores():
    
        return {"stores" : stores}
    
@app.post("/stores")
def post_stores():
    request_data= request.get_json()
    
    new_store={**stores , "name" : request_data["name"], "items" :request_data["items"]}
    return new_store,200

@app.post("/stores/<string:name>/Items")
def post_storesitem(name) :
        
        request_data= request.get_json()
        for store in stores :
            if store["name"]== name: 
                new_item ={"name" : request_data["name"], "price" :request_data["price"]}
                store["Items"].append(new_item)
                return stores
            
        return {"message" :"Store not found"} ,404    
        
@app.get("/stores/<string:name>")
def get_storesitem(name) :
    
     for store in stores :
            if store["name"]== name: 
                return {"items" : store["Items"]}
    
     return {"message" :"Store not found"} ,404   
    
    