from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Ads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    settlement = db.Column(db.String(40))
    under_construction = db.Column(db.Boolean)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, index=True)
    oblast_district = db.Column(db.String(40), index=True)
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean)
    address = db.Column(db.String(40))
    construction_year = db.Column(db.Integer, index=True)
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float)
    active = db.Column(db.Boolean)

    def __init__(self, id, settlement, under_construction, description, price,
                 oblast_district, living_area, has_balcony, address,
                 construction_year, rooms_number, premise_area, active):
        self.id = id
        self.settlement = settlement
        self.under_construction = under_construction
        self.description = description
        self.price = price
        self.oblast_district = oblast_district
        self.living_area = living_area
        self.has_balcony = has_balcony
        self.address = address
        self.construction_year = construction_year
        self.rooms_number = rooms_number
        self.premise_area = premise_area
        self.active = active
