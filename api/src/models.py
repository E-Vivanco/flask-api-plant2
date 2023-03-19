from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), unique=False, nullable=False)
    lastname=db.Column(db.String(120),unique=False,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password
            # do not serialize the password, its a security breach
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=False, nullable=False)
    mass= db.Column(db.Integer, unique=False,nullable=False)
    skin=db.Column(db.String(80),unique=False, nullable=False)
    hair=db.Column(db.String(80),unique=False, nullable=False)
   

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'mass': self.mass,
            'skin':self.skin,
            'hair':self.hair
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=False, nullable=False)
    climate = db.Column(db.String(250),unique=False, nullable=False)
    terrain = db.Column(db.String(100),unique=False, nullable=False)
    gravity = db.Column(db.String(100),unique=False, nullable=False)
    diameter = db.Column(db.String(100),unique=False, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain,
            'gravity':self.gravity,
            'diameter':self.diameter
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=False, nullable=False)
    model = db.Column(db.String(250),unique=False, nullable=False)
    manufacturer = db.Column(db.String(200),unique=False, nullable=False)
    vehicleclass = db.Column(db.String(150),unique=False, nullable=False)
    passerger = db.Column(db.Integer,unique=False, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'vehicleclass':self.vehicleclass,
            'passerger':self.passerger
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()


class Favorito(db.Model):
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))

  
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'character_id': self.character_id,
            'planet_id': self.planet_id,
            'vehicle_id':self.vehicle_id
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()