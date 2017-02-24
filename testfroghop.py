import unittest
import froghop
f = froghop.Froghop()
class TestFroghop(unittest.TestCase):

    def test_definitions(self):
        self.assertTrue(True)
        f.getSolution('')

    def test_easy(self):
        self.assertEquals(-1, f.getSolution('1'))
        self.assertEquals(-1, f.getSolution('dfgbtea'))
        self.assertEquals(-1, f.getSolution('-'))
        self.assertEquals(-1, f.getSolution('='))
        self.assertEquals(-1, f.getSolution('@'))
        self.assertEquals(-1, f.getSolution('@&*^GV*^&B'))


    def test_basicsolutions(self):
        self.assertEquals('__',f.getSolution('__'))
        self.assertEquals('___',f.getSolution('___'))
        self.assertEquals('__________',f.getSolution('__________'))

        self.assertEquals('x__',f.getSolution('x'))
        self.assertEquals('xx__',f.getSolution('xx'))
        self.assertEquals('xxxxxxxxxxx__',f.getSolution('xxxxxxxxxxx'))





if __name__ == '__main__':
    unittest.main()

