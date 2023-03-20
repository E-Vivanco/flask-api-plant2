import os
from flask_cors import CORS
from flask import Flask,render_template,json, jsonify,request
#import mysql.connector
#import requests
#from utils import APIException, generate_sitemap
#from admin import setup_admin
from flask_migrate import Migrate
from dotenv import load_dotenv
from models import db,User,Character,Planet,Vehicle,Favorito


load_dotenv()

app = Flask(__name__)
app.url_map.slashes=False
app.config['DEBUG']=True
app.config['ENV']='development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] ="cualquier_palabra"
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URI')
#CORS(app)

# rrl de starw urlSW
db.init_app(app)
Migrate(app,db) # db init, db migrate, db upgrade
CORS(app, resources={r"/api/*": {"origins": "*"}})
#setup_admin(app)

@app.route("/")
def home():
    return render_template('index.html')

## User routes
@app.route('/api/users', methods=['GET'])
def get_users():

    # SELECT * FROM users;
    users = User.query.all() 
    users = list(map(lambda user: user.serialize(), users))

    return jsonify(users), 200

@app.route('/api/users', methods=['POST'])
def create_user():
    # INSERT INTO users() VALUES ()

    datos = request.get_json()
    user = User()
    user.name = datos['name']
    user.lastname = datos['lastname']
    user.email = datos['email']
    user.password = datos['password']
    user.save() # ejecuta add + commit


    return jsonify(user.serialize()), 201

@app.route('/api/users/<int:id>', methods=['PATCH'])
def update_user(id):
    # UPDATE user SET name="", lastname="" email="", password="" WHERE id = ?
    
    name = request.json.get('name') # None
    lastname = request.json.get('lastname') # None
    email =  request.json.get('email') # None
    password =  request.json.get('password') # None

    # SELECT * FROM users WHERE id = ?
    user = User.query.get(id)
    user.name = name
    user.lastname = lastname
    user.email = email
    user.password = password
    user.update()
    
    #db.session.commit()

    return jsonify(user.serialize()), 202

@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    # SELECT * FROM users WHERE id = ?
    user = User.query.get(id)

    # DELETE FROM users WHERE id=?
    user.delete()

    return jsonify({ "message": "User Deleted" }), 202

@app.route('/api/characters', methods=['GET'])
def get_character():

    characters = Character.query.all()
    characters = list(map(lambda character: character.serialize(), characters))

    return jsonify(characters), 200

@app.route('/api/characters', methods=['POST'])
def create_character():

    datos = request.get_json()
    character = Character()
    character.name = datos['name']
    character.mass = datos['mass']
    character.skin = datos['skin']
    character.hair = datos['hair']
    character.save()

    return jsonify(character.serialize()), 201
@app.route('/api/characters/<int:id>', methods=['PATCH'])
def update_character(id):
    # UPDATE user SET name="" WHERE id = ?
    
    name = request.json.get('name') # None
    mass = request.json.get('mass') # None
    skin =  request.json.get('skin') # None
    hair =  request.json.get('hair') # None

    # SELECT * FROM users WHERE id #
    character = Character.query.get(id)
    character.name = name
    character.mass = mass
    character.skin = skin
    character.hair = hair
    character.update()
    
    
    return jsonify(character.serialize()), 202
    
