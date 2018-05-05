# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode,  DATETIME
from datetime import datetime


Base = declarative_base()


class Training(Base):
    __tablename__ = 'training'
    id = Column(Integer, primary_key=True)
    suggestion = Column(Unicode(), unique=False, nullable=True)
    team = Column(Unicode(), unique=False, nullable=True)
    date = Column(DATETIME(timezone=True), unique=False, nullable=True)

    def __init__(self, suggestion, team):
        self.date = datetime.utcnow()
        self.suggestion = suggestion
        self.team = team

    def __repr__(self):
        return "training {0} from {1}".format(self.suggestion, self.team)

