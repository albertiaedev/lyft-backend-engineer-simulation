import unittest
from datetime import datetime

from carrigan_tire import CarriganTire
from octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        # Test that the tire should be serviced when the sum of wornArr is >= 0.9
        tire = CarriganTire([0.3, 0.4, 0.2])
        self.assertFalse(tire.tire_should_be_serviced())
        tire = CarriganTire([0.3, 0.4, 0.3])
        self.assertTrue(tire.tire_should_be_serviced())

        # Test that the tire should not be serviced when the sum of wornArr is < 0.9
        tire = CarriganTire([0.1, 0.2, 0.3])
        self.assertFalse(tire.tire_should_be_serviced())

        # Test that the tire should be serviced when the sum of wornArr is exactly 0.9
        tire = CarriganTire([0.3, 0.3, 0.3])
        self.assertFalse(tire.tire_should_be_serviced())


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        # Test that the tire should be serviced when the sum of wornArr is >= 3
        tire = OctoprimeTire([1, 1, 1])
        self.assertTrue(tire.tire_should_be_serviced())
        tire = OctoprimeTire([1, 1, 1, 1])
        self.assertTrue(tire.tire_should_be_serviced())

        # Test that the tire should not be serviced when the sum of wornArr is < 3
        tire = OctoprimeTire([1, 1])
        self.assertFalse(tire.tire_should_be_serviced())

        # Test that the tire should be serviced when the sum of wornArr is exactly 3
        tire = OctoprimeTire([1, 1, 1, 0])
        self.assertTrue(tire.tire_should_be_serviced())



if __name__ == '__main__':
    unittest.main()