@app.route('/api/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    # SELECT * FROM users WHERE id = ?
    character = Character.query.get(id)

    # DELETE FROM users WHERE id=?
    character.delete()

    return jsonify({ "message": "Character Deleted" }), 202
    

@app.route('/api/planets', methods=['GET'])
def get_planet():

    planets = Planet.query.all()
    planets = list(map(lambda planet: planet.serialize(), planets))

    return jsonify(planets), 200

@app.route('/api/planets', methods=['POST'])
def create_planet():

    datos = request.get_json()
    planet = Planet()
    planet.name = datos['name']
    planet.climate = datos['climate']
    planet.terrain = datos['terrain']
    planet.gravity = datos['gravity']
    planet.diameter = datos['diameter']
    planet.save()

    return jsonify(planet.serialize()), 201

@app.route('/api/planets/<int:id>', methods=['PATCH'])
def update_planet(id):
    # UPDATE user SET name="" WHERE id = ?
    
    name = request.json.get('name') # None
    climate = request.json.get('climate') # None
    terrain =  request.json.get('terrain') # None
    gravity =  request.json.get('gravity') # None
    diameter =  request.json.get('diameter') # None

    # SELECT * FROM users WHERE id #
    planet = Planet.query.get(id)
    planet.climate = climate
    planet.terrain = terrain
    planet.gravity = gravity
    planet.diameter = diameter
    planet.update()
    
    
    return jsonify(planet.serialize()), 202
    
@app.route('/api/planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
    # SELECT * FROM users WHERE id = ?
    planet = Planet.query.get(id)

    # DELETE FROM users WHERE id=?
    planet.delete()

    return jsonify({ "message": "Character Deleted" }), 202

    
@app.route('/api/vehicles', methods=['GET'])
def get_vehicle():

    vehicles = Vehicle.query.all()
    vehicles = list(map(lambda vehicle: vehicle.serialize(), vehicles))

    return jsonify(vehicles), 200

@app.route('/api/vehicles', methods=['POST'])
def create_vehicle():

    datos = request.get_json()
    vehicle = Vehicle()
    vehicle.name = datos['name']
    vehicle.model = datos['model']
    vehicle.manufacturer = datos['manufacturer']
    vehicle.vehicleclass = datos['vehicleclass']
    vehicle.passerger = datos['passerger']
    vehicle.save()

    return jsonify(vehicle.serialize()), 201

@app.route('/api/vehicles/<int:id>', methods=['PATCH'])
def update_vehicle(id):
    # UPDATE user SET name="" WHERE id = ?
    
    name = request.json.get('name') # None
    model = request.json.get('model') # None
    manufacturer =  request.json.get('manufacturer') # None
    vehicleclass =  request.json.get('vehicleclass') # None
    passerger =  request.json.get('passerger') # None

    # SELECT * FROM users WHERE id #
    vehicle = Vehicle.query.get(id)
    vehicle.model = model
    vehicle.manufacturer = manufacturer
    vehicle.vehicleclass = vehicleclass
    vehicle.passerger = passerger
    vehicle.update()
    
    
    return jsonify(vehicle.serialize()), 202
    
@app.route('/api/vehicles/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    # SELECT * FROM users WHERE id = ?
    vehicle = Vehicle.query.get(id)

    # DELETE FROM users WHERE id=?
    vehicle.delete()

    return jsonify({ "message": "Character Deleted" }), 202

@app.route('/api/favoritos', methods=['GET'])
def get_favoritos():

    favoritos = Favorito.query.all()
    favoritos = list(map(lambda favorito: favorito.serialize(), favoritos))
    return jsonify(favoritos), 200

@app.route('/api/favoritos', methods=['POST'])
def create_favorito():

    datos = request.get_json()
    favorito = Favorito()
    favorito.user_id = datos['user_id']
    favorito.character_id = datos['character_id']
    favorito.planet_id = datos['planet_id']
    favorito.vehicle_id = datos['vehicle_id']
    favorito.save()

    return jsonify(favorito.serialize()), 201


@app.route('/api/favoritos/<int:id>', methods=['PATCH'])
def update_favorito(id):
    
    user_id = request.json.get('user_id')
    character_id = request.json.get('character_id')
    planet_id = request.json.get('planet_id')
    vehicle_id = request.json.get('vehicle_id')


    favorito = Favorito.query.get(id)
    favorito.user_id = user_id
    favorito.character_id = character_id
    favorito.planet_id = planet_id
    favorito.vehicle_id = vehicle_id
    favorito.update()

    return jsonify(favorito.serialize()), 200

@app.route('/api/favoritos/<int:id>', methods=['DELETE'])
def delete_favorito(id):

    favorito = Favorito.query.get(id)
    favorito.delete()

    return jsonify({ "message": "Favorite Deleted" }), 200



with app.app_context():
    db.create_all()
    

if __name__ == '__main__':
    app.run()