from ..utils.db import db
from enum import Enum


class Size(Enum):
    SMALL='small'
    MEDIUM='medium'
    LARGE='large'
    EXTRA_LARGE='extra-large'


class OrderStatus(Enum):
    PENDING='pending'
    IN_TRANSIT='in-transit'
    DELIVERED='delivered'


class Order(db.Model):
    __tablename__='orders'

    id=db.Column(db.Integer(),primary_key=True)
    size=db.Column(db.Enum(Size),default=Size.SMALL)
    order_status=db.Column(db.Enum(OrderStatus) ,default=OrderStatus.PENDING)
    flavour=db.Column(db.String(),nullable=False)
    quantity=db.Column(db.Integer())
    customer=db.Column(db.Integer(),db.ForeignKey('users.id'))

    def __str__(self):
        return f"<Order {self.id}>"


    def save(self):
        db.session.add(self)
        db.session.commit()

    