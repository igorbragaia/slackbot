# -*- coding: utf-8 -*-
from db.models import Training
from db.manager import SQLManager


def getTraining():
    session = SQLManager().get_session()
    session.query(Training).all()
    session.close()


def insertTraining(suggestion, team):
    session = SQLManager().get_session()
    msg = Training(suggestion, team)
    session.add(msg)
    session.commit()
    session.close()


if __name__ == '__main__':
    insertTraining("c++", "devops")
