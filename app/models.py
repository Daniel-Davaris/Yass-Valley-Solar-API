from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib


@login.user_loader
def load_user(id):
	"""User loader for flask login."""
	return User.query.get(int(id))


class User(UserMixin, db.Model):
	"""User table - renamed to Person to avoid sql injection attacks."""

	__tablename__ = 'person'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		"""Tells the class how to reperesnt itself."""
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		"""Runs the passwords through a hash and appends."""
		self.password_hash = generate_password_hash(str(password))

	def check_password(self, password):
		"""Checks a password against the hash."""
		return check_password_hash(self.password_hash, password)

	def avatar(self, size):
		"""Returns avatar of user."""
		digest = hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()
		self.profile_pic = \
			'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
				digest, size
			)
		return self.profile_pic


class Customer(db.Model):
    # Contact Details
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    phoneNum = db.Column(db.String(15))
    mobileNum = db.Column(db.String(15))
    emailAddress = db.Column(db.String(255))
    invoceNum = db.Column(db.Integer)

    # Owner details
    address = db.Column(db.String(255))
    suburb = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postCode = db.Column(db.Integer)
    directions = db.Column(db.String(255))

    # Property details
    propertyType = db.Column(db.String(255))
    storyType = db.Column(db.String(255))
    existingSystem = db.Column(db.String(255))
    switchboardSpecialRequirements = db.Column(db.String(255))
    undergroundPowerRequirements = db.Column(db.String(255))
    dataCableRequirements = db.Column(db.String(255))

    # Electical Details
    meteringType = db.Column(db.String(255))
    subMetering = db.Column(db.String(255))
    retailer = db.Column(db.String(255))
    phase = db.Column(db.String(255))
    poleNum = db.Column(db.String(255))
    transformerSize = db.Column(db.String(255))
    serviceType = db.Column(db.String(255))


    serviceMainsLen = db.Column(db.Integer)
    serviceMainsSize = db.Column(db.Integer)
    consumerMainsLen = db.Column(db.Integer)
    consumerMainsSize = db.Column(db.Integer)
    FSSLen = db.Column(db.Integer)
    FSSSize = db.Column(db.Integer)


    # Usage details
    loadProfile = db.Column(db.String(255))
    quater1DailyKWH = db.Column(db.String(255))
    quater2DailyKWH = db.Column(db.String(255))
    quater3DailyKWH = db.Column(db.String(255))
    quater4DailyKWH = db.Column(db.String(255))
    currentElectricityCost = db.Column(db.String(255))
    currentFitRate = db.Column(db.String(255))
    heatingSystem1 = db.Column(db.String(255))
    heatingSystem2 = db.Column(db.String(255))
    coolingSystems = db.Column(db.String(255))
    pool = db.Column(db.String(255))
    pumping = db.Column(db.String(255))
    hotWater = db.Column(db.String(255))
    floorHeating = db.Column(db.String(255))
    otherSigLoads = db.Column(db.String(255))



class Design(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    name = db.Column(db.String(255))

    inverterLocationAndMounting = db.Column(db.String(255))
    roofType = db.Column(db.String(255))
    panelOreintation = db.Column(db.String(255))
    roofHeight = db.Column(db.String(255))
    shading = db.Column(db.String(255))
    monitoring = db.Column(db.String(255))
    installationDifficulty = db.Column(db.String(255))
    notes = db.Column(db.String(255))

class Design_Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    design_id = db.Column(db.Integer)
    item_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    category = db.Column(db.Integer)
    # ADD MORE ROWS

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    
