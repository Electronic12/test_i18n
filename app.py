from flask import Flask, render_template, request, session, redirect
from babel import numbers, dates
from datetime import datetime, date, time
from flask_babel import Babel, format_date, gettext
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


#session['language'] = Config.BABEL_DEFAULT_LOCALE

@babel.localeselector
def get_locale():
    language = Config.BABEL_DEFAULT_LOCALE
    if 'language' in session:
        language = session['language'] if session['language'] else Config.BABEL_DEFAULT_LOCALE
    return language

@app.route('/')
def index():

    anthony = gettext('anthony')
    # results = { 'us_date' : us_date }
    return render_template("index.html",  anthony = anthony)

# /change-language/tk
@app.route('/change-language/<code>')
def change_language(code):
    session['language'] = code
    return redirect('/')
    #return {'language': session['language']}

if __name__ == '__main__':
    app.run(debug=True, port=5000)