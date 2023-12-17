from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
import os

TOP_SECRET_API_KEY = os.environ['TOP_SECRET_API_KEY']
app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dict = {}
        for col in self.__table__.columns:
            dict[col.name] = getattr(self, col.name)

        return dict


# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    result = db.session.execute(
        db.select(Cafe)
    ).scalars().all()

    random_cafe = random.choice(result)
    return jsonify(cafe=random_cafe.to_dict())

@app.route('/all')
def get_all_cafe():
    result = db.session.execute(
        db.select(Cafe)
    ).scalars().all()

    all_cafe_data = [cafe.to_dict() for cafe in result]
    return jsonify(cafes=all_cafe_data)

@app.route('/search/<loc>')
def get_loc_cafe(loc):
    result = db.session.execute(
        db.select(Cafe).where(Cafe.location == loc)
    ).scalars().all()
    if len(result) == 0:
        return jsonify(error={'Not Found': "Sorry, we don't have a cafe at that location."})
    else:
        cafe_data = [cafe.to_dict() for cafe in result]
        return jsonify(cafes=cafe_data)

# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('loc'),
        has_sockets=bool(request.form.get('sockets')),
        has_toilet=bool(request.form.get('toilet')),
        has_wifi=bool(request.form.get('wifi')),
        can_take_calls=bool(request.form.get('calls')),
        seats=request.form.get('seats'),
        coffee_price=request.form.get('coffee_price')
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(
        response={
            "success": "Successfully added new cafe"
        }
    )

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_coffee_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={
            "success": "Successfully updated coffee price"
        }), 200
    else:
        return jsonify(
            response={
                "not found": "Sorry, a cafe with that id was not found in the database"
            }
        ), 404


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if api_key == TOP_SECRET_API_KEY:
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(
                response={"success":"Successfully deleted cafe from database"}
            ), 200
        else:
            return jsonify(
                error={"Not found": "Sorry, a cafe with that id was not found in the database"}
            ), 404
    else:
        return jsonify(
            error={"Forbidden":"Sorry, that's not allowed. Make sure you have the correct API Key"}
        ), 403

if __name__ == '__main__':
    app.run(debug=True)
