from flask import Flask, current_app, request, Response
from flask_cors import CORS
from flask_restful import Api
from flask_migrate import Migrate
from database.db import db
from resources.profile import ProfileApi, ProfilesApi
from config import Config

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config.from_object(Config)

#Define MariaDB engine using MariaDB connector
app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+mysqlconnector://dating:password@127.0.0.1:3306/dating"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
      try :
            db.create_all()
      except Exception as ex :
            print('got the wrong create all'+str(ex))

api = Api(app)      
api.add_resource(ProfileApi, '/profiles')
api.add_resource(ProfilesApi, '/profiles/<id>')

with app.app_context():
    @current_app.before_request
    def basic_authentication():
        if request.method.lower() == 'options':
            return Response()

if __name__ == '__main__':
      app.run()
