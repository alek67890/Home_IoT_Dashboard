from app import app
from flask import abort, request, render_template
from devices import objects


@app.route('/')
@app.route('/dashboard')
def dashboard():
    device = request.args.get('device', default='home')
    toggle = request.args.get('toggle', default=None)
    if device not in objects.list_of_topics():
        abort(404)
    if device == 'home':
        return render_template('dashboard.html', topic_list=objects.list_of_topics(), data=objects.data, active=device)
    else:
        return render_template('dash_device.html', topic_list=objects.list_of_topics(), data=objects.data, active=device)


@app.route('/ok')
def ok():
    return('OK')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', topic_list=objects.list_of_topics(), data=objects.data,), 404



