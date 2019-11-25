from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey, REAL, Numeric, DateTime, DECIMAL, BIGINT
from sqlalchemy.orm import relationship
from datetime import datetime
from Src import Base


class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_phone_number = Column(String, ForeignKey('user.phone_number'), nullable=False)
    user_table_relationship = relationship('User')
    amount = Column(String, nullable=False)
    currency = Column(String, default='VND')
    transaction_type = Column(String, nullable=False)
    detail = Column(String, nullable=False)
    note = Column(String, default=None)

    def __repr__(self):
        return '<Transaction id: %d>' % self.id


class Promotion(Base):
    __tablename__ = 'promotion'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    picture_url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    duration_from = Column(DateTime, nullable=False)
    duration_to = Column(DateTime, nullable=False)

    def __repr__(self):
        return '<Promotion id: %d>' % self.id


class User(Base):
    __tablename__ = 'user'
    phone_number = Column(String, primary_key=True, nullable=False)
    pin = Column(String, default=None)
    full_name = Column(String, default=None)
    birth_day = Column(DateTime, default=None)
    email = Column(String, default=None)
    point = Column(BIGINT, default=0)
    created_on_utc = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User Phone Number: %s>' % self.phone_number

    def serializer(self):
        return {
            'phone_number': self.phone_number,
            'full_name': self.full_name,
            'birth_day': self.birth_day,
            'email': self.email
        }


class SmsLog(Base):
    __tablename__ = 'sms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sms_time = Column(String)
    bank_account = Column(String)
    amount = Column(BIGINT)
    currency = Column(String)
    account_balance = Column(String)
    note = Column(String)
    user_gateway = Column(String)

    def __repr__(self):
        return '<Sms id: %s>' % self.id
