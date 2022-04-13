from flask import Flask, render_template, request
from babel import numbers, dates
from datetime import datetime, date, time
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


@babel.localeselector
def get_locale():
    return 'tk'

@app.route('/')
def index():

    anthony = gettext('anthony')
    # results = { 'us_date' : us_date }
    return render_template("index.html",  anthony = anthony)

if __name__ == '__main__':
    app.run(debug=True, port=5000)