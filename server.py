from flask import Flask, render_template, request
from db import db, Ads
from sqlalchemy import and_, or_
from datetime import datetime
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def ads_list():
    ads_per_page = 15
    default_page = 1
    page = request.args.get(get_page_parameter(), type=int, default=default_page)
    oblast_district = request.args.get('oblast_district')
    new_building = request.args.get('new_building', False)
    min_price = request.args.get('min_price', 0)
    if not min_price:
        min_price = 0
    max_price_of_ads = Ads.query.order_by(Ads.price)[-1].price
    max_price = request.args.get('max_price', max_price_of_ads)
    current_year = datetime.today().year
    if oblast_district is not None and bool(new_building) is True:
        ads = Ads.query.filter(Ads.active == True,
                               and_(Ads.price <= max_price, Ads.price >= min_price),
                               Ads.oblast_district == oblast_district,
                               or_(Ads.under_construction == True, Ads.construction_year >= current_year-2)
                               ).paginate(int(page), ads_per_page, False)
    elif oblast_district is None and bool(new_building) is True:
        ads = Ads.query.filter(Ads.active == True,
                               and_(Ads.price <= max_price, Ads.price >= min_price),
                               or_(Ads.under_construction == True, Ads.construction_year >= current_year - 2)
                               ).paginate(int(page), ads_per_page, False)
    elif oblast_district is not None and bool(new_building) is False:
        ads = Ads.query.filter(Ads.active == True,
                               and_(Ads.price <= max_price, Ads.price >= min_price),
                               Ads.oblast_district == oblast_district
                               ).paginate(int(page), ads_per_page, False)
    else:
        ads = Ads.query.filter(Ads.active == True,
                               and_(Ads.price <= max_price, Ads.price >= min_price)
                               ).paginate(int(page), ads_per_page, False)
    pagination = Pagination(page=page, total=ads.total, per_page=ads_per_page, css_framework='bootstrap3')
    if oblast_district is None:
        oblast_district = "Череповецкий район"
    return render_template('ads_list.html', ads=ads,
                           pagination=pagination, min_price=min_price,
                           max_price=max_price, new_building=new_building,
                           oblast_district=oblast_district)


if __name__ == "__main__":
    app.run()
