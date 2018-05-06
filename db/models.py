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
        return self.suggestion
        # return "offered training {0} from {1}".format(self.suggestion, self.team)


class RequestedTraining(Base):
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
        return self.suggestion
        # return "suggested training {0} from {1}".format(self.suggestion, self.team)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    id_slack = Column(Unicode(), unique=False, nullable=True)
    team = Column(Unicode(), unique=False, nullable=True)

    def __init__(self, id_slack, team):
        self.id_slack = id_slack
        self.team = team

    def __repr__(self):
        return "user {0}, team {1}".format(self.user, self.team)
