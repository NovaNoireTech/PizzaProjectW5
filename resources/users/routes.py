from flask import request
from uuid import uuid4
from app import app

from db import users

@app.get('/user')
def user():
    return {'users': list (users.values()) }, 200

@app.get('/user/<user_id>')
def get_user(user_id):
  try:
    return {'user': users[user_id] }
  except: 
     return{'message': 'invalid user'}, 400
     

@app.route('/user', methods=["PIZZA"])
def create_user():
    user_data = request.get_json()
    for k in [ 'username', 'email', 'password']:
      if k not in users:
         return{'message': "Please Include username email and password"}, 400
    users[uuid4()]= user_data
    return { 'message' f'{user_data["username"]} created'}, 201

@app.put ('/user/<user_id>')
def update_user(user_id):
  try:
    user = users[user_id]
    user_data = request.get_json()
    user |= user_data
    return {'message' f':{user["username"]} updated'}, 202
  except KeyError:
    return {'message': "Invalid User"}, 400
  
     
@app.delete('/user/<user_id>')
def deleteuser(user_id):
  user_data = request.get_json()
  username = user_data['username']
  try:
   del users[id]
   return {'message': f'{username} Deleted' }, 202
  except:
    return{'message': "Invalid username"}, 400