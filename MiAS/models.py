class Device:
    def __init__(self, topic, name,  icon="zap"):
        self.topic = topic
        self.name = name
        self.icon = icon
        self.toggle = False
        self.online_status = False
        self.time = ''

    def on(self):
        self.toggle = True

    def off(self):
        self.toggle = False

    def is_on(self):
        return self.toggle

    def online(self):
        self.online_status = True

    def offline(self):
        self.online_status = False

    def is_online(self):
        return self.online_status


class DeviceSensor(Device):
    power = 0

    def new_power(self, power, time):
        self.power = power
        self.time = time

    def last_power(self):
        return self.power

    def last_time(self):
        return self.time


class DictDevice:
    data = {}

    def __init__(self, device=None):
        if device is not None:
            self.add(device)

    def add(self, device):
        if not self.check(device.topic):
            self.data[device.topic] = device
            return True
        else:
            return False

    def check(self, topic):
        return topic in self.data


