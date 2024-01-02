from flask import request
from uuid import uuid4

from app import app
from db import users, pizza

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

# @app.get ('/pizza')
# def get_pizza():
#    return{ 'pizza': list(pizza.values()) }

# @app.get ('/pizza/<pizza_id>')
# def get_pizza(pizza_id):
#   try:
#     return {'pizza': pizza[pizza_id]}, 200
#   except KeyError: 
#     return {'message': "Invalid Pizza"}, 400
  

# @app.post('/pizza')
# def create_pizza():
#    pizza_data = request.get_json
#    user_id = pizza_data['user_id']
#    if user_id in users:
#       pizza[uuid4()] = pizza_data
#       return {'message': "Pizza Created" }, 201
#    return{'message': "Invalid User"}, 401

# @app.put('/pizza/<pizza_id>')
# def update_pizza(pizza_id):
#   try:
#     pizza = pizza[pizza_id]
#     pizza_data = request.get_json()
#     if pizza_data['user_id'] == pizza ['user_id']:
#       pizza['toppings'] = pizza_data['toppings']
#       return {'message': 'Pizza Updated' }, 202
#     return {'message': "Unauthorized"}, 401
#   except: 
#      return {'message': "Invalid Pizza Id"}, 400
   
# @app.delete('/pizza/<pizza_id>')
# def delete_pizza(pizza_id):
#   try: 
#     del pizza [pizza_id]
#     return {"message": "Pizza Deleted"}, 202
#   except: 
#     return {'message': "Invalid Post"}, 400