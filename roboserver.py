#!/usr/bin/python
import pygame, socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("", 5660))
serversocket.listen(1)

conn, addr = serversocket.accept()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [640, 480]
screen = pygame.display.set_mode(size)
 
global done
done = False

pygame.display.set_caption("Robo Kal")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

 
# Initialize the joysticks
pygame.joystick.init()
 
# Get ready to print

# -------- Main Program Loop -----------
joynum = 0
joystick_count = pygame.joystick.get_count()
if joystick_count > 0:
	joystick = pygame.joystick.Joystick(joynum)
	joystick.init()
x_key = float(0)
y_key = float(0)
x_joy = float(0)
y_joy = float(0)
while not done:
	Ox_key = x_key
	Oy_key = y_key
	Ox_joy = x_joy
	Oy_joy = y_joy
	x_key = float(0)
	y_key = float(0)
	x_joy = float(0)
	y_joy = float(0)
	# EVENT PROCESSING STEP
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			global done
			done = True
 
		# PPossible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN
		# JOYBUTTONUP JOYHATMOTION
		if event.type == pygame.JOYBUTTONDOWN:
			print("Joystick button pressed.")
		if event.type == pygame.JOYBUTTONUP:
			print("Joystick button released.")
	press=pygame.key.get_pressed()
	if press[pygame.K_w]:
		y_key += float(-1)
	if press[pygame.K_a]:
		x_key += float(-1)
	if press[pygame.K_s]:
		y_key += float(1)
	if press[pygame.K_d]:
		x_key += float(1)
	if joystick_count > 0:
		x_joy = joystick.get_axis(0)
		y_joy = joystick.get_axis(1)
		print (str(x_joy) + str(y_joy))
	if x_joy < float(0.3) and x_joy > float(-0.3):
		x_joy = float(0)
	if y_joy < float(0.3) and y_joy > float(-0.3):
		y_joy = float(0)
	if x_joy > float(0.3) or x_joy < float(-0.3) or y_joy > float(0.3) or y_joy < float(-0.3) or Oy_joy != 0 or Ox_joy != 0:
		conn.sendall(str(x_joy) + "," +str(y_joy))
	if x_key > float(0.3) or x_key < float(-0.3) or y_key > float(0.3) or y_key < float(-0.3) or Oy_key != 0 or Ox_key != 0:
		conn.sendall(str(x_key) + "," +str(y_key))
 
	# Limit to 10 frames per second
	clock.tick(20)
 
pygame.quit()