import unittest
from grid import create_grid, count_neighbors
from engine import update_grid

class TestGameOfLife(unittest.TestCase):
    
    def test_neighbor_counting_and_wrapping(self):
        # Create a tiny 3x3 grid with a single live cell at (0,0)
        grid = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        # Test direct neighbor count
        self.assertEqual(count_neighbors(grid, 1, 1), 1)
        
        # Test toroidal wrapping: cell at (0,2) wraps around to check (0,0)
        # Let's place a cell at (0,2) and check neighbors of (0,0)
        grid2 = [
            [0, 0, 1],
            [0, 0, 0],
            [1, 0, 0]
        ]
        # (0,0) should see (0,2) and (2,0) due to wrapping edges
        self.assertEqual(count_neighbors(grid2, 0, 0), 2)

    def test_conway_rules(self):
        # Rule: Live cell with 2 neighbors survives (3x3 block simulation)
        grid = [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        next_gen = update_grid(grid)
        # A 2x2 block is a stable still-life (Beehive/Block variant)
        self.assertEqual(next_gen[0][0], 1)
        self.assertEqual(next_gen[0][1], 1)

if __name__ == '__main__':
    unittest.main()