from flask import render_template
from app import app, db, models
import datetime

"""
navbar:
0=default
1=collapsed
2=shade
"""

@app.route('/')
@app.route('/thesis')
def index():
    return render_template("thesis.html",
                           title="Thesis",
                           navbar=3)

@app.route('/article')
def article():
    return render_template("article.html",
                           title="Article",
                           navbar=1)

@app.route('/the_week')
def the_week():
    return render_template("the_week.html",
                           title="9/11",
                           navbar=2)

@app.route('/feed_rail')
def goings_on():
    return render_template("feed_rail.html",
                           title="Feed Rail",
                           navbar=1)

@app.route('/antarctica')
def antarctica():
    return render_template("antarctica.html",
                           title="Antarctica",
                           navbar=2)

@app.route('/charlie_wins')
def charlie_wins():
    return render_template("charlie_wins.html",
                           title="Charlie Wins")

@app.route('/blowback')
def blowback():
    return render_template("blowback.html",
                           title="Blowback")

@app.route('/reflection')
def reflection():
    return render_template("reflection.html",
                           title="A Reflection")


@app.route('/terrorism')
def terrorism():
    return render_template("terrorism.html",
                           title="Terrorism & the Taliban")

@app.route('/works_cited')
def works_cited():
    return render_template("works_cited.html",
                           title="Works Cited")
