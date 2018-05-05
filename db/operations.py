# -*- coding: utf-8 -*-
from db.models import Training
from db.manager import SQLManager
from pprint import pprint
from datetime import datetime
from datetime.datetime import utcnow


def getTraining():
    session = SQLManager().get_session()
    response = session.query(Training).all()
    session.close()
    return response


def insertTraining(suggestion, team):
    session = SQLManager().get_session()
    msg = Training(suggestion, team)
    session.add(msg)
    session.commit()
    session.close()


if __name__ == '__main__':
    insertTraining("c#", "devops")
    x = getTraining()

    from pprint import pprint
    pprint(x)
