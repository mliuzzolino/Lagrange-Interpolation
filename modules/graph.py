import matplotlib.pyplot as plt
import numpy as np


def plot(X, Y, L, inter_x, inter_y):
	plt.ion()
	plt.cla()
	# Set plot parameters
	x_min = min(X) - np.abs(max(X))*0.15
	x_max = max(X) + np.abs(max(X))*0.15
	y_min = min(L.Y_LagrangeP) - np.abs(max(L.Y_LagrangeP))*0.15
	y_max = max(L.Y_LagrangeP) + np.abs(max(L.Y_LagrangeP))*0.15

	# Plot points
	plt.plot(X, Y, 'ro')

	# Plot Lagrange Polynomial
	plt.plot(L.X_LagrangeP, L.Y_LagrangeP, 'b--')

	# Plot interpolated point
	plt.plot(inter_x, inter_y, 'ko', linewidth=20)
	plt.plot(np.linspace(x_min, inter_x, 50), np.ones(50)*inter_y, 'k--')
	plt.plot(np.ones(50)*inter_x, np.linspace(y_min, inter_y, 50), 'k--')
	
	# Set text to display tuple
	x_text_position = inter_x + 0.2
	y_text_position = inter_y + 4.2
	plt.text(x_text_position, y_text_position, "Interpolated Value \n({:.2f}, {:.2f})".format(inter_x, inter_y), fontsize=13.5)

	# Set axis
	plt.axis([x_min, x_max, y_min, y_max])

	# Set labels and title
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Lagrange Interpolation: Degree {}'.format(L.n-1))
	

