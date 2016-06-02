import numpy as np

def to_radian(angle):
	return angle * np.pi / 180

def rotate(vector, angle):
	theta = to_radian(angle)
	matrix = [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
	return np.dot(matrix, vector)

def rotate_x(vector, angle):
	theta = to_radian(angle)
	matrix = [[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]]
	return np.dot(matrix, vector)

def rotate_y(vector, angle):
	theta = to_radian(angle)
	matrix = [[np.cos(theta), 0, -np.sin(theta)], [0, 1, 0], [np.sin(theta), 0, np.cos(theta)]]
	return np.dot(matrix, vector)

def rotate_z(vector, angle):
	theta = to_radian(angle)
	matrix = [[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]]
	return np.dot(matrix, vector)
