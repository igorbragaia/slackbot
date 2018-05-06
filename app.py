# -*- coding: utf-8 -*-
from flask import Flask, render_template
from db.operations import get_offered_trainings

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    trainings = get_offered_trainings()
    trainings = [[item.team, item.suggestion] for item in trainings]
    return render_template('index.html', trainings=trainings)


if __name__ == '__main__':
    app.run(debug=True)
