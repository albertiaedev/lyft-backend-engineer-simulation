import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        # Test engine that should be serviced
        engine = CapuletEngine(61000, 30000)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_be_serviced(self):
        # Test engine that should not be serviced
        engine = CapuletEngine(59000, 30000)
        self.assertFalse(engine.engine_should_be_serviced())

    def test_engine_serviced_within_last_30000_miles(self):
        # Test engine that was serviced within the last 30,000 miles
        engine = CapuletEngine(60000, 50000)
        self.assertFalse(engine.engine_should_be_serviced())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        # Test engine with warning light on
        engine_with_warning_light = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine_with_warning_light.engine_should_be_serviced())

        # Test engine with warning light off
        engine_without_warning_light = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine_without_warning_light.engine_should_be_serviced())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        # Test engine that should be serviced
        engine_that_should_be_serviced = WilloughbyEngine(120000, 60000)
        self.assertTrue(engine_that_should_be_serviced.engine_should_be_serviced())

    def test_engine_should_be_serviced(self):
        # Test engine that should not be serviced
        engine_that_should_not_be_serviced = WilloughbyEngine(110000, 60000)
        self.assertFalse(engine_that_should_not_be_serviced.engine_should_be_serviced())
    
    def test_engine_serviced_within_last_30000_miles(self):
        # Test engine that was serviced within the last 60,000 miles
        engine_that_was_serviced_recently = WilloughbyEngine(100000, 90000)
        self.assertFalse(engine_that_was_serviced_recently.engine_should_be_serviced())


if __name__ == '__main__':
    unittest.main()