from app import app
from flask import abort, request, render_template

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/ok')
def ok():
    return('OK')



