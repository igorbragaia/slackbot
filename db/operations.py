# -*- coding: utf-8 -*-
from collections import Counter
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
    cnt = Counter()

    for item in response:
        cnt[str(item)] += 1

    return cnt


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
    msg =  RequestedTraining(id_slack, team, suggestion)
    session.add(msg)
    session.commit()
    session.close()


def insert_offered_trainings(id_slack, team, suggestion):
    session = SQLManager().get_session()
    msg = OfferedTraining(id_slack, team, suggestion)
    session.add(msg)
    session.commit()
    session.close()


def get_unique_requested_trainings_with_quantity():
    session = SQLManager().get_session()
    response = session.query(RequestedTraining).all()
    session.close()
    cnt = Counter()

    for item in response:
        cnt[str(item)] += 1

    return cnt


def remove_string_from_db(id_slack, suggestion):
    session = SQLManager().get_session()
    suggestion = session.query(OfferedTraining).filter_by(id_slack=id_slack, suggestion=suggestion).first()
    if suggestion is not None:
        session.delete(suggestion)
        session.commit()
    session.close()


def remove_offered_training(id_slack, suggestion):
    session = SQLManager().get_session()
    response = session.query(OfferedTraining).filter_by(id_slack=id_slack, suggestion=suggestion).first()
    if response is not None:
        session.delete(response)
        session.commit()

    response = session.query(RequestedTraining).filter_by(id_slack=id_slack, suggestion=suggestion).first()
    if response is not None:
        session.delete(response)
        session.commit()
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
    # insert_requested_trainings("UAJ3F080G", "dev", "excel")
    # insert_requested_trainings("UAX3F080G", "vendas", "excel")
    # insert_requested_trainings("UAY3F080G", "vendas", "excel")
    # insert_requested_trainings("UAA3F080G", "vendas", "excel")
    # insert_requested_trainings("UAQ3F080G", "rh", "excel")
    # insert_requested_trainings("UAW3F080G", "rh", "excel")
    # insert_requested_trainings("UAE3F080G", "parcerias", "excel")
    # insert_requested_trainings("UAT3F080G", "parcerias", "excel")
    # insert_requested_trainings("UAI3F080G", "parcerias", "excel")
    # insert_requested_trainings("UAO3F080G", "parcerias", "excel")
    # insert_requested_trainings("UAP3F080G", "parcerias", "excel")
    # insert_requested_trainings("UAJ3A080G", "dev", "elixir")
    # insert_requested_trainings("UAX3B080G", "dev", "elixir")
    # insert_requested_trainings("UAY3C080G", "dev", "elixir")
    # insert_requested_trainings("UAA3D080G", "dev", "elixir")
    # insert_requested_trainings("UAQ3E080G", "dev", "elixir")
    # insert_requested_trainings("UAW3F080G", "rh", "typescript")
    # insert_requested_trainings("UAE3G080G", "dev", "typescript")
    # insert_requested_trainings("UAT3I080G", "dev", "typescript")
    # insert_requested_trainings("UAI3FJ80G", "dev", "react")
    # insert_requested_trainings("UAO3FK80G", "dev", "react")
    # insert_requested_trainings("UAP3FL80G", "dev", "angular")
    # insert_requested_trainings("UAP3FL80G", "dev", "angular")
    # insert_requested_trainings("UAP3FL80G", "dev", "angular")
    # insert_requested_trainings("UAP3FL80G", "dev", "vue")
    # insert_requested_trainings("UAP3FL80G", "dev", "vue")
    # insert_requested_trainings("UAP3FL80G", "dev", "vue")
    # insert_requested_trainings("UAP3FL80G", "dev", "vue")
    # insert_requested_trainings("parcerias", "parcerias", "vendas")
    # insert_requested_trainings("UAX3B080G", "parcerias", "pitch")
    # insert_requested_trainings("UAY3C080G", "parcerias", "vendas")
    # insert_requested_trainings("UAA3D080G", "parcerias", "vendas")
    # insert_requested_trainings("UAQ3E080G", "parcerias", "pitch")
    # insert_requested_trainings("UAW3F080G", "parcerias", "pitch")
    # insert_requested_trainings("UAE3G080G", "parcerias", "espanhol")
    # insert_requested_trainings("UAT3I080G", "parcerias", "espanhol")
    # insert_requested_trainings("UAI3FJ80G", "parcerias", "ingles")
    # insert_requested_trainings("UAO3FK80G", "rh", "pitch")
    # insert_requested_trainings("UAP3FL80G", "rh", "pitch")
    # insert_requested_trainings("UAP3FL80G", "rh", "pitch")
    # insert_requested_trainings("UAP3FL80G", "rh", "pitch")
    # insert_requested_trainings("UAP3FL80G", "rh", "pitch")
    # insert_requested_trainings("UAP3FL80G", "vendas", "pitch")
    # insert_requested_trainings("UAP3FL80G", "vendas", "ingles")
    # insert_requested_trainings("UAP3FL80G", "vendas", "ingles")
    # insert_requested_trainings("UAEXG080G", "dev", "vue")
    # insert_requested_trainings("UAT3W080G", "dev", "react")
    # insert_requested_trainings("UAI3QJ80G", "dev", "angular")
    # insert_requested_trainings("UAO3RK80G", "rh", "pitch")
    # insert_requested_trainings("UAR3FL80G", "vendas", "pitch")
    # insert_requested_trainings("URP3FL80G", "parcerias", "espanhol")
    # insert_requested_trainings("URP3FL80G", "parcerias", "ingles")
    # insert_requested_trainings("URP3FL80G", "rh", "espanhol")
    # insert_requested_trainings("RAP3FL80G", "rh", "pitch")
    # insert_requested_trainings("UAR3FL80G", "rh", "lideranca")
    # insert_requested_trainings("UAR3FL80G", "rh", "pitch")
    
    insert_offered_trainings("UAP3FL80G", "vendas", "ingles")
    insert_offered_trainings("UAP3FL80G", "vendas", "ingles")
    insert_offered_trainings("UAEXG080G", "dev", "vue")
    insert_offered_trainings("UAT3W080G", "dev", "react")
    insert_offered_trainings("UAI3QJ80G", "dev", "angular")
    insert_offered_trainings("UAO3RK80G", "rh", "pitch")
    insert_offered_trainings("UAR3FL80G", "vendas", "pitch")
    insert_offered_trainings("URP3FL80G", "parcerias", "espanhol")
    insert_offered_trainings("URP3FL80G", "parcerias", "ingles")
    insert_offered_trainings("URP3FL80G", "rh", "espanhol")
    insert_offered_trainings("RAP3FL80G", "rh", "pitch")
    insert_offered_trainings("UAR3FL80G", "rh", "lideranca")
    insert_offered_trainings("UAR3FL80G", "rh", "pitch")
