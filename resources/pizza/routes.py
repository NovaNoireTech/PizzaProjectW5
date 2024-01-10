from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from models import pizzamodel
from schemas import PizzaSchema, PizzaSchemaNested

from . import bp
from resources import pizza


@bp.route('/<pizza_id>')
class Pizza(MethodView):

    @bp.response(200, PizzaSchemaNested)
    def get(self, pizza_id):
        post = pizzamodel.query.get(pizza_id)
        if pizza:
            print(pizza.author)
            return pizza
        abort(400, message = 'Invalid Pizza')

    @bp.arguements(PizzaSchema)
    def put(self, pizza_data, pizza_id):
        pizza = pizzamodel.query.get(pizza_id)
        if pizza: 
            pizza.toppings = pizza_data['toppings']
            pizza.commit()
            return {'message': 'pizza updated'}, 201
        return {'message': "Invalid Pizza Id"}, 400
    
    
    def delete(self, pizza_id):
        pizza = pizzamodel.query.get(pizza_id)
        if pizza:
            pizza.delete()
            return {"message": "Pizza Deleted"}, 202
        return {'message': "Invalid Pizza"}, 400

@bp.route('/')
class PizzaList(MethodView):

    @bp.response(200, PizzaSchema(many = True))
    def get (self):
        return pizzamodel.query.all()
    
    @bp.arguments(PizzaSchema)
    def pizza(self, pizza_data):
        try:
            pizza = pizzamodel()
            pizza.user_id = pizza_data ['user_id']
            pizza.toppings= pizza_data ['toppings']
            pizza.commit()
            return {'message': "Pizza Created" }, 201
        except:
            return {'message': "Invalid User"}, 401
      

    # def delete(self, pizza_id):
    #     data= request.delete_json()
    #     print (data)
    #     for d in data:
    #         pizza [d]=data[d]

# def pizzahome():
#     return users, 200

# @bp.route("/", methods=["POST"]) 

# def createpizza():
#     data= request.get_json()
#     print (data)
#     for d in data: 
#         pizza[d]= data[d]

    ###pizza[] 

#     return {"message": "pizza added", "pizza": pizza}

# @bp.delete("/")

# def delete():
#     return pizza, 200

# @bp.route("/", methods= ["POST"])

# def delete_pizza():
#     data= request.delete_json()
#     print (data)
#     for d in data:
#         pizza [d]=data[d]

#     return {"message": "pizza deleted", "pizza": pizza}

# @bp.get ('/pizza')
# def get_pizza():
#    return{ 'pizza': list(pizza.values()) }

# @bp.get ('/pizza/<pizza_id>')
# def get_pizza(pizza_id):
#   try:
#     return {'pizza': pizza[pizza_id]}, 200
#   except KeyError: 
#     return {'message': "Invalid Pizza"}, 400
  

# @bp.post('/pizza')
# def create_pizza():
#    pizza_data = request.get_json
#    user_id = pizza_data['user_id']
#    if user_id in users:
#       pizza[uuid4()] = pizza_data
#       return {'message': "Pizza Created" }, 201
#    return{'message': "Invalid User"}, 401

# @bp.put('/pizza/<pizza_id>')
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
   
# @bp.delete('/pizza/<pizza_id>')
# def delete_pizza(pizza_id):
#   try: 
#     del pizza [pizza_id]
#     return {"message": "Pizza Deleted"}, 202
#   except: 
#     return {'message': "Invalid Post"}, 400