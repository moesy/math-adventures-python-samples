from introduction.function_eval import f, g, h
import unittest


class TestFunctionEval(unittest.TestCase):

    def test_f_x(self):
        self.assertEqual(f(0), 2.732050807568877)
        self.assertEqual(f(0.44),  2.4147236990991408)

    def test_g_t(self):
        self.assertEqual(g(0), -1)

    def test_h_t(self):
        # divide by zero = None
        self.assertEqual(h(0), None)


if __name__ == '__main__':
    unittest.main()
