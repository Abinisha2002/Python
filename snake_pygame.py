'''pythongame'''
# import pygame
# pygame.init()
# white = (255, 255, 255)
# # assigning values to height and width variable
# height = 400
# width = 400
# # creating the display surface object
# # of specific dimension..e(X, Y).
# display_surface = pygame.display.set_mode((height, width))

# # set the pygame window name
# pygame.display.set_caption('Image')

# # creating a surface object, image is drawn on it.
# image = pygame.image.load(r'img1.jpg')

# # infinite loop
# while True:
#     display_surface.fill(white)
#     display_surface.blit(image, (0, 0))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             # quit the program.
#             quit()
#         # Draws the surface object to the screen.
#         pygame.display.update()
       
import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by OpenAI')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            our_snake(snake_block, snake_List)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop() 
 

'''#test
#battle ships
import pygame

# Initialize pygame
pygame.init()

# Set up the screen
Black = (0,0,0)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))

#Load The images
imp = pygame.image.load("img1.jpg")
imp = pygame.transform.scale(imp, (100,100))
imp2 = pygame.image.load("img2.jpg")
imp2 = pygame.transform.scale(imp2, (100,100))

#initilize the font
font = pygame.font.SysFont("Arial", 32)

def RedrawGameWindow():

  screen.fill((255, 255, 255))
  
  global G00
  global G01
  global G02
  global G10
  global G11
  global G12
  global G20
  global G21
  global G22
  
  G00 =pygame.draw.rect(screen, Black, (250, 150, 100, 100), 1)

  G01 = pygame.draw.rect(screen, Black, (350, 150, 100, 100), 1)

  G02 = pygame.draw.rect(screen, Black, (450, 150, 100, 100), 1)  

  G10 = pygame.draw.rect(screen, Black, (250, 250, 100, 100), 1)
    
  G11 = pygame.draw.rect(screen, Black, (350, 250, 100, 100), 1)

  G12 =pygame.draw.rect(screen, Black, (450, 250, 100, 100), 1)

  G20 =pygame.draw.rect(screen, Black, (250, 350, 100, 100), 1)

  G21 = pygame.draw.rect(screen, Black, (350, 350, 100, 100), 1)

  G22 = pygame.draw.rect(screen, Black, (450, 350, 100, 100), 1)

  grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
  
  pygame.display.flip()

def displayGrid(grid):
  print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
  print("-----------")
  print(" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
  print("-----------")
  print(" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])

def checkGridX(grid):
  global RowMsg
  #Checks The Rows
  
  if grid[0][0]=="X" and grid[0][1]=="X" and grid[0][2]=="X":
    RowMsg = "Three Xs in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print(RowMsg)
    #winner = True
      
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
      
  if grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]=="X":
    RowMsg = "Three Xs in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print(RowMsg)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]=="X":
    RowMsg = "Three Xs in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a row.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  #Checks The Collums

  if grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]=="X":
    RowMsg = "Three Xs in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a Collum.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[0][1]=="X" and grid[1][1]=="X" and grid[2][1]=="X":
    RowMsg = "Three Xs in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a Collum.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[0][2]=="X" and grid[1][2]=="X" and grid[2][2]=="X":
    RowMsg = "Three Xs in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a Collum.")
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  #Checks Diagonals

  if grid[2][0]=="X" and grid[1][1]=="X" and grid[0][2]=="X":
    RowMsg = "Three Xs in a Diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a Diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]=="X":
    RowMsg = "Three Xs in a Diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

def checkGrid0(grid):
  
  if grid[0][0]=="O" and grid[0][1]=="O" and grid[0][2]=="O":
    RowMsg = "Three 0s in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a row.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[1][0]=="O" and grid[1][1]=="O" and grid[1][2]=="O":
    RowMsg = "Three 0s in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a row.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[2][0]=="O" and grid[2][1]=="O" and grid[2][2]=="O":
    RowMsg = "Three 0s in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a row.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  #Checks The Collums

  if grid[0][0]=="O" and grid[1][0]=="O" and grid[2][0]=="O":
    RowMsg = "Three 0s in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a Collum.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[0][1]=="O" and grid[1][1]=="O" and grid[2][1]=="O":
    RowMsg = "Three 0s in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a Collum.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[0][2]=="O" and grid[1][2]=="O" and grid[2][2]=="O":
    RowMsg = "Three 0s in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a Collum.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  #Checks Diagonals

  if grid[2][0]=="O" and grid[1][1]=="O" and grid[0][2]=="O":
    RowMsg = "Three 0s in a diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Os in a Diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[0][0]=="O" and grid[1][1]=="O" and grid[2][2]=="O":
    RowMsg = "Three 0s in a diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Os in a diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

#Intializing More varibles
grid = [[" "," "," "],[" "," "," "],[" "," "," "]] #creates the Consle Reperezentaio of the Grid
Turn = True # Deterumins wether its X or Os turn
#winner = False

#Creates the Grid In Pygame


displayGrid(grid)
RedrawGameWindow()
# Set up the game loop
running = True
while running:
    # Handle events
  
    for event in pygame.event.get():
      
      #Mouse Detection
      #Checks For mouse clicking within each aquare
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
          RedrawGameWindow()
          grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
          Turn = True

      if event.type == pygame.MOUSEBUTTONDOWN:
          
          if G00.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 0
            col = 0
            if "X" in grid[0][0] or "O" in grid[0][0]: # Checks wether the grid is empty
              print("stop")
            else:
              if Turn == True:
                grid[row][col] = "X"
                Turn = False
                screen.blit(imp, (250,150))
              else:
                screen.blit(imp2, (250, 150))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              
              
            
              displayGrid(grid)
            
              pygame.display.flip()
              checkGridX(grid)
          if G01.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 0
            col = 1
            if "X" in grid[0][1] or "O" in grid[0][1]:
              print("Stop")
            else:
              if Turn == True:
                grid[row][col] = "X"
                Turn = False
                screen.blit(imp, (350,150))
              else:
                screen.blit(imp2, (350,150))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)

              pygame.display.flip()
              checkGridX(grid)
              
          if G02.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 0
            col = 2
            if "X" in grid[0][2] or "O" in grid[0][2]:
              print("Stop")
            else:
              if Turn == True:
                grid[row][col] = "X"
                Turn = False
                screen.blit(imp, (450,150))
              else:
                screen.blit(imp2, (450,150))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
                displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)
          if G10.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 1
            col = 0
            if "X" in grid[1][0] or "O" in grid[1][0]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (250,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (250,250))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
            
              pygame.display.flip()
              checkGridX(grid)
          if G11.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 1
            col = 1
            if "X" in grid[1][1] or "O" in grid[1][1]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (350,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (350,250))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
            
              pygame.display.flip()
              checkGridX(grid)
          if G12.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 1
            col = 2
            if "X" in grid[1][2] or "O" in grid[1][2]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (450,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (450,250))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)
          if G20.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 2
            col = 0
            if "X" in grid[2][0] or "O" in grid[2][0]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (250,350))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (250,350))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)
          if G21.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 2
            col = 1
            if "X" in grid[2][1] or "O" in grid[2][1]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (350,350))
                grid[row][col] = "X"
                Turn = False
                
              else:
                screen.blit(imp2, (350,350))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)
          if G22.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 2
            col = 2
            if "X" in grid[2][2] or "O" in grid[2][2]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (450,350))
                grid[row][col] = "X"
                Turn = False
                checkGridX(grid)
              else:
                screen.blit(imp2, (450,350))
                
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
                
              displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)

      if event.type == pygame.QUIT: #Checks whether you pressed the X button
        running = False
    
    text = font.render("Tic Tac toe ", True, (0, 0, 0))  # Render the text
    text_rect = text.get_rect(center=(screen_width/2, 100))  # Get the rectangle for the text
    
    #text2 = font.render(RowMsg, True, (0, 0, 0))  # Render the text
    text_rect2 = text.get_rect(center=(350, 500))
    
    screen.blit(text, text_rect)
    pygame.display.flip()  # Update the screen

  
# Quit pygame
pygame.quit()  '''



