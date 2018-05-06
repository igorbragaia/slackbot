# -*- coding: utf-8 -*-
from flask import Flask, render_template
from db.operations import get_offered_trainings

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    # x = get_offered_trainings()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
