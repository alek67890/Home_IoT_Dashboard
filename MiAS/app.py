from flask import Flask
from flask_mqtt import Mqtt

from config import Configuration
from devices import objects

import json




app = Flask(__name__)
app.config.from_object(Configuration)

mqtt = Mqtt()
mqtt.init_app(app)




@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):

    for topic in objects.list_of_topics():
        if objects.type_device(topic) in ["Device", "DeviceSensor"]:
            mqtt.subscribe(topic + '/stat/POWER')
            mqtt.subscribe(topic + '/tele/LWT')

        if objects.type_device(topic) in ["DeviceSensor"]:
            mqtt.subscribe(topic + '/tele/SENSOR')



@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    # print('topic =')
    # print(data['topic'])
    # print('payload =')
    # print(data['payload'])
    topic = data['topic'].split('/')

    if objects.check(topic[0]):
        if topic[2] == 'POWER':
            if data['payload'] == 'ON':
                objects.data[topic[0]].on()
            if data['payload'] == 'OFF':
                objects.data[topic[0]].off()

        if topic[2] == 'LWT': # Last Will / Is Online or Not
            if data['payload'] == 'Online':
                objects.data[topic[0]].online()
            if data['payload'] == 'Offline':
                objects.data[topic[0]].ofline()

        if topic[2] == 'SENSOR':
            # pass
            power_data = json.loads(data['payload'])
            print(power_data['Time'])
            time = power_data['Time']
            power = power_data['ENERGY']
            objects.data[topic[0]].new_power(power, time)
            # devices.data[topic[0]].new_power()  use_power

        txt = topic[0] + ' is ' + data['payload'] + '->' + topic[1] + '->' + topic[2]
        print(txt)

        # print(devices.data[topic[0]].is_on())
        # print(devices.data[topic[0]].is_online())


