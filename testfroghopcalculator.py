import unittest
import froghopcalculator
fhcalc = froghopcalculator.FroghopCalculator()


class TestFroghopCalculator(unittest.TestCase):

    def test_getFinalXSubscript(self):
        self.assertEquals(8, fhcalc.getFinalXSubscript('_x_x___xx___'))
        self.assertEquals(8, fhcalc .getFinalXSubscript('_x_x___xx________________'))
        self.assertEquals(0, fhcalc.getFinalXSubscript('____________'))
        self.assertEquals(3, fhcalc.getFinalXSubscript('_x_x____'))
        self.assertEquals(16, fhcalc.getFinalXSubscript('xxxxxxxxxxxxxxxxx'))


    def test_getFinalPosition(self):
        self.assertEquals(0, fhcalc.getFinalPosition('_x'))
        self.assertEquals(0, fhcalc.getFinalPosition('_xx'))
        self.assertEquals(0, fhcalc.getFinalPosition('_xxxxxxxxx'))

        self.assertEquals(1, fhcalc.getFinalPosition('__x'))
        self.assertEquals(1, fhcalc.getFinalPosition('__xx'))
        self.assertEquals(1, fhcalc.getFinalPosition('__xxxxxxxxx'))

        self.assertEquals(8, fhcalc.getFinalPosition('_________x'))
        self.assertEquals(8, fhcalc.getFinalPosition('_________xx'))
        self.assertEquals(8, fhcalc.getFinalPosition('_________xxxxxxxxx'))




if __name__ == '__main__':
    unittest.main()

