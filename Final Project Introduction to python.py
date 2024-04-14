import sys
import random

# Function to play the Tic-Tac-Toe game
def tic_tac_toe():
    # Insert the Tic-Tac-Toe game code here.
    def print_board(board):
        # This function prints the current state of the board.
        for row in board:
            # Join each cell in the row with " | " and print it.
            print(" | ".join(row))
            # Print a separator line between rows.
            print("-" * 5)
            
    def check_win(board, player):
        # This function checks if the given player has won the game.
        # Define all possible winning conditions for a 3x3 Tic-Tac-Toe board.
        win_conditions = [
            [board[0][0], board[0][1], board[0][2]],  # Horizontal top row
            [board[1][0], board[1][1], board[1][2]],  # Horizontal middle row
            [board[2][0], board[2][1], board[2][2]],  # Horizontal bottom row
            [board[0][0], board[1][0], board[2][0]],  # Vertical left column
            [board[0][1], board[1][1], board[2][1]],  # Vertical middle column
            [board[0][2], board[1][2], board[2][2]],  # Vertical right column
            [board[0][0], board[1][1], board[2][2]],  # Diagonal from top-left to bottom-right
            [board[2][0], board[1][1], board[0][2]]   # Diagonal from bottom-left to top-right
        ]
        # Check if any winning condition contains all positions taken by the same player.
        return [player, player, player] in win_conditions
    
    def get_free_positions(board):
        # This function returns a list of tuples indicating the free positions on the board.
        return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    
    def main():
        # This function orchestrates the game flow.
        # Initialize the game board as a 3x3 matrix filled with spaces, indicating free positions.
        board = [[" " for _ in range(3)] for _ in range(3)]
        # Set the initial player to 'X'.
        current_player = "X"
        while True:
            # Print the current board state.
            print_board(board)
            # Fetch all free positions available on the board.
            free_positions = get_free_positions(board)
            # Check if there are no free positions left and declare a tie if true.
            if not free_positions:
                print("It's a tie!")
                break
            
            # Prompt the current player to make a move.
            print(f"Player {current_player}, enter your move (row, column):")
            try:
                # Read and parse player input for row and column.
                row, col = map(int, input().split())
                # Validate if the chosen position is free.
                if (row, col) in free_positions:
                    # Make the move for the current player.
                    board[row][col] = current_player
                    # Check for a win after the move.
                    if check_win(board, current_player):
                        # Print the board and declare the current player as the winner.
                        print_board(board)
                        print(f"Player {current_player} wins!")
                        break
                    # Switch player turns.
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print("This position is already taken or invalid, choose another.")
            except ValueError:
                # Handle non-integer inputs gracefully.
                print("Invalid input. Please enter row and column numbers separated by a space.")
                
    if __name__ == "__main__":
        main()

