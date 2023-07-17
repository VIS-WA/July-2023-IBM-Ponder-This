import pygame
import copy

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Set up the screen dimensions
screen_width = 500
screen_height = 500
block_size = 100
n = 5  # Size of the grid
steps = 0
global cost
cost = 0
grid = [[0 for _ in range(n)] for _ in range(n)]

def reset_grid(grid):
    n = len(grid)
    # Create the game grid
    grid[1][0] = 4
    grid[2][0] = 4
    grid[3][0] = 1
    grid[4][0] = 1
    grid[0][1] = 2
    grid[1][1] = 2
    grid[0][2] = 2
    grid[0][3] = 3
    grid[1][3] = 3
    grid[1][2] = 3
    grid[1][4] = 8
    grid[2][4] = 8
    grid[2][3] = 8	
    grid[2][2] = 8	
    grid[3][4] = 5
    grid[3][3] = 6
    grid[4][4] = 9
    grid[4][3] = 9
    grid[4][2] = 7
    grid[4][1] = 7
	
    '''
    grid[0][0] = 1
    grid[1][0] = 1
    grid[0][1] = 2
    grid[1][1] = 2
    grid[0][2] = 2
    grid[0][3] = 3
    grid[1][3] = 3
    grid[1][2] = 3
    grid[0][4] = 4
    grid[1][4] = 4
    grid[2][0] = 5
    grid[2][1] = 6
    grid[2][2] = 7
    grid[2][3] = 7
    grid[2][4] = 8
    grid[3][4] = 8
    grid[3][3] = 8
    grid[3][2] = 8
    grid[3][1] = 9
    grid[3][0] = 9
'''	

# grid

reset_grid(grid)
# Block color mapping
block_colors = {
    1: ORANGE,
    2: GREEN,
    3: RED,
    4: ORANGE,
    5: BLUE,
    6: BLUE,
    7: YELLOW,
    8: PURPLE,
    9: YELLOW,
}

# Block size mapping
block_sizes = {
    1: 2,
    2: 3,
    3: 3,
    4: 2,
    5: 1,
    6: 1,
    7: 2,
    8: 4,
    9: 2,
}   



def draw_grid():
    screen.fill(WHITE)
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                pygame.draw.rect(
                    screen,
                    block_colors[grid[i][j]],
                    (j * block_size, i * block_size, block_size, block_size),
                )




def move_block(row, col, dx, dy):
    block_num = grid[row][col]
    global cost, selected_block

    # Find the entire block
    block_squares = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == block_num:
                block_squares.append((i, j))


    # Move the block
    new_block_squares = []
    for square in block_squares:
        new_row = square[0] + dx
        new_col = square[1] + dy

        if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
            return 0

        if grid[new_row][new_col] != 0 and grid[new_row][new_col] != block_num:
            return 0

        new_block_squares.append((new_row, new_col))

    for square in block_squares:
        grid[square[0]][square[1]] = 0

    for square in new_block_squares:
        grid[square[0]][square[1]] = block_num
    
    cost += 5 - block_sizes[block_num]
    # update selected block
    selected_block[0] += dx
    selected_block[1] += dy
    
    return 1


def reset_game():
    global steps, grid, cost
    steps = 0
    cost = 0
    grid = [[0 for _ in range(n)] for _ in range(n)]
    reset_grid(grid)


def undo_move(history,historys):
    global steps, grid, cost
    if len(history) > 1:
        steps -= 1
        grid = copy.deepcopy(history[-2])
        history.pop()
        number,_ = historys[-1]
        historys.pop()
        cost -= 5 - block_sizes[number]
        # print the number of squares in a block that is moved
        

        # historys.pop()



def print_history(historys):
    print("Move history:")
    for step, state in enumerate(historys):
        # print(f"Step {step + 1}")
        for row in state:
            print(row)

steps = 0
cost = 0

# Initialize Pygame
pygame.init()

# Initialize the Pygame window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block Moving Game")

# Initialize the clock
clock = pygame.time.Clock()

global selected_block
# Main game loop
def game_loop():
    global steps, selected_block
    history = []
    historys = []
    selected_block = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # print(selected_block)

                if event.key == pygame.K_UP:
                    if selected_block:
                        if move_block(selected_block[0], selected_block[1], -1, 0):
                            steps += 1
                            historys.append((block,"up"))
                            history.append(copy.deepcopy(grid))

                if event.key == pygame.K_DOWN:
                    if selected_block:
                        if move_block(selected_block[0], selected_block[1], 1, 0):
                            steps += 1
                            historys.append((block,"down"))
                            history.append(copy.deepcopy(grid))


                if event.key == pygame.K_LEFT:
                    if selected_block:
                        if move_block(selected_block[0], selected_block[1], 0, -1):
                            steps += 1
                            historys.append((block,"left"))
                            history.append(copy.deepcopy(grid))


                if event.key == pygame.K_RIGHT:
                    if selected_block:
                        if move_block(selected_block[0], selected_block[1], 0, 1):
                            steps += 1
                            historys.append((block,"right"))
                            history.append(copy.deepcopy(grid))


                if event.key == pygame.K_r:
                    reset_game()
                    historys = []
                    history = [copy.deepcopy(grid)]

                if event.key == pygame.K_u:
                    undo_move(history,historys)

                if event.key == pygame.K_p:
                    print_history(historys)
                
                if event.key == pygame.K_q:
                    running = False
                    # quit the window

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // block_size
                col = x // block_size
                block = grid[row][col]
                if block != 0:
                    selected_block = [row, col]

        draw_grid()

 

        # Display the number of steps
        font = pygame.font.Font(None, 20)
        text = font.render("Steps: " + str(steps), True, BLACK)
        screen.blit(text, (10, screen_height - 20))

        text = font.render("Cost: " + str(cost), True, BLACK)
        screen.blit(text, (10, screen_height - 40))
        
        # Display the options to reset, undo, and quit
        text = font.render("Press R to reset", True, BLACK)
        screen.blit(text, (10, screen_height - 60))
        text = font.render("Press U to undo", True, BLACK)
        screen.blit(text, (10, screen_height - 80))
        text = font.render("Press Q to quit", True, BLACK)
        screen.blit(text, (10, screen_height - 100))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# Run the game
game_loop()
