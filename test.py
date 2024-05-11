import unittest
from path_reducer_an.path_reducer import PathReducer


class TestPathReducer(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path_reducer = PathReducer()

    def test_case_1(self):
        self.assertEqual(self.path_reducer.reduce_path(["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","WEST"]), ["WEST"])

    def test_case_2(self):
        self.assertEqual(self.path_reducer.reduce_path(["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"]), [])

    def test_case_3(self):
        self.assertEqual(self.path_reducer.reduce_path(["NORTH","WEST","SOUTH","EAST"]), ["NORTH","WEST","SOUTH","EAST"])

    def test_case_4(self):
        self.assertEqual(self.path_reducer.reduce_path(["NORTH","SOUTH","EAST","WEST"]), [])


if __name__ == '__main__':
    unittest.main()