import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security_bkup import authenticate, identity
from Resources.user_bkup import UserRegister
from Resources.item import Item, Item_list
from Resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Jose'
api = Api(app)


jwt = JWT(app, authenticate, identity)
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Item_list, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
