from app import app
from flask import abort, request, render_template
from devices import objects


@app.route('/')
@app.route('/dashboard')
def dashboard():
    device = request.args.get('device')

    return render_template('dashboard.html', topic_list=objects.list_of_topics(), data=objects.data, active=device)


@app.route('/ok')
def ok():
    return('OK')



