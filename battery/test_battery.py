import unittest
from datetime import datetime

from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        # Test battery that should be serviced
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2020, 1, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.battery_should_be_serviced())
    
    def test_battery_should_be_not_serviced(self):
        # Test battery that should not be serviced
        current_date = datetime(2022, 1, 1)
        last_service_date = datetime(2020, 1, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.battery_should_be_serviced())

    def test_battery_sercived_within_last_year(self):
        # Test battery that was serviced within the last year
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2022, 1, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.battery_should_be_serviced())


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        # Test battery that should be serviced
        current_date = datetime(2024, 1, 1)
        last_service_date = datetime(2020, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.battery_should_be_serviced())

    def test_battery_should_be_not_serviced(self):
        # Test battery that should not be serviced
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2020, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.battery_should_be_serviced())

    def test_battery_sercived_within_last_year(self):
        # Test battery that was serviced within the last year
        current_date = datetime(2024, 1, 1)
        last_service_date = datetime(2023, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.battery_should_be_serviced())


if __name__ == '__main__':
    unittest.main()
