import numpy as np
import matplotlib.pyplot as plt

def rotate(vector, angle):
	theta = angle * np.pi / 180
	matrix = [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
	return np.dot(matrix, vector)

def plot2d(string, alpha, delta, init_angle=0, color='k'):
	plt.gca().set_aspect('equal', adjustable='box')
	pos = np.zeros(2)
	direction = rotate(np.array([1, 0]), init_angle)
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
	plt.show()
