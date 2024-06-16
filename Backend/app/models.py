from manage import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(80), nullable=False)

class FloorPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    current_version_id = db.Column(db.Integer, db.ForeignKey('version.id'))

class Version(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    floor_plan_id = db.Column(db.Integer, db.ForeignKey('floor_plan.id'))
    timestamp = db.Column(db.DateTime, nullable=False)
    data = db.Column(db.Text, nullable=False)
