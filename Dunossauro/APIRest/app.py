from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec

server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title="Live Python Dunossauro")
spec.register(server)


@server.get('/users') #rota, endpoint, recurso, url/uri

def get_users():
    return 'Hello, users!'

server.run()