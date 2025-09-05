import unittest
from RandomizedGridGeneration import DungeonCrawler, Player

class TestDungeonCrawler(unittest.TestCase):
    def setUp(self):
        # Set up a small grid for testing
        self.game = DungeonCrawler(grid_size=3)
        self.game.goal = (1, 1)  # Set a fixed goal position
        self.game.exit = (2, 2)  # Set a fixed exit position
        self.game.grid[1][1] = 'G'
        self.game.grid[2][2] = 'E'
        self.game.player.position = (0, 0)  # Start player at (0, 0)

    def test_initial_position(self):
        # Test if the player starts at the correct position
        self.assertEqual(self.game.player.position, (0, 0))

    def test_move_within_bounds(self):
        # Test valid moves within the grid boundaries
        self.game.player.move('down', self.game.grid_size)
        self.assertEqual(self.game.player.position, (1, 0))
        self.game.player.move('right', self.game.grid_size)
        self.assertEqual(self.game.player.position, (1, 1))

    def test_move_out_of_bounds(self):
        # Test invalid moves that go out of bounds
        self.game.player.move('up', self.game.grid_size)
        self.assertEqual(self.game.player.position, (0, 0))  # Position should not change
        self.game.player.move('left', self.game.grid_size)
        self.assertEqual(self.game.player.position, (0, 0))  # Position should not change

    def test_reach_goal(self):
        # Test if the player is notified upon reaching the goal
        self.game.player.position = (1, 1)
        self.game.check_position()
        self.assertIsNone(self.game.goal)  # Goal should be cleared

    def test_reach_exit_without_goal(self):
        # Test if the player cannot win without reaching the goal first
        self.game.player.position = (2, 2)
        # Check that the game does not exit and the goal is still present
        self.game.check_position()
        self.assertIsNotNone(self.game.goal)  # Goal should still exist

    def test_reach_exit_after_goal(self):
        # Test if the player wins after reaching the goal and then the exit
        self.game.player.position = (1, 1)
        self.game.check_position()  # Clear the goal
        self.game.player.position = (2, 2)
        with self.assertRaises(SystemExit):
            self.game.check_position()  # Should exit the game

if __name__ == '__main__':
    unittest.main()
