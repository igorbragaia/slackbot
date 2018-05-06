# -*- coding: utf-8 -*-
from db.models import OfferedTraining, SuggestedTraining
from db.manager import SQLManager


def get_offered_trainings():
    session = SQLManager().get_session()
    response = session.query(OfferedTraining).all()
    session.close()
    return response


def get_unique_offered_trainings():
    session = SQLManager().get_session()
    response = session.query(OfferedTraining).all()
    session.close()
    unique = set([item.suggestion for item in response])
    return unique


def get_suggested_trainings():
    session = SQLManager().get_session()
    response = session.query(SuggestedTraining).all()
    session.close()
    return response


def get_unique_suggested_trainings():
    session = SQLManager().get_session()
    response = session.query(SuggestedTraining).all()
    session.close()
    unique = set([item.suggestion for item in response])
    return unique


def insert_suggested_trainings(user, team, suggestion):
    session = SQLManager().get_session()
    msg = OfferedTraining(user, team, suggestion)
    session.add(msg)
    session.commit()
    session.close()


def insert_offered_trainings(user, team, suggestion):
    session = SQLManager().get_session()
    msg = SuggestedTraining(user, team, suggestion)
    session.add(msg)
    session.commit()
    session.close()


if __name__ == '__main__':
    # insert_suggested_training("Igor Bragaia", "c#", "devops")
    # insert_offered_training("Igor Bragaia", "c#", "devops")
    x = get_offered_trainings()
    x = get_suggested_trainings()

    from pprint import pprint
    pprint(x)
