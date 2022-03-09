import unittest

from main import number_to_string


class Test(unittest.TestCase):

    def test_casual_case_1_func(self):
        self.assertEqual(number_to_string(1233123), 'один миллион двести тридцать три тысячи сто двадцать три')

    def test_casual_case_2_func(self):
        self.assertEqual(
            'Двадцать два миллиарда двести тридцать четыре миллиона сто двадцать четыре тысячи четыреста '
            'двенадцать'.strip().lower(), number_to_string(22234124412).strip().lower())

    def test_casual_case_3_func(self):
        self.assertEqual(
            'один'.strip().lower(), number_to_string(1).strip().lower())

    def test_casual_case_4_func(self):
        self.assertEqual(
            'два'.strip().lower(), number_to_string(2).strip().lower())

    def test_casual_case_5_func(self):
        self.assertEqual(
            'сто двадцать'.strip().lower(), number_to_string(120).strip().lower())

    def test_casual_case_6_func(self):
        self.assertEqual(
            'ноль'.strip().lower(), number_to_string(0).strip().lower())

    def test_casual_case_7_func(self):
        self.assertEqual(
            'сто двадцать три'.strip().lower(), number_to_string(123).strip().lower())

    def test_casual_case_8_func(self):
        self.assertEqual(
            'сто двадцать четыре тысячи'.strip().lower(), number_to_string(124000).strip().lower())

    def test_casual_case_9_func(self):
        self.assertEqual(
            'сто двадцать семь тысяч триста двадцать один'.strip().lower(), number_to_string(127321).strip().lower())

    def test_casual_case_10_func(self):
        self.assertEqual(
            'Двенадцать миллионов'.strip().lower(), number_to_string(12000000).strip().lower())
