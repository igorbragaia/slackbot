# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode,  DateTime
from datetime import datetime


Base = declarative_base()


class OfferedTraining(Base):
    __tablename__ = "offeredtraining"
    id = Column(Integer, primary_key=True)
    user = Column(Unicode(), unique=False, nullable=True)
    team = Column(Unicode(), unique=False, nullable=True)
    suggestion = Column(Unicode(), unique=False, nullable=True)
    date = Column(DateTime(timezone=True), unique=False, nullable=True)

    def __init__(self, user, team, suggestion):
        self.date = datetime.utcnow()
        self.user = user
        self.team = team
        self.suggestion = suggestion

    def __repr__(self):
        return "offered training {0} from {1}".format(self.suggestion, self.team)


class SuggestedTraining(Base):
    __tablename__ = "suggestedtraining"
    id = Column(Integer, primary_key=True)
    user = Column(Unicode(), unique=False, nullable=True)
    team = Column(Unicode(), unique=False, nullable=True)
    suggestion = Column(Unicode(), unique=False, nullable=True)
    date = Column(DateTime(timezone=True), unique=False, nullable=True)

    def __init__(self, user, team, suggestion):
        self.date = datetime.utcnow()
        self.user = user
        self.team = team
        self.suggestion = suggestion

    def __repr__(self):
        return "suggested training {0} from {1}".format(self.suggestion, self.team)


