import json
from db import db, Ads
from server import app


def insert_ads_to_db(json_data):
    for ad in json_data:
        existing_ad = Ads.query.get(ad['id'])
        if existing_ad is None:
            ad_in_db = Ads(ad['id'], ad['settlement'], ad['under_construction'], ad['description'], ad['price'],
                           ad['oblast_district'], ad['living_area'], ad['has_balcony'], ad['address'],
                           ad['construction_year'], ad['rooms_number'], ad['premise_area'], active=True)
            db.session.add(ad_in_db)
        else:
            existing_ad.settlement = ad['settlement']
            existing_ad.under_construction = ad['under_construction']
            existing_ad.description = ad['description']
            existing_ad.price = ad['price']
            existing_ad.oblast_district = ad['oblast_district']
            existing_ad.living_area = ad['living_area']
            existing_ad.has_balcony = ad['has_balcony']
            existing_ad.address = ad['address']
            existing_ad.construction_year = ad['construction_year']
            existing_ad.rooms_number = ad['rooms_number']
            existing_ad.premise_area = ad['premise_area']
            existing_ad.active = True
    db.session.commit()
    return


def load_json_data(filepath):
    json_data = []
    with open(filepath) as data_file:
        json_data = json.load(data_file)
    return json_data


def reset_active_fields_in_ads(ads):
    for ad in ads:
        ad.active = False
    db.session.commit()
    return


if __name__ == "__main__":
    with app.app_context():
        reset_active_fields_in_ads(Ads.query.all())
        json_data = load_json_data('ads.json')
        insert_ads_to_db(json_data)
