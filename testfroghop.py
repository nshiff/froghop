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

    def test_capital_x_is_ok(self):
        self.assertEquals( f.getSolution('x'), f.getSolution('X'))
        self.assertEquals(f.getSolution('xx'), f.getSolution('XX'))
        self.assertEquals(f.getSolution('xxxxxxxxxxx'), f.getSolution('XXXXXXXXXXX'))

    def test_save_one_over_long_x_string(self):
        self.assertEquals('_x__', f.getSolution('_x'))
        self.assertEquals('_xx___', f.getSolution('_xx'))
        self.assertEquals('_xxxxxxxxx__________', f.getSolution('_xxxxxxxxx'))

    def test_save_two_over_long_x_string(self):
        self.assertEquals('__x__', f.getSolution('__x'))
        self.assertEquals('__xx___', f.getSolution('__xx'))
        self.assertEquals('__xxxxxxxxx__________', f.getSolution('__xxxxxxxxx'))

    def test_save_n_over_long_x_string(self):
        self.assertEquals('_________x__', f.getSolution('__x'))
        self.assertEquals('_________xx___', f.getSolution('__xx'))
        self.assertEquals('_________xxxxxxxxx__________', f.getSolution('__xxxxxxxxx'))

    def test_puzzlestatement(self):
        self.assertEquals('_xxx____', f.getSolution('_xxx'))

    def test_puzzlestatement2(self):
        self.assertEquals('_X_X___XX______', f.getSolution('_X_X___XX'))


if __name__ == '__main__':
    unittest.main()

