import unittest
from unittest.mock import Mock
from mazeHunter import BFS

class TestMzHntr(unittest.TestCase):       

    def testBFSSuccessfulSearch(self):
        self.new_dict = {}

        self.rows = 4
        self.columns = 4

        for i in range(self.rows):
            for j in range(self.columns):

                top = None
                bottom = None
                left = None
                right = None

                if i - 1 >= 0:
                    top = f"x{i-1}y{j}"
                if i + 1 < self.rows:
                    bottom = f"x{i+1}y{j}"
                if j - 1 >= 0:
                    left = f"x{i}y{j-1}"
                if j + 1 < self.columns:
                    right = f"x{i}y{j+1}"

                self.new_dict[f"x{i}y{j}"] = {"x" : i, "y" : j, "color" : "white", 
                                         "top": top, "bottom": bottom, "left": left, 
                                         "right": right }
        self.new_dict["x0y0"]["color"] = "green"
        self.new_dict["x3y3"]["color"] = "red"

        # pprint.pprint(self.new_dict)

        BFS(self.new_dict)
        


if __name__ == "__main__":
    unittest.main()