# importing libraries
import pygame
import time
import random

snake_speed = 15

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
			[90, 50],
			[80, 50],
			[70, 50]
			]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
				random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):

	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object 
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# create a rectangular object for the text
	# surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	game_window.blit(score_surface, score_rect)

# game over function
def game_over():

	# creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	# creating a text surface on which text 
	# will be drawn
	game_over_surface = my_font.render(
		'Your Score is : ' + str(score), True, red)
	
	# create a rectangular object for the text 
	# surface object
	game_over_rect = game_over_surface.get_rect()
	
	# setting position of the text
	game_over_rect.midtop = (window_x/2, window_y/4)
	
	# blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()


# Main Function
while True:
	
	# handling key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'

	# If two keys pressed simultaneously
	# we don't want snake to move into two 
	# directions simultaneously
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	# Snake body growing mechanism
	# if fruits and snakes collide then scores
	# will be incremented by 10
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 10
		fruit_spawn = False
	else:
		snake_body.pop()
		
	if not fruit_spawn:
		fruit_position = [random.randrange(1, (window_x//10)) * 10, 
						random.randrange(1, (window_y//10)) * 10]
		
	fruit_spawn = True
	game_window.fill(black)
	
	for pos in snake_body:
		pygame.draw.rect(game_window, green,
						pygame.Rect(pos[0], pos[1], 10, 10))
	pygame.draw.rect(game_window, white, pygame.Rect(
		fruit_position[0], fruit_position[1], 10, 10))

	# Game Over conditions
	if snake_position[0] < 0 or snake_position[0] > window_x-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > window_y-10:
		game_over()

	# Touching the snake body
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	# displaying score continuously
	show_score(1, white, 'times new roman', 20)

	# Refresh game screen
	pygame.display.update()

	# Frame Per Second /Refresh Rate
	fps.tick(snake_speed)