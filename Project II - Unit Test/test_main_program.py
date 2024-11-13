#Project II - Chasyl De Guzman

import unittest
from unittest.mock import patch
import main_program

class TestMainProgram(unittest.TestCase):
    
    #test_main_valid_input

    @patch('builtins.input', side_effect=['3', '85', '90', '95'])
    @patch('builtins.print')
    def test_main_valid_input(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('The class average is: 90.00')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )
    
    #test_invalid_number_of_students

    @patch('builtins.input', side_effect=['0', '3', '85', '90', '95'])
    @patch('builtins.print')
    def test_invalid_number_of_students(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('The class average is: 90.00')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )

    #test_invalid_grades

    @patch('builtins.input', side_effect=['3', '105', '-5', '85', '90', '95'])
    @patch('builtins.print')
    def test_invalid_grades(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('The class average is: 90.00')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )

    #test_non_numeric_input_for_grades

    @patch('builtins.input', side_effect=['3', 'abc', '85', 'abc', '90', 'abc', '95'])
    @patch('builtins.print')
    def test_non_numeric_input_for_grades(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('The class average is: 90.00')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )

    #test_non_numeric_input_for_number_of_students

    @patch('builtins.input', side_effect=['abc', '3', '85', '90', '95'])
    @patch('builtins.print')
    def test_non_numeric_input_for_number_of_students(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('The class average is: 90.00')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )
    
    #test_single_student

    @patch('builtins.input', side_effect=['1', '85'])
    @patch('builtins.print')
    def test_single_student(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('The class average is: 85.00')
        self.assertIn(
            unittest.mock.call('The class average is: 85.00'), 
            mock_print.mock_calls
        )
    


if __name__ == '__main__':
    unittest.main()

    
