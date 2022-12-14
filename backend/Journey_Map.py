from flask import  request, jsonify
from db_connector import db

# Journey Map Table
class Journey_Map(db.Model):
    __tablename__ = 'Journey_Map'
    __table_args__ = {'extend_existing': True}
    jm_fk_journey_id = db.Column(db.Integer, primary_key=True, nullable=False)
    jm_fk_course_id = db.Column(
        db.String(20), primary_key=True, nullable=False)

    def __init__(self, jm_fk_journey_id, jm_fk_course_id):
        if not isinstance(jm_fk_journey_id, int):
            raise TypeError("jm_fk_journey_id must be an Integer")
        if not isinstance(jm_fk_course_id, str):
            raise TypeError("jm_fk_course_id must be a String")
        self.jm_fk_journey_id = jm_fk_journey_id
        self.jm_fk_course_id = jm_fk_course_id

    def json(self):
        return {
            "jm_fk_journey_id": self.jm_fk_journey_id,
            "jm_fk_course_id": self.jm_fk_course_id
        }

#Functions (CRUD)
# ********************************* Create ********************************* 
# Create a new journey map
def create_journey_map(jm_fk_journey_id, jm_fk_course_id):
    data = request.get_json()
    new_map = Journey_Map(
        data['jm_fk_journey_id'], data['jm_fk_course_id'])
    if data and new_map:
        try:
            db.session.add(new_map)
            db.session.commit()
        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "An error occurred creating the record."
                }
            ), 500

        return jsonify(
            {
                "code": 201,
                "data": new_map.json(),
                "message": "Success"
            }
        ), 201


# ********************************* Retrieve *********************************
#Get all journey maps
def get_journey_maps(jm_fk_journey_id):
    journeyMaps = Journey_Map.query.filter_by(jm_fk_journey_id = jm_fk_journey_id).all()
    if journeyMaps:
        return jsonify(
            {
                "code": 200,
                "data":
                [j.json() for j in journeyMaps]
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "No journey maps found."
            }
        ) 


# ********************************* Update ********************************* 


# ********************************* Delete ********************************* 
# Delete a journey map
def delete_journey_map(jm_fk_journey_id,jm_fk_course_id):
    del_map = Journey_Map.query.filter_by(jm_fk_journey_id = jm_fk_journey_id, jm_fk_course_id = jm_fk_course_id).first()
    if del_map:
        db.session.delete(del_map)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "message": "Journey Map removed successfully"
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Journey Map not found."
        }
    ), 404