# Function to play the Snake game
def snake_game():
    import pygame
    # Initialize pygame
    pygame.init()

    # Insert the Snake game code here.
    import pygame
    import random
    import sys
    
    # Initialize pygame
    pygame.init()
    
    # Constants for easy configuration
    CELL_SIZE = 20
    CELL_NUMBER = 20
    SCREEN_WIDTH = CELL_SIZE * CELL_NUMBER
    SCREEN_HEIGHT = CELL_SIZE * CELL_NUMBER
    FPS = 10
    
    # RGB color definitions
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    class SNAKE:
        def __init__(self):
            # Initialize the snake's starting position and size
            self.body = [pygame.Rect(5 * CELL_SIZE, 5 * CELL_SIZE, CELL_SIZE, CELL_SIZE)]
            self.direction = pygame.Vector2(0, 0)
            self.new_block = False
            
        def draw_snake(self):
            # Draw each block of the snake's body
            for block in self.body:
                pygame.draw.rect(screen, GREEN, block)
                
        def move_snake(self):
            # Move the snake in the current direction unless direction is zero
            if self.direction.magnitude() == 0:
                return  # Prevents the snake from moving if no direction is set
            # If not adding a new block, move the snake by adjusting body positions
            if not self.new_block:
                body_copy = self.body[:-1]
                body_copy.insert(0, self.body[0].copy().move(self.direction.x * CELL_SIZE, self.direction.y * CELL_SIZE))
                self.body = body_copy
            else:
                self.body.insert(0, self.body[0].copy().move(self.direction.x * CELL_SIZE, self.direction.y * CELL_SIZE))
                self.new_block = False
                
        def add_block(self):
            # Flag to add a new block to the snake's body
            self.new_block = True
            
    class FRUIT:
        def __init__(self):
            # Initialize and place fruit at a random position
            self.randomize()
            
        def draw_fruit(self):
            # Draw the fruit
            pygame.draw.rect(screen, RED, self.pos)
            
        def randomize(self):
            # Randomize fruit position within the grid
            self.x = random.randint(0, CELL_NUMBER - 1)
            self.y = random.randint(0, CELL_NUMBER - 1)
            self.pos = pygame.Rect(self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
    def check_collision(snake, fruit):
        # Check for collision between the snake head and the fruit
        if snake.body[0].colliderect(fruit.pos):
            fruit.randomize()  # Move the fruit
            snake.add_block()  # Grow the snake
            
    def check_fail(snake):
        # Check for collisions with the boundaries or itself
        if not 0 <= snake.body[0].x < SCREEN_WIDTH or not 0 <= snake.body[0].y < SCREEN_HEIGHT:
            return True  # Snake hits the wall
        for block in snake.body[1:]:
            if snake.body[0].colliderect(block):
                return True  # Snake hits itself
        return False
    
    def main():
        # Main game function
        snake = SNAKE()
        fruit = FRUIT()
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # Update direction based on key press ensuring opposite directions are not chosen
                    if event.key == pygame.K_UP and snake.direction.y != 1:
                        snake.direction = pygame.Vector2(0, -1)
                    elif event.key == pygame.K_DOWN and snake.direction.y != -1:
                        snake.direction = pygame.Vector2(0, 1)
                    elif event.key == pygame.K_LEFT and snake.direction.x != 1:
                        snake.direction = pygame.Vector2(-1, 0)
                    elif event.key == pygame.K_RIGHT and snake.direction.x != -1:
                        snake.direction = pygame.Vector2(1, 0)
                        
            screen.fill(BLACK)  # Clear screen
            snake.move_snake()  # Update snake position
            check_collision(snake, fruit)  # Check for collisions
            if check_fail(snake):  # Check if the game should end
                print("Game Over!")
                running = False
            snake.draw_snake()  # Render snake
            fruit.draw_fruit()  # Render fruit
            
            pygame.display.update()  # Update display
            clock.tick(FPS)  # Maintain the game speed
            
        pygame.quit()  # Quit pygame
        sys.exit()  # Exit the program
        
    if __name__ == "__main__":
        main()
        

    # Properly quit the pygame
    pygame.quit()

# Function to play the Rock, Paper, Scissors game
def rock_paper_scissors():
    # Insert the Rock, Paper, Scissors game code here.
    import random
    
    def get_computer_choice():
        # Function to randomly select the computer's choice from the options.
        options = ["rock", "paper", "scissors"]
        return random.choice(options)
    
    def get_user_choice():
        # Function to get the user's choice. Validates input to ensure it is correct.
        choice = input("Choose rock, paper, or scissors: ").lower()
        while choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            choice = input("Choose rock, paper, or scissors: ").lower()
        return choice
    
    def determine_winner(user_choice, computer_choice):
        # Function to determine the winner of the game based on choices.
        if user_choice == computer_choice:
            return "It's a tie!"
        # Winning conditions for the user.
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        # If none of the above conditions, the user loses.
        else:
            return "You lose!"
    
    def play_game():
        # Main game loop.
        while True:
            computer_choice = get_computer_choice()
            user_choice = get_user_choice()
            # Print choices to console.
            print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")
            # Print the result of the game.
            print(determine_winner(user_choice, computer_choice))
            
            # Ask if the user wants to play again.
            play_again = input("Play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing!")
                break
            
    if __name__ == "__main__":
        play_game()
        

def main_menu():
    while True:
        print("Game Menu:")
        print("1. Tic-Tac-Toe")
        print("2. Snake")
        print("3. Rock, Paper, Scissors")
        print("4. Exit")
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            tic_tac_toe()
        elif choice == '2':
            snake_game()
        elif choice == '3':
            rock_paper_scissors()
        elif choice == '4':
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main_menu()
    