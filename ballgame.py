# SINGLE BALL RUNNING GAME
# import pygame
# import random

# # Define some colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# color=[0,0,0]
# SCREEN_WIDTH = 500
# SCREEN_HEIGHT = 500
# BALL_SIZE = 20

# # Define the starting color and the increment for each new ball
# START_COLOR = (0, 0, 0)


# class Ball:
#     """
#     Class to keep track of a ball's location, vector, and color.
#     """
#     def __init__(self,c):
#         self.x = 0
#         self.y = 0
#         self.change_x = 0
#         self.change_y = 0
#         self.color=c
        

            

# def make_ball(ball_list,c):
#     """
#     Function to make a new ball with a color.
#     """
#     # Calculate the color for the new ball based on the current number of balls
#     num_balls = len(ball_list)
#     """ color = tuple(min(255, START_COLOR[i] + num_balls * COLOR_INCREMENT[i]) for i in range(3))
#     print(color) """
#     ball = Ball(c)
#     # Starting position of the ball.
#     # Take into account the ball size so we don't spawn on the edge.
#     ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
#     ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

#     # Speed and direction of rectangle
#     ball.change_x = 5
#     ball.change_y = 5

#     return ball

# def main():
#     """
#     This is our main program.
#     """
#     pygame.init()

#     # Set the height and width of the screen
#     size = [SCREEN_WIDTH, SCREEN_HEIGHT]
#     screen = pygame.display.set_mode(size)

#     pygame.display.set_caption("Bouncing Balls")

#     # Loop until the user clicks the close button.
#     done = False

#     # Used to manage how fast the screen updates
#     clock = pygame.time.Clock()

#     ball_list = []

#     # Create the initial ball
#     ball = make_ball(ball_list,color)
#     ball_list.append(ball)

#     # -------- Main Program Loop -----------
#     while not done:
#         # --- Event Processing
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True
#             elif event.type == pygame.KEYDOWN:
#                 if color[0]<245:
#                     color[0]+=10
#                 elif color[2]<245:
#                     color[2]+=10
#                 elif color[1]<245:
#                     color[1]+=10
#                 else:
#                     color[0]=0
#                     color[1]=0
#                     color[2]=0
#                 if event.key == pygame.K_SPACE:
#                     ball = make_ball(ball_list,color)
#                     ball_list.append(ball)

#         # --- Logic
#         for ball in ball_list:
#             # Move the ball's center
#             ball.x += ball.change_x
#             ball.y += ball.change_y

#             # Bounce the ball if needed
#             if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
#                 ball.change_y *= -1
#             if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
#                 ball.change_x *= -1

#         # --- Drawing
#         # Set the screen background
#         screen.fill(WHITE)

        



#         # Draw the balls with their respective colors
#         for ball in ball_list:
          
#             pygame.draw.circle(screen, color, [ball.x, ball.y], BALL_SIZE)

#         # --- Wrap-up
#         # Limit to 60 frames per second
#         clock.tick(200)

#         # Go ahead and update the screen with what we've drawn.
#         pygame.display.flip()

#     # Close everything down
#     pygame.quit()

# if __name__ == "__main__":
#     main()









# # MULTIPLE BALLS
# import pygame
# # initialize pygame
# pygame.init()

# # define width of screen
# width = 1000
# # define height of screen
# height = 600
# screen_res = (width, height)

# pygame.display.set_caption("GRS Bouncing game")
# screen = pygame.display.set_mode(screen_res)

# # define colors
# red = (255, 0, 0)
# green=(0,255,0)
# blue=(0,0,255)
# redgreen=(255,255,0)
# redblue=(255,0,255)
# black = (255,255,255)

