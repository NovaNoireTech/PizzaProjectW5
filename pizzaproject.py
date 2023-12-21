
from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

users = {
  '1': {
    'username': 'kedwards',
    'email' : 'kedwards@gmail.com'
  },
  '2' : {
    'username': 'kmassey',
    'email': 'kmassey@gmail.com'
  },
  '3' : {
    'username': 'sglover',
    'email': 'sglover@gmail.com'
  }

}

pizza = {
  '1' : {
    'toppings' : ['cheese', 'mushrooms'] ,
    'user_id': '1'
  },
  '2': {
    'toppings': ['cheese', 'pepperoni'] ,
    'user_id': '2'
  },
  '3':{
    'toppings': ['cheese', 'chicken'] ,
    'user_id' : '3'
  }
}

## @app.route("/", methods=["POST"])--- accepts get and post methods
@app.route("/")

def pizzahome():
    return users, 200

@app.route("/", methods=["POST"]) 

def createpizza():
    data= request.get_json()
    print (data)
    for d in data: 
        pizza[d]= data[d]

    ###pizza[] 

    return {"message": "pizza added", "pizza": pizza}

@app.delete("/")

def delete():
    return pizza, 200

@app.route("/", methods= ["POST"])

def delete_pizza():
    data= request.delete_json()
    print (data)
    for d in data:
        pizza [d]=data[d]

    return {"message": "pizza deleted", "pizza": pizza}

##returned pizza in insomnia, list not deleted