import unittest
from DrawGraph import *

class DrawGraph_test(unittest.TestCase):
    def setUp(self):
        self.top = Tk()
    def test_no_value_less_than_zero(self):
        graph = DrawGraph(self.top,(100,45,23))
        self.assertEqual(graph.min_value, 0)

    def test_no_value_more_than_zero(self):
        graph = DrawGraph(self.top,(-10,-1,-102))
        self.assertEqual(graph.max_value,0)

    def test_min_value_found(self):
        graph = DrawGraph(self.top,(0, 15, -7))
        self.assertTrue(graph.min_value, -7)

    def test_max_value_found(self):
        graph = DrawGraph(self.top,(-1, 0, 4))
        self.assertEqual(graph.max_value, 4)

    def test_scale_above_and_including_zero(self):
        graph = DrawGraph(self.top,(0,5), 500, 500)
        self.assertEqual(graph.scale, 100)
        self.assertEqual(graph.x_axis, 500)

    def test_scale_above_and_excluding_zero(self):
        graph = DrawGraph(self.top,(10,5), 500, 500)
        self.assertEqual(graph.scale, 50)
        self.assertEqual(graph.x_axis, 500)

    def test_scale_above_and_below_zero(self):
        graph = DrawGraph(self.top,(-2,5), 70, 70)
        self.assertEqual(graph.scale, 10)
        self.assertEqual(graph.x_axis, 50)

    def test_scale_above_and_including_zero(self):
        graph = DrawGraph(self.top,(0,-75), 150, 150)
        self.assertEqual(graph.scale, 2)
        self.assertEqual(graph.x_axis, 0)

    def test_scale_above_and_excluding_zero(self):
        graph = DrawGraph(self.top,(-17,-5), 68, 68)
        self.assertEqual(graph.scale, 4)
        self.assertEqual(graph.x_axis, 0)

    
if __name__ == "__main__":
    unittest.main() 
