from .__init__ import db
class Lists(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(256))
	item = db.relationship('Items', backref='list_name')

class Items(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(256))
	list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))



