from datetime import datetime
from sqlalchemy import desc, asc
from app.core.extensions import db


class Brand(db.Model):
    __tablename__ = 'brands'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.Text)

    @classmethod
    def create(cls, name, description):
        brand = cls(name=name, description=description)
        db.session.add(brand)
        db.session.commit()
        return brand

    @classmethod
    def edit_by_id(cls, id, name, description):
        brand = cls.query.get(id)
        brand.name = name
        brand.description = description
        db.session.commit()
        return brand

    @classmethod
    def delete(cls, id):
        brand = cls.query.get(id)
        db.session.delete(brand)
        return db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


class Phone(db.Model):
    __tablename__ = 'phones'
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
    brand = db.relationship('Brand', backref='phones')
    name = db.Column(db.String(100), unique=True)
    date_release = db.Column(db.Date)

    @classmethod
    def create(cls, name, brand_id, date_release):
        date = datetime.strptime(date_release, '%Y-%m-%d').date()
        phone = cls(name=name, brand_id=brand_id, date_release=date)
        db.session.add(phone)
        db.session.commit()
        return phone

    @classmethod
    def delete(cls, id):
        phone = cls.query.get(id)
        db.session.delete(phone)
        return db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all_paginate(cls, order, page, per_page=10):
        sort = asc(cls.id) if order == 'asc' else desc(cls.id)
        return cls.query.order_by(sort).paginate(page=page, per_page=per_page).items