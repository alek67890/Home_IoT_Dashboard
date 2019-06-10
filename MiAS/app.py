from flask import Flask
from flask_mqtt import Mqtt
import models
from config import Configuration


mqtt = Mqtt()

app = Flask(__name__)
app.config.from_object(Configuration)
mqtt.init_app(app)




@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('POW1/stat/POWER')
    mqtt.subscribe('POW1/tele/LWT')
    mqtt.subscribe('POW1/tele/SENSOR')


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print('topic =')
    print(data['topic'])
    print('payload =')
    print(data['payload'])
