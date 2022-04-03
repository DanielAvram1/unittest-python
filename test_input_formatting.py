import unittest
from barbar import Solver, get_output
from text_formatting import *

class InputFormattingTestCase(unittest.TestCase):

  def test_wrong_R(self):
    with self.assertRaisesRegex(Exception, R_NU_E_INT):
      in_file = 'wrong_R_test.in'
      Solver(in_file)


  def test_wrong_C(self):
    with self.assertRaisesRegex(Exception, C_NU_E_INT):
      in_file = 'wrong_C_test.in'
      Solver(in_file)


  def test_R_too_small(self):
    with self.assertRaisesRegex(Exception, R_ESTE_MAI_MIC_CA_1):
      in_file = 'R_too_small.in'
      Solver(in_file)

  def test_C_too_small(self):
    with self.assertRaisesRegex(Exception, C_ESTE_MAI_MIC_CA_1):
      in_file = 'C_too_small.in'
      Solver(in_file)

  def test_R_too_big(self):
    with self.assertRaisesRegex(Exception, R_ESTE_MAI_MARE_CA_1000):
      in_file = 'R_too_big.in'
      Solver(in_file)

  def test_C_too_big(self):
    with self.assertRaisesRegex(Exception, C_ESTE_MAI_MARE_CA_1000):
      in_file = 'C_too_big.in'
      Solver(in_file)


  def test_wrong_no_of_chars(self):
    with self.assertRaisesRegex(Exception, linia_nu_are_caract('\d+', '\d+')):
      in_file = 'wrong_no_of_chars.in'
      Solver(in_file)

  
  def test_wrong_no_of_lines(self):
    with self.assertRaisesRegex(Exception, fis_nu_are_linii('\d+')):
      in_file = 'wrong_no_of_lines.in'
      Solver(in_file)

  def test_no_I(self):
    with self.assertRaisesRegex(Exception, NO_I):
      in_file = 'no_I.in'
      Solver(in_file)

  def test_no_O(self):
    with self.assertRaisesRegex(Exception, NO_O):
      in_file = 'no_O.in'
      Solver(in_file)

  def test_wrong_char(self):
    with self.assertRaisesRegex(Exception, caract_nu_e_permis("[^\n]")):
      in_file = 'wrong_char.in'
      Solver(in_file)

  def test_no_dragons(self):
    with self.assertRaisesRegex(Exception, NU_SUNT_DRAGONI):
      in_file = 'no_dragons.in'
      solver = Solver(in_file)
      solver.solve()
  
  def test_wrong_ok_file(self):
    with self.assertRaisesRegex(ValueError, nu_este_numar('not_a_number')):
      out_file = 'wrong_ok.ok'
      get_output(out_file)
      