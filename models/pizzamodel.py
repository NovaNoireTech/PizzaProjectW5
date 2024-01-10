#  timezone
from datetime import datetime

from app import db
from . import UserModel

class pizzamodel(db.Model):

  __tablename__ = 'pizza'

  id = db.Column(db.Integer, primary_key = True)
  body = db.Column(db.String, nullable = False)
  timestamp = db.Column(db.String)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  user = db.relationship(UserModel, back_populates =  'pizza')

  def __repr__(self):
    return f'<pizza: {self.topping}>'
  
  def commit(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()