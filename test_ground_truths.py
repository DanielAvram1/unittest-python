import unittest
from barbar import Solver, get_output

class GroundTruthsTestCase(unittest.TestCase):
  
  def get_answer_and_ground_truth(self, index):
    file_name = 'grader_test'
    in_file = file_name + str(index) + '.in'
    out_file = file_name + str(index) + '.ok'
    solver = Solver(in_file)
    solver.solve()
    ground_truth = get_output(out_file)
    return (solver.answer, ground_truth)

  def test_1(self):
    ans, gt = self.get_answer_and_ground_truth(1)
    self.assertEqual(ans, gt)

  def test_2(self):
    ans, gt = self.get_answer_and_ground_truth(2)
    self.assertEqual(ans, gt)
  
  def test_3(self):
    ans, gt = self.get_answer_and_ground_truth(3)
    self.assertEqual(ans, gt)

  def test_4(self):
    ans, gt = self.get_answer_and_ground_truth(4)
    self.assertEqual(ans, gt)

  def test_5(self):
    ans, gt = self.get_answer_and_ground_truth(5)
    self.assertEqual(ans, gt)

  def test_6(self):
    ans, gt = self.get_answer_and_ground_truth(6)
    self.assertEqual(ans, gt)

  def test_7(self):
    ans, gt = self.get_answer_and_ground_truth(7)
    self.assertEqual(ans, gt)

  def test_8(self):
    ans, gt = self.get_answer_and_ground_truth(8)
    self.assertEqual(ans, gt)

  def test_9(self):
    ans, gt = self.get_answer_and_ground_truth(9)
    self.assertEqual(ans, gt)

  # def test_10(self):
  #   ans, gt = self.get_answer_and_ground_truth(10)
  #   self.assertEqual(ans, gt)
  
  def test_11(self):
    ans, gt = self.get_answer_and_ground_truth(11)
    self.assertEqual(ans, gt)

  def test_12(self):
    ans, gt = self.get_answer_and_ground_truth(12)
    self.assertEqual(ans, gt)

  def test_13(self):
    ans, gt = self.get_answer_and_ground_truth(13)
    self.assertEqual(ans, gt)

