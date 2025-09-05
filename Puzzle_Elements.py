# Importing the random module to generate random positions for the goal and exit points.
import random

# The DungeonCrawler class manages the game, including the grid, player, goal, and exit.
class DungeonCrawler:
    def __init__(self, grid_size=5):
        # Initialize the grid size and create a 2D grid filled with empty spaces.
        self.grid_size = grid_size
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        
        # Create a Player object starting at the top-left corner (0, 0).
        self.player = Player(0, 0)
        
        # Randomly generate positions for the goal and exit points.
        self.goal = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        self.exit = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        
        # Ensure the goal and exit points are not the same as the starting position or each other.
        while self.goal == (0, 0):
            self.goal = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        while self.exit == (0, 0) or self.exit == self.goal:
            self.exit = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        
        # Mark the goal and exit positions on the grid.
        self.grid[self.goal[0]][self.goal[1]] = 'G'
        self.grid[self.exit[0]][self.exit[1]] = 'E'

    #     # Initialize puzzles and generate them.
    #     self.puzzles = {}
    #     self.generate_puzzles()

    # # Generate puzzle elements and place them on the grid.
    # def generate_puzzles(self):
    #     puzzle_types = ['Lever', 'Door', 'Bridge']
    #     for puzzle_type in puzzle_types:
    #         while True:
    #             puzzle_position = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
    #             if puzzle_position not in [self.goal, self.exit, (0, 0)] and puzzle_position not in self.puzzles:
    #                 self.puzzles[puzzle_position] = puzzle_type
    #                 self.grid[puzzle_position[0]][puzzle_position[1]] = 'P'
    #                 break

    # Display the current state of the grid to the player.
    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print()

    # Main game loop where the player can input moves and interact with the game.
    def play(self):
        print("Welcome to the Dungeon Crawler!")
        print("Find the goal (G) and then reach the exit (E) to win.")
        self.display_grid()

        while True:
            # Prompt the player for a move and validate the input.
            move = input("Enter your move (up, down, left, right): ").strip().lower()
            if move in ['up', 'down', 'left', 'right']:
                # Move the player and check their new position.
                self.player.move(move, self.grid_size)
                self.check_position()
            # elif move == 'hint':
            #     # Provide a hint if the player requests it.
            #     self.provide_hint()
            else:
                print("Invalid move. Try again.")

    # Check the player's current position and determine if they reached the goal, exit, or a puzzle.
    def check_position(self):
        x, y = self.player.position
        if (x, y) == self.goal:
            # Notify the player when they reach the goal and clear the goal from the grid.
            print("You found the goal!")
            self.grid[x][y] = ' '
            self.goal = None  # Goal is cleared
        elif (x, y) == self.exit and self.goal is None:
            # Notify the player when they reach the exit after finding the goal.
            print("You reached the exit. You win!")
            exit()
        # elif (x, y) in self.puzzles:
        #     # Notify the player when they encounter a puzzle and solve it.
        #     puzzle = self.puzzles[(x, y)]
        #     print(f"You encountered a {puzzle} puzzle!")
        #     self.solve_puzzle(puzzle, (x, y))
        else:
            # Inform the player of their current position.
            print(f"Player is now at position ({x}, {y}).")
        self.display_grid()

    # # Solve the encountered puzzle based on its type.
    # def solve_puzzle(self, puzzle, position):
    #     if puzzle == 'Lever':
    #         print("You need to pull the lever to unlock a doorway.")
    #         action = input("Pull the lever? (yes/no): ").strip().lower()
    #         if action == 'yes':
    #             print("You pulled the lever. A doorway is now unlocked!")
    #             self.puzzles.pop(position)
    #             self.grid[position[0]][position[1]] = ' '
    #         else:
    #             print("You chose not to pull the lever.")
    #     elif puzzle == 'Door':
    #         print("The door is locked. Find the lever to unlock it.")
    #     elif puzzle == 'Bridge':
    #         print("The bridge is broken. Solve the puzzle to repair it.")
    #         action = input("Solve the bridge puzzle? (yes/no): ").strip().lower()
    #         if action == 'yes':
    #             print("You solved the puzzle and repaired the bridge!")
    #             self.puzzles.pop(position)
    #             self.grid[position[0]][position[1]] = ' '
    #         else:
    #             print("You chose not to solve the bridge puzzle.")

    # # Provide a hint for solving puzzles.
    # def provide_hint(self):
    #     if self.puzzles:
    #         hint_position, hint_puzzle = next(iter(self.puzzles.items()))
    #         print(f"Hint: There is a {hint_puzzle} puzzle at position {hint_position}.")
    #     else:
    #         print("No puzzles left to solve!")

# The Player class represents the player character and handles movement within the grid.
class Player:
    def __init__(self, x, y):
        # Initialize the player's starting position.
        self.position = (x, y)

    # Move the player in the specified direction, ensuring they stay within the grid boundaries.
    def move(self, direction, grid_size):
        x, y = self.position
        if direction == 'up' and x > 0:
            x -= 1
        elif direction == 'down' and x < grid_size - 1:
            x += 1
        elif direction == 'left' and y > 0:
            y -= 1
        elif direction == 'right' and y < grid_size - 1:
            y += 1
        else:
            # Notify the player if the move is invalid (off the grid).
            print("Invalid move. You can't move off the grid.")
            return
        # Update the player's position after a valid move.
        self.position = (x, y)

    # # Request a hint from the dungeon.
    # def request_hint(self, dungeon):
    #     dungeon.provide_hint()

