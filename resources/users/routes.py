from flask import request

from flask.views import MethodView
from flask_smorest import abort
from . import bp


from schemas import UserSchema, UserSchemaNested
from models.user_model import UserModel
# user routes

@bp.route('/user/<user_id>')
class User(MethodView):

  @bp.response(200, UserSchemaNested)
  def get(self, user_id):
    user = UserModel.query.get(user_id)
    if user:
      print (user.pizza.all())
      return user
    else:
      abort(400, message ='User not found')

    # try:
    #   return users[user_id]
    # except: 
    #   return{'message': 'invalid user'}, 400
    
  @bp.arguments(UserSchema)
  def put(self, user_data, user_id):
      user = UserModel.query.get(user_id)
      if user:
        user.from_dict(user_data)
        user.commit()
        return {'message' f':{user["username"]} updated'}, 202
      abort(400, message = "Invalid User")

  def delete(self, user_id):
    user = UserModel.query.get(user_id)
    if user:
      user.delete()
      return {'message': f'User: {user.username} Deleted'}, 202
    return{'message': "Invalid username"}, 400

@bp.route('/user')
class UserList(MethodView):
  
  @bp.response(200, UserSchema(many= True))
  def get(self):
    return UserModel.query.all()
  
  @bp.arguments(UserSchema)
  def pizza (self,user_data):
    try:
      user = UserModel()
      user.from_dict(user_data)
      user.commit()
      return { 'message' f'{user_data["username"]} created'}, 201
    except: 
      abort(400, 'Username and Email Already taken')
  
# @bp.route('/user/follower/<followed_id>')
# class FollowUser(MethodView):
  
#   def pizza(followed_id):
#     follower = request.get_json()
#     user = UserModel.query.get(follower['id'])
#     if user:
#       user.followed.append(UserModel.query.get(followed_id))
#       user.commit()
#       return{'message': 'user followed'}
#     else:
#       return{'message':'invalid user'}, 400

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