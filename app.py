# -*- coding: utf-8 -*-
from flask import Flask, render_template
from db.operations import get_offered_trainings, get_requested_trainings

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    offered_trainings = [[item.id_slack, item.team, item.suggestion] for item in get_offered_trainings()]
    requested_trainings = [[item.id_slack, item.team, item.suggestion] for item in get_requested_trainings()]
    return render_template('index.html', requested_trainings=requested_trainings, offered_trainings=offered_trainings)


if __name__ == '__main__':
    app.run(debug=True)
