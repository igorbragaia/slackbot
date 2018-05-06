# -*- coding: utf-8 -*-
from db.models import OfferedTraining, RequestedTraining, User
from db.manager import SQLManager
from pprint import pprint

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


def get_unique_offered_trainings_with_quantity():
    session = SQLManager().get_session()
    response = session.query(OfferedTraining).all()
    session.close()
    print("response:")
    print(response)

    print("list(response):")
    type(response)
    type(response[0])
    print(list(response))
    l = sorted(list(response))
    print(l)
    unique = []
    count = 0
    last_val = ""

    for i in range(len(l)):
        item = l[i]
        count += 1
        if last_val == "":
            last_val = item
        if item != last_val:
            last_val = item
            unique.append({
                "text": item,
                "count": count
            })
            count = 0

    return unique


def get_requested_trainings():
    session = SQLManager().get_session()
    response = session.query(RequestedTraining).all()
    session.close()
    return response


def get_unique_requested_trainings():
    session = SQLManager().get_session()
    response = session.query(RequestedTraining).all()
    session.close()
    unique = set([item.suggestion for item in response])
    return unique


def insert_requested_trainings(id_slack, team, suggestion):
    session = SQLManager().get_session()
    msg = OfferedTraining(id_slack, team, suggestion)
    session.add(msg)
    session.commit()
    session.close()


def insert_offered_trainings(id_slack, team, suggestion):
    session = SQLManager().get_session()
    msg = RequestedTraining(id_slack, team, suggestion)
    session.add(msg)
    session.commit()
    session.close()


def remove_string_from_db(text):
    session = SQLManager().get_session()

    session.close()


def insert_user(id_slack, team):
    session = SQLManager().get_session()
    user = User(id_slack, team)
    session.add(user)
    session.commit()
    session.close()


def get_user(id_slack):
    session = SQLManager().get_session()
    response = session.query(User).filter_by(id_slack=id_slack).first()
    session.close()
    if response is not None:
        return response.team
    else:
        return None


if __name__ == '__main__':
    # insert_suggested_training("Igor Bragaia", "c#", "devops")
    # insert_suggested_training("Igor sdfsd", "c#", "dev")
    # insert_suggested_training("sd Braffadsfadgaia", "excel", "mkt")
    # insert_suggested_training("sd Braffadsfadgaia", "excel", "mkt")
    # insert_suggested_training("sd Braffadsfadgaia", "excel", "mkt")
    # insert_suggested_training("qq Bfaragaia", "excel", "devops")
    # insert_suggested_training("fdas Bragaia", "c#", "devops")
    # insert_suggested_training("kk Bragaia", "c++", "dev")
    # insert_offered_training("Igor Bragaia", "c#", "devops")
    # x = get_offered_trainings()
    # x = get_suggested_trainings()

    # insert_user("csd3", "igor", "dev")
    from pprint import pprint
    x = get_user("123121x")
    pprint(x)
    x = get_user("x21123")
    pprint(x)