# # define ball
# ball_obj = pygame.draw.circle(surface=screen, color=red, center=[100, 100], radius=20) 
# ball_obj1= pygame.draw.circle(surface=screen, color=blue, center=[100,100],radius=20)
# ball_obj2= pygame.draw.circle(surface=screen, color=green, center=[100,100],radius=20)
# ball_obj3= pygame.draw.circle(surface=screen, color=redgreen, center=[100,100],radius=20)
# ball_obj4= pygame.draw.circle(surface=screen, color=redblue, center=[100,100],radius=20)
# # define speed of ball
# # speed = [X direction speed, Y direction speed]
# speed = [1, 1] 
# speed1 = [2, 2]
# speed2= [3,3]
# speed3=[4,4]
# speed4=[5,5]

# # game loop
# while True:
# 	# event loop
# 	for event in pygame.event.get():
# 		# check if a user wants to exit the game or not
# 		if event.type == pygame.QUIT:
# 			exit()

# 	# fill black color on screen
# 	screen.fill(black)

# 	# move the ball
# 	# Let center of the ball is (100,100) and the speed is (1,1)
# 	ball_obj = ball_obj.move(speed) 
# 	ball_obj1=ball_obj1.move(speed1)
# 	ball_obj2=ball_obj2.move(speed2)
# 	ball_obj3=ball_obj3.move(speed3)
# 	ball_obj4=ball_obj4.move(speed4)
# 	# Now center of the ball is (101,101)
# 	# In this way our wall will move

# 	# if ball goes out of screen then change direction of movement
# 	if ball_obj.left <= 0 or ball_obj.right >= width:
# 		speed[0] = -speed[0]
# 	if ball_obj.top <= 0 or ball_obj.bottom >= height:
# 		speed[1] = -speed[1]
		
# 	if ball_obj1.left <= 0 or ball_obj1.right >= width:
# 		speed1[0] =- speed1[0]
# 	if ball_obj1.top <= 0 or ball_obj1.bottom >= height:
# 		speed1[1] =- speed1[1] 
		

# 	if ball_obj2.left <= 0 or ball_obj2.right >= width:
# 		speed2[0] =- speed2[0]
# 	if ball_obj2.top <= 0 or ball_obj2.bottom >= height:
# 		speed2[1] =- speed2[1] 
	
# 	if ball_obj3.left <= 0 or ball_obj3.right >= width:
# 		speed3[0] =- speed3[0]
# 	if ball_obj3.top <= 0 or ball_obj3.bottom >= height:
# 		speed3[1] =- speed3[1] 
		
# 	if ball_obj4.left <= 0 or ball_obj4.right >= width:
# 		speed4[0] =- speed4[0]
# 	if ball_obj4.top <= 0 or ball_obj4.bottom >= height:
# 		speed4[1] =- speed4[1] 
		
    


# 	# draw ball at new centers that are obtained after moving ball_obj
# 	pygame.draw.circle(surface=screen, color=red,center=ball_obj.center, radius=30)
# 	pygame.draw.circle(surface=screen,color=blue,center=ball_obj1.center,radius=30)
# 	pygame.draw.circle(surface=screen,color=green,center=ball_obj2.center,radius=30)
# 	pygame.draw.circle(surface=screen,color=redgreen,center=ball_obj3.center,radius=30)
# 	pygame.draw.circle(surface=screen,color=redblue,center=ball_obj4.center,radius=30)
	
	



# 	# update screen
# 	pygame.display.flip()


'''JUMPING BALL'''
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Jumping Ball")

# Set up colors  
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the ball
ball_radius = 20
ball_x = window_width // 2
ball_y = window_height - ball_radius
ball_dy = 0
gravity = 0.5
jump_strength = -10
on_ground = True

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                ball_dy = jump_strength
                on_ground = False

    # Update ball position
    ball_y += ball_dy
    ball_dy += gravity

    # Check for collision with ground
    if ball_y >= window_height - ball_radius:
        ball_y = window_height - ball_radius
        ball_dy = 0
        on_ground = True

    # Fill the window with white color
    window.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(window, BLUE, (ball_x, int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()  
