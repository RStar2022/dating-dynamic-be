from flask import Blueprint, Response, request, jsonify
from flask_restful import Resource
from database.models import Profile
from database.db import db
from datetime import datetime
from requests import get

class ProfileApi(Resource):
    def get(self):
        get_profile = Profile.query.to_json()
        return Response(get_profile, mimetype="applicaton/json", status=200)

    def post(self):
        try : 
            body = request.get_json()
            # Get each json_data and put it into new variable
            req_name = body['name']
            date = body['date']
            req_date = datetime.strptime(date, '%m-%d-%Y').date()
            req_occupation = body['occupation']
            req_hobby = body['hobby']
            req_gender = body['gender']
            pic = body['img'].encode("utf-8")
            data = Profile(name = req_name, date = req_date, occupation = req_occupation, hobby = req_hobby, gender = req_gender, img = pic)
            db.session.add(data)
            db.session.commit()
            id = data.id
            return {'id':str(id)}, 200
        except Exception as e:
            messages = str(e)
            return messages, 400

class ProfilesApi(Resource):
    def put(self, id):
        try :
            profile = Profile.query.filter_by(id=id).first()
            body = request.get_json()
            profile.name = body["name"]
            db.session.commit()
            date = body["date"]
            profile.date = datetime.strptime(date, '%m-%d-%Y').date()
            db.session.commit()
            profile.hobby = body["hobby"]
            db.session.commit()
            profile.gender = body["gender"]
            db.session.commit()
            profile.img = body["img"]
            db.session.commit()
            return 'Update successful', 200
        except Exception as e:
            messages = "Error for updating your data"
            return messages, 400
    
    def get(self, id):
        #try : 
            profile_info = Profile.query.filter_by(id=id).first()
            return jsonify(profile_info.as_dict())
"""except Exception as e:
messages = "Your ID is not saved in database"
return messages, 400"""
        



