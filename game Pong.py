# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle1_pos = [[0, HEIGHT/2], [PAD_WIDTH, HEIGHT/2], [PAD_WIDTH, HEIGHT/2 + PAD_HEIGHT], [0, HEIGHT/2 + PAD_HEIGHT]]
paddle2_pos = [[WIDTH - PAD_WIDTH, HEIGHT/2], [WIDTH, HEIGHT/2], [WIDTH, HEIGHT/2 + PAD_HEIGHT], [WIDTH - PAD_WIDTH, HEIGHT/2 + PAD_HEIGHT]]
paddle1_vel = [[0, 0], [0, 0], [0, 0], [0, 0]]
paddle2_vel = [[0, 0], [0, 0], [0, 0], [0, 0]]


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == LEFT:
        ball_vel = [-random.randrange(2, 4), - random.randrange(1, 3)]
    else:
        ball_vel = [random.randrange(2, 4), - random.randrange(1, 3)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect off of left hand side of canvas
    if (ball_pos[1] < BALL_RADIUS) or (ball_pos[1] >= (HEIGHT - BALL_RADIUS)):
        ball_vel[1] = - ball_vel[1]
    
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS) and (ball_pos[1] < paddle1_pos[1][1] or ball_pos[1] > paddle1_pos[2][1]):
        spawn_ball(RIGHT)    
    elif (ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH) and (ball_pos[1] < paddle2_pos[0][1] or ball_pos[1] > paddle2_pos[3][1]):
        spawn_ball(LEFT)
        
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS, 2, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[0][1] <= 0:
        paddle1_pos[0][1] += 1
        paddle1_pos[1][1] += 1
        paddle1_pos[2][1] += 1
        paddle1_pos[3][1] += 1        
    elif paddle1_pos[3][1] >= HEIGHT:
        paddle1_pos[0][1] -= 1
        paddle1_pos[1][1] -= 1
        paddle1_pos[2][1] -= 1
        paddle1_pos[3][1] -= 1
    else:
        paddle1_pos[0][1] += paddle1_vel[0][1]
        paddle1_pos[1][1] += paddle1_vel[1][1]
        paddle1_pos[2][1] += paddle1_vel[2][1]
        paddle1_pos[3][1] += paddle1_vel[3][1]
        
    if paddle2_pos[0][1] <= 0:
        paddle2_pos[0][1] += 1
        paddle2_pos[1][1] += 1
        paddle2_pos[2][1] += 1
        paddle2_pos[3][1] += 1        
    elif paddle2_pos[3][1] >= HEIGHT:
        paddle2_pos[0][1] -= 1
        paddle2_pos[1][1] -= 1
        paddle2_pos[2][1] -= 1
        paddle2_pos[3][1] -= 1
    else:
        paddle2_pos[0][1] += paddle2_vel[0][1]
        paddle2_pos[1][1] += paddle2_vel[1][1]
        paddle2_pos[2][1] += paddle2_vel[2][1]
        paddle2_pos[3][1] += paddle2_vel[3][1]

    # draw paddles
    canvas.draw_polygon(paddle1_pos, 1, 'White', 'White')
    canvas.draw_polygon(paddle2_pos, 1, 'White', 'White')
    
    # determine whether paddle and ball collide    
    if (ball_pos[0] <= paddle1_pos[1][0] + BALL_RADIUS) and ball_pos[1] >= paddle1_pos[1][1] and ball_pos[1] <= paddle1_pos[2][1]:
        ball_vel[0] = - ball_vel[0]
        
    if ball_pos[0] + BALL_RADIUS >= paddle2_pos[0][0] and ball_pos[1] >= paddle2_pos[0][1] and ball_pos[1] <= paddle2_pos[3][1]:
        ball_vel[0] = - ball_vel[0]  
        
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = [[0, -4], [0, -4], [0, -4], [0, -4]]
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = [[0, 4], [0, 4], [0, 4], [0, 4]] 
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = [[0, -4], [0, -4], [0, -4], [0, -4]]
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = [[0, 4], [0, 4], [0, 4], [0, 4]]       
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = [[0, 0], [0, 0], [0, 0], [0, 0]]
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = [[0, 0], [0, 0], [0, 0], [0, 0]] 
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = [[0, 0], [0, 0], [0, 0], [0, 0]]
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = [[0, 0], [0, 0], [0, 0], [0, 0]]

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
