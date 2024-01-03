from flask import request
from uuid import uuid4
from flask.views import MethodView

from . import bp
from db import users

from schemas import UserSchema
# user routes

@bp.route('/user/<user_id>')
class User(MethodView):


  @bp.response(200, UserSchema)
  def get(self, user_data, user_id):
    try:
      return users[user_id]
    except: 
      return{'message': 'invalid user'}, 400
    
  @bp.arguments(UserSchema)

  def put(self, user_data, user_id):
    try:
      user = users[user_id]
      user |= user_data
      return {'message' f':{user["username"]} updated'}, 202
    except KeyError:
      return {'message': "Invalid User"}, 400

  def delete(self, user_id):
    try:
      del users[user_id]
      return {'message': f'User Deleted'}, 202
    except:
      return{'message': "Invalid username"}, 400

@bp.route('/user')
class UserList(MethodView):
  
  @bp.response(200, UserSchema(many= True))
  def get(self):
    return list(users.values())
  
  @bp.arguments(UserSchema)
  def post(self,user_data):
    users[uuid4()]= user_data
    return { 'message' f'{user_data["username"]} created'}, 201
  
# @bp.response(200, UserSchema(many=True))
# @bp.get('/user')
# def user():
#     return {'users': list (users.values()) }, 200

# @bp.get('/user/<user_id>')
# @bp.response(200, UserSchema)
# def get_user(user_id):
#   try:
#     return {'user': users[user_id] }
#   except: 
#      return{'message': 'invalid user'}, 400
     

# @bp.route('/user', methods=["PIZZA"])
# @bp.arguments(UserSchema)
# def create_user():
#     user_data = request.get_json()
#     users[uuid4()]= user_data
#     return { 'message' f'{user_data["username"]} created'}, 201
    # for k in [ 'username', 'email', 'password']:
    #   if k not in users:
    # abort( {'message': "Please Include username email and password"}, 400)
    # users[uuid4()]= user_data
  

# @bp.put ('/user/<user_id>')
# def update_user(user_id):
#   try:
#     user = users[user_id]
#     user_data = request.get_json()
#     user |= user_data
#     return {'message' f':{user["username"]} updated'}, 202
#   except KeyError:
#     return {'message': "Invalid User"}, 400
  
     
# @bp.delete('/user/<user_id>')
# def deleteuser(user_id):
#   user_data = request.get_json()
#   username = user_data['username']
#   try:
#    del users[id]
#    return {'message': f'{username} Deleted' }, 202
#   except:
#     return{'message': "Invalid username"}, 400