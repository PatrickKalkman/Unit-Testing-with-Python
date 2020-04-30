from unittest.mock import Mock
from alarm import Alarm
from sensor import Sensor

def test_alarm_reads_temperature_from_sensor():
    mock_sensor = Mock(Sensor)
    mock_sensor.take_measurement.return_value = 35
    alarm = Alarm(mock_sensor)
    alarm.validate()
    mock_sensor.take_measurement.assert_called()
    # assert alarm.active == True
