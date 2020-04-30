from unittest.mock import Mock
from alarm import Alarm
from sensor import Sensor


def test_high_temperature_activates_alarm():
    stub_sensor = Mock(Sensor)
    stub_sensor.take_measurement.return_value = 35
    alarm = Alarm(stub_sensor)
    alarm.validate()
    assert alarm.active == True
