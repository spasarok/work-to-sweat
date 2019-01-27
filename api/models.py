from api.app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'), nullable=False)
    __tablename__ = 'users'

class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(9), unique=True, nullable=False)
    __tablename__ = 'days'

class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), unique=True, nullable=False)
    __tablename__ = 'genders'

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True, nullable=False)
    __tablename__ = 'workouts'

class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    __tablename__ = 'memberships'

class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), unique=True, nullable=False)
    __tablename__ = 'time'

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id_0 = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_id_1 = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    __tablename__ = 'messages'

class MembershipLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    membership_id = db.Column(db.Integer, db.ForeignKey('membership_locations.id'), nullable=False)
    __tablename__ = 'membership_locations'

class UserMembership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    membership_id = db.Column(db.Integer, db.ForeignKey('membership_locations.id'), nullable=False)
    __tablename__ = 'user_memberships'

class UserPrefDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    day_id = db.Column(db.Integer, db.ForeignKey('days.id'), nullable=False)
    __tablename__ = 'user_pref_days'

class UserPrefGender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'), nullable=False)
    __tablename__ = 'user_pref_genders'

class UserPrefLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    membership_location_id = db.Column(db.Integer, db.ForeignKey('membership_locations.id'), nullable=False)
    __tablename__ = 'user_pref_locations'

class UserPrefTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    time_id = db.Column(db.Integer, db.ForeignKey('times.id'), nullable=False)
    __tablename__ = 'user_pref_times'

class UserPrefWorkout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    __tablename__ = 'user_pref_workouts'
