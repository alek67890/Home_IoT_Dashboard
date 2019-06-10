from app import app
from flask import abort, request, render_template
from devices import devices


@app.route('/')
@app.route('/dashboard')
def dashboard():
    device = request.args.get('device')

    return render_template('dashboard.html', topic_list=devices.list_of_topics(), data=devices.data, active=device)


@app.route('/ok')
def ok():
    return('OK')



