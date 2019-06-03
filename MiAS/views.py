from app import app
from flask import abort, request

@app.route('/')
def homepage():
    return('HELLO FLASK')


@app.route('/ok')
def ok():
    return('OK')

