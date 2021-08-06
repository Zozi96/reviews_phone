from app.core.extensions import db


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    phone_id = db.Column(db.Integer, db.ForeignKey('phones.id'))
    phone = db.relationship('Phone', backref='reviews')
    text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='reviews')

    @classmethod
    def create(cls, phone, text, user_id):
        review = cls(phone=phone, text=text, user_id=user_id)
        db.session.add(review)
        db.session.commit()
        return review

    @classmethod
    def delete(cls, id):
        review = cls.query.get(id)
        db.session.delete(review)
        return db.session.commit()
