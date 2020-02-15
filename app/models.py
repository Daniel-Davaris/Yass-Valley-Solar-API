from app import db


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

    
