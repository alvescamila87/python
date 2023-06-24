from itertools import count
from typing import Optional

from flask import Flask, request, jsonify
from flask_pydantic_spec import (
    FlaskPydanticSpec, Response, Request
)
from pydantic import BaseModel, Field
from tinydb import TinyDB, Query

server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title="Live Python Dunossauro")
spec.register(server)
database = TinyDB('database.json')
c = count()

class User(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
    name: str
    age: int

class Users(BaseModel):
    users: list[User]
    count: int

@server.get('/users') #rota, endpoint, recurso, url/uri
#@spec.validate(resp=Response(HTTP_200=User))
@spec.validate(resp=Response(HTTP_200=Users))
def get_users():
    """return all users from DB"""
    return jsonify(
        Users(
            user=database.all(),
            count=len(database.all())
        ).dict()
    )
@server.post('/users')
@spec.validate(
    body=Request(User), resp=Response(HTTP_200=User)
)
def post_user():
    """insert user on the DB"""
    body = request.context.body.dict()
    database.insert(body)
    return body

@server.put('/users/<int:id>')
@spec.validate(
    body=Request(User), resp=Response(HTTP_201=User)
)
def put_user(id):
    """update the user's info on the DB"""
    User = Query()
    body = request.context.body.dict()
    database.update(body, User.id == id)
    return jsonify(body)

@server.delete('/users/<int:id>')
@spec.validate(resp=Response('HTTP_204'))
def delete_user(id):
    """delete user from the DB"""
    User = Query()
    database.remove(User.id == id)
    return jsonify({})

server.run()