import pygame 
import random as r

#pygame.init()

#win=pygame.display.set_mode((500,500))
#pygame.display.set_caption('mewo snake')

class Square:
	def __init__(self,x,y,width):
		self.x=x
		self.y=y
		self.width=width

class Snake:
	def __init__(self,x,y,width,vel,length):
		self.width=width
		self.vel=vel
		self.nodes=[]
		self.length=length
		my_square=Square(x=x,y=y,width=width)
		for i in range(length):
			self.nodes.append(Square(x=x,y=y,width=width))

	def step(self,new_direction):
		wanted_length=self.length
		x=self.nodes[len(self.nodes)-1].x
		y=self.nodes[len(self.nodes)-1].y
		if new_direction=='stop':
			pass
		if new_direction== 'left':
			self.nodes.append(Square(x=x-self.vel, y=y, width=self.width))
			if wanted_length<len(self.nodes):
				self.nodes.pop(0)
		if new_direction== 'right':
			self.nodes.append(Square(x=x+self.vel, y=y, width=self.width))
			if wanted_length<len(self.nodes):
				self.nodes.pop(0)
		if new_direction== 'up':
			self.nodes.append(Square(x=x,y=y-self.vel,width=self.width))
			if wanted_length<len(self.nodes):
				self.nodes.pop(0)
		if new_direction== 'down':
			self.nodes.append(Square(x=x,y=y+self.vel,width=self.width))
			if wanted_length<len(self.nodes):
				self.nodes.pop(0)

def eat(snake,apple):
	if snake.nodes[len(snake.nodes)-1].x==apple.x and snake.nodes[len(snake.nodes)-1].y==apple.y:
		
		return True
	else: return False

def collision(snake):
	headx=snake.nodes[len(snake.nodes)-1].x
	heady=snake.nodes[len(snake.nodes)-1].y
	tail=snake.nodes[0:len(snake.nodes)-2]
	for node in tail:
		if headx==node.x and heady==node.y:
			print(node.x,node.y)
			return True
	return False

def new_random_position(snake):
	apple.x=20*r.randint(1,24)
	apple.y=20*r.randint(1,24)
	for nodes in my_snake.nodes: #making sure new apple is not in snake
		if apple.x==nodes.x and apple.y==nodes.y:
			new_random_position(snake)

names=[]
quit=False
while(quit==False):
	run=True
	first_move=True
	new_direction='stop'
	old_direction='stop'

	apple=Square(x=20*r.randint(1,24),y=20*r.randint(1,24),width=20)

	my_snake=Snake(x=40,y=40,width=20,vel=20,length=3)

	speed=50

	print('type your name:')
	player=input()

	pygame.init()
	win=pygame.display.set_mode((500,500))
	pygame.display.set_caption('mewo snake')

	while run:
		pygame.time.delay(speed) #delay

		for event in pygame.event.get(): #quit the game
			if event.type==pygame.QUIT:
				run=False
				pygame.quit()
		
		if new_direction !='stop':
			if collision(my_snake): #checks if the snake collides with itself
				run=False
				break

		old_direction=new_direction

		keys=pygame.key.get_pressed() #press keys
		if keys[pygame.K_LEFT] and old_direction!='right':
			new_direction='left'
		if keys[pygame.K_RIGHT]and old_direction!='left':
			new_direction='right'
		if keys[pygame.K_UP]and old_direction!='down':
			new_direction='up'
		if keys[pygame.K_DOWN]and old_direction!='up':
			new_direction='down'
		
		if my_snake.nodes[len(my_snake.nodes)-1].x>=500 or my_snake.nodes[len(my_snake.nodes)-1].y>=500: #boundaries
			run=False
			break
		if my_snake.nodes[len(my_snake.nodes)-1].x<=0 or my_snake.nodes[len(my_snake.nodes)-1].y<=0:
			run=False
			break

		if eat(my_snake, apple):
			speed-=1
			my_snake.length+=1
			old_x=apple.x
			old_y=apple.y
			new_random_position(my_snake)

		my_snake.step(new_direction)

		win.fill((0,0,0))
		for node in my_snake.nodes: #draw the snake
			headx=node.x
			heady=node.y
			#print('position: x:{}, y:{}'.format(headx,heady))
			pygame.draw.rect(win,(0,255,0),(headx,heady,my_snake.width,my_snake.width))
			pygame.draw.rect(win,(255,0,0),(apple.x,apple.y,apple.width,apple.width)) #draw the apple

		pygame.display.update()

	pygame.quit()
	print('your score: {} Points!'.format(len(my_snake.nodes)-3))
	names.append((player,len(my_snake.nodes)-3))
	s,n = 0,''
	for name in names:
		if name[1]>s:
			s=name[1]
			n=name[0]
	print('highscore {} with {} points!'.format(n,s))
	pygame.time.delay(500)
	print('retry?(y/n)')
	retry=input()
	if retry=='n':
		pygame.quit()
		quit=True
	