import os


class Configuration(object):
    DEBUG = True
    ENV = 'development'

    MQTT_BROKER_URL = os.getenv('MQTT_BROKER_URL', 'localhost')
    MQTT_BROKER_PORT = int(os.getenv('MQTT_BROKER_PORT', '1883'))
    MQTT_USERNAME = os.getenv('MQTT_USERNAME', '')
    MQTT_PASSWORD = os.getenv('MQTT_PASSWORD', '')
    MQTT_KEEPALIVE = 5  # set the time interval for sending a ping to the broker to 5 seconds
    MQTT_TLS_ENABLED = False  # set TLS to disabled for testing purposes