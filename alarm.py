class Alarm:

    def __init__(self, sensor):
        self.temperature_low_threshold = 12
        self.temperature_high_threshold = 32
        self.sensor = sensor
        self.active = False

    def validate(self):
        temperature = self.sensor.take_measurement()
        if temperature < self.temperature_low_threshold:
            self.active = True
        elif temperature > self.temperature_high_threshold:
            self.active = True
        else:
            self.active = False