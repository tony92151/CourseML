import argparse 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import random
import time

class gameOfLive:
	def __init__(self,size):
		self.size = size
		self.black = 0
		self.white = 255
		self.game = None
		plt.ion()
		self.fig, self.ax = plt.subplots() 

	def initGame(self):
		temp = []
		for i in range(self.size**2):
			if random.random()>0.5:
				temp.append(self.white)	
			else:
				temp.append(self.black)
		temp = np.array(temp).reshape((self.size,self.size))
		self.game = temp

	def step(self,frameNum):
		tem = np.zeros(self.size**2).reshape((self.size,self.size))
		for i in range(self.size):
			for j in range(self.size):	

				sum = (self.game[i-1:i+2,:][:,j-1:j+2].sum()-self.game[i][j])/255
				#print("sum: ",sum)

				if self.game[i][j] == self.white:	
					if (sum < 2) or (sum > 3):
						tem[i][j] = self.black
					else:
						tem[i][j] = self.white
				elif self.game[i][j] == self.black:
					if (sum == 3):
						tem[i][j] = self.white
					else:
						tem[i][j] = self.black
		self.game = tem
		img = self.ax.imshow(a.game) 

if __name__ == '__main__': 
	a = gameOfLive(30)
	a.initGame()

	# ani = animation.FuncAnimation(a.fig, 
	# 							a.step, 
	# 							frames = 1, 
	# 							interval=50)
	# plt.show()
	#
	for i in range(1000):
		a.step(0)
		a.fig.canvas.draw()
		a.fig.canvas.flush_events()
		#time.sleep(0.05)
