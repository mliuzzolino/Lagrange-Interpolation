from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class Lagrange_Polynomial(object):

	def __init__(self, degree, X, Y):
		self.n = degree + 1
		self.X = X
		self.Y = Y
		
		self.X_LagrangeP = np.arange(min(X), max(X)+0.01, 0.01)

		self.generate_polynomial()
	

	def L_coeff_function(self, x, k):
		Lk = 1
		for i in xrange(self.n):
			if i == k:
				continue
			numerator = x - self.X[i]
			denominator = self.X[k] - self.X[i]
			Lk *= (numerator / denominator)
		return Lk


	def generate_polynomial(self):
		self.Y_LagrageP = []
		for x in self.X_LagrangeP:
			Pk = 0
			for k, y in enumerate(self.Y):
				Lk = self.L_coeff_function(x, k)
				Pk += (y * Lk)
			self.Y_LagrageP.append(Pk)


	def interpolate_at(self, inter_x):
		for index, x in enumerate(self.X_LagrangeP):
			if np.abs(inter_x - x) < 1e-4:
				return self.Y_LagrageP[index]

		return False
