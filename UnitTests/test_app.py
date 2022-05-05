from unittest import TestCase, result
from AutomaticCalculationsRecognition import *


class AppTest(TestCase):
    def test_img2string(self):
        # Given 
        img = "images/1+1.png"
        expected_result = "1+1"
        # When
        result = img2string(img)
        # Then
        self.assertEqual(expected_result, result)
        
    def test_string2op(self):
        # Given 
        op_string = "4+6"
        expected_result = 10
        # When
        result = string2op(op_string)
        # Then
        self.assertEqual(expected_result, result)

    def test_string2op_zero(self):
        # Given 
        op_string = "15/0"
        # When

        # Then
        self.assertRaises(ZeroDivisionError, string2op, op_string)


    def test_calculus(self):
        # Given 
        img = "images/1+1.png"
        expected_result = 2
        # When
        result = calculus(img)
        # Then
        self.assertEqual(expected_result, result)


