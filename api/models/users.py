from ..utils.db import db
 

class User(db.Model):
    __tablename__= 'users'

    id=db.Column(db.Integer(),primary_key=True)
    email=db.Column(db.String(80),nullable=False,unique=True)
    username = db.Column(db.String(25),nullable=False)
    password_hash=db.Column(db.Text(),nullable=False)
    is_active=db.Column(db.Boolean(),default=True)
    is_staff=db.Column(db.Boolean(),default=False)
    orders=db.relationship('Order',backref='user',lazy=True)

    def __repr__(self):
        f"<User {self.id} {self.username}>"


    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)