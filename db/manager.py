# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base


class SQLManager:
    def __init__(self, url = 'postgres://uswgcessxqcctc:e4b6be0cd49a2376569738f62300be0d508a66f5f0ca706609dff1d88303c205@ec2-54-225-96-191.compute-1.amazonaws.com:5432/d3keafn04h38j8'):
        self.engine = create_engine(url)

    def create_all_tables(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        Base.metadata.bind = self.engine
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        return session
