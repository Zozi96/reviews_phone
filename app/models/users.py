from app.core.extensions import db, bcrypt
from flask_jwt_extended import get_jwt_identity

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String,
        nullable=False
    )


    @classmethod
    def create(cls, username, email, password):
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        user = cls(
            username=username,
            email=email,
            password=pw_hash
        )
        db.session.add(user)
        db.session.commit()
        return user

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @classmethod
    def delete(cls, id):
        user = cls.query.get(id)
        db.session.delete(user)
        return db.session.commit()

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_current_identity(cls):
        return User.get(get_jwt_identity())
