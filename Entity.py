from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlite.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    mid = Column(Integer, nullable=False)
    dup = Column(Boolean, nullable=False)
    state = Column(String(30), nullable=False)
    topic = Column(String(255), nullable=False)
    payload = Column(String(255), nullable=False)
    qos = Column(Integer, nullable=False)
    retain = Column(Boolean, nullable=False)

    def __init__(self, timestamp, mid, dup, state, topic, payload, qos, retain):
        self.timestamp = timestamp
        self.mid = mid
        self.dup = dup
        self.state = state
        self.topic = topic
        self.payload = payload
        self.qos = qos
        self.retain = retain

    def create(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    def read(self, id):
        session = Session()
        message = session.query(Message).filter_by(id=id).first()
        session.close()
        return message

    def update(self, id):
        session = Session()
        message = session.query(Message).filter_by(id=id).first()
        message.timestamp = self.timestamp
        message.mid = self.mid
        message.dup = self.dup
        message.state = self.state
        message.topic = self.topic
        message.payload = self.payload
        message.qos = self.qos
        message.retain = self.retain
        session.commit()
        session.close()

    def delete(self, id):
        session = Session()
        message = session.query(Message).filter_by(id=id).first()
        session.delete(message)
        session.commit()
        session.close()
        
    @classmethod
    def get_all_messages(cls, session):
        return session.query(cls).all()


class Subscription(Base):
    __tablename__ = 'subscription'
    id = Column(Integer, primary_key=True)
    topic = Column(String(255))
    qos = Column(Integer)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship("Client", back_populates="subscriptions")
    
    @classmethod
    def add_subscription(cls, session, client_id, topic):
        subscription = cls(client_id=client_id, topic=topic)
        session.add(subscription)
        session.commit()

    @classmethod
    def remove_subscription(cls, session, client_id, topic):
        subscription = session.query(cls).filter_by(client_id=client_id, topic=topic).first()
        if subscription:
            session.delete(subscription)
            session.commit()

    @classmethod
    def get_subscriptions(cls, session, client_id):
        subscriptions = session.query(cls).filter_by(client_id=client_id).all()
        return subscriptions

    @classmethod
    def get_clients(cls, session, topic):
        subscriptions = session.query(cls).filter_by(topic=topic).all()
        clients = [s.client for s in subscriptions]
        return clients
class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))
    subscriptions = relationship("Subscription", back_populates="client")
    
    def create(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    def read(self, id):
        session = Session()
        client = session.query(Client).filter_by(id=id).first()
        session.close()
        return client

    def update(self, id):
        session = Session()
        client = session.query(Client).filter_by(id=id).first()
        client.username = self.username
        client.password = self.password
        session.commit()
        session.close()

    def delete(self, id):
        session = Session()
        client = session.query(Client).filter_by(id=id).first()
        session.delete(client)
        session.commit()
        session.close()
        
Base.metadata.create_all(engine)