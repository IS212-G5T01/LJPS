import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_cors import CORS
from os import environ

# Flask App and DB connection is done here.
app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/LJPS_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

CORS(app)
db = SQLAlchemy(app)


#Skill in the LJPS System
class Skill(db.Model):
    __tablename__ = 'Skill'
    skill_id = db.Column(db.Integer, primary_key=True, nullable=False)
    skill_name = db.Column(db.String(100), nullable=False)
    skill_desc = db.Column(db.String(255), nullable=False)
    skill_status = db.Column(db.Integer, nullable=False)
    def __init__(self, skill_name, skill_desc, skill_status):
        self.skill_name = skill_name
        self.skill_desc = skill_desc
        self.skill_status = skill_status
        

    def json(self):
        return  {
            "skill_id": self.skill_id, 
            "skill_name": self.skill_name, 
            "skill_desc": self.skill_desc,
            "skill_status": self.skill_status
        }

@app.route("/")
def home():
    pass

#This segment of code is update details of a selected skill
#=============== Update Skill details by skill_id======================================
@app.route("/createSkill", methods=['POST'])
def change_apt():
    data = request.get_json()
    skill_name, skill_desc = "", ""
    if data['skill_name']:
        skill_name = data['skill_name']
    if data['skill_desc']:
        skill_desc = data['skill_desc']
    if (skill_name == "") or (skill_desc == ""):
        return jsonify(
            {
                "code": 500,
                "message": "Skill name or Skill desc is empty"
            }
        ) 
    skill = Skill(skill_id="", skill_name=skill_name, skill_desc=skill_desc, skill_status=1)
    try:
        db.session.commit(skill)
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating the skill."
            }
        ), 500

    return jsonify(
        {
            "code": 200,
            "data": skill.json()
        }
    )


#Run flask app
if __name__ == "__main__":
    app.run(debug=True)