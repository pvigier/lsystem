import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from util import *

# 2D

def plot2d(string, alpha, delta=1, init_direction=np.array([1., 0]), colors={}):
	plt.gca().set_aspect('equal', adjustable='box')
	pos = np.zeros(2, dtype=np.float64)
	direction = init_direction
	color = 'k'
	saved_states = []
	for x in string:
		if x == 'F':
			new_pos = pos + direction
			plt.plot([pos[0], new_pos[0]], [pos[1], new_pos[1]], c=color)
			pos = new_pos
		elif x == '+':
			direction = rotate(direction, alpha)
		elif x == '-':
			direction = rotate(direction, -alpha)
		elif x == '*':
			direction *= delta
		elif x == '/':
			direction /= delta
		elif x == '|':
			direction = rotate(direction, 180)
		elif x == '[':
			saved_states.append((pos, direction))
		elif x == ']':
			pos, direction = saved_states.pop()
		elif x in colors:
			color = colors[x]
	plt.show()

# 3D

def axis_equal_3d(ax):
    extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    sz = extents[:,1] - extents[:,0]
    centers = np.mean(extents, axis=1)
    maxsize = max(abs(sz))
    r = maxsize / 2
    for ctr, dim in zip(centers, 'xyz'):
        getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)

def plot3d(string, alpha, delta=1, init_direction=np.array([1., 0, 0]), colors={}):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	pos = np.zeros(3, dtype=np.float64)
	direction = init_direction
	color = 'k'
	saved_states = []
	for x in string:
		if x == 'F':
			new_pos = pos + direction
			ax.plot([pos[0], new_pos[0]], [pos[1], new_pos[1]], [pos[2], new_pos[2]], c=color)
			pos = new_pos
		elif x == '+':
			direction = rotate_x(direction, alpha)
		elif x == '-':
			direction = rotate_x(direction, -alpha)
		elif x == '&':
			direction = rotate_y(direction, alpha)
		elif x == '^':
			direction = rotate_y(direction, -alpha)
		elif x == '<':
			direction = rotate_z(direction, alpha)
		elif x == '>':
			direction = rotate_z(direction, -alpha)
		elif x == '*':
			direction = direction * delta
		elif x == '/':
			direction = direction / delta
		elif x == '|':
			direction = rotate_x(direction, 180)
			direction = rotate_y(direction, 180)
			direction = rotate_z(direction, 180)
		elif x == '[':
			saved_states.append((pos, direction))
		elif x == ']':
			pos, direction = saved_states.pop()
		elif x in colors:
			color = colors[x]
	axis_equal_3d(ax)
	plt.show()