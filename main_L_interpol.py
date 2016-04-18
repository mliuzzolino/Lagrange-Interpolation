from __future__ import division

from modules.lagrange_polynomial import Lagrange_Polynomial
from modules.graph import plot
import modules.utilities as utility 
import numpy as np

	
def main(X, Y, log_data=False, outfile_path=None):

	# Let n = len(X). Then the following must hold: Degree of L Poly < n
	Degree_of_Legrange_Polynomial = 4


	# Generate Lagrane Polynomial
	print("\tGenerating Lagrange Polynomials...")
	L = Lagrange_Polynomial(Degree_of_Legrange_Polynomial, X, Y)

	print("\n\tReady for interpolation.\n")

	while True:

		# Get value x to interpolate at from user
		inter_x = utility.get_user_input(L)

		# Calculate y value at user-entered x
		inter_y = L.interpolate_at(inter_x)

		# Checks for return False, indicating error in interpolating value at y
		if not inter_y:
			print("\n\tError calculating y for {}. Please choose another value for x.\n".format(inter_x))
			continue

		# Print interpolated tuple
		print("\n\tInterpolated value: ({:.3f}, {:.3f})\n".format(inter_x, inter_y))
		
		# Log data if enabled
		if log_data:
			utility.data_logger(inter_x, inter_y, outfile_path)
		# Plot graphs with interpolated point
		plot(X, Y, L, inter_x, inter_y)

		
if __name__ == '__main__':

	# Predefined data points from textbook. Can make more dynamic later.
	X = np.array([1, 2, 4, 5, 7])
	Y = np.array([52, 5, -5, -40, 10])

	# Print introduction
	utility.introduction()
	
	# Check if user wants to log data, obtain outfile name, and initiate main function
	log_data, outfile_path = utility.prompt_user()
	if not log_data:
		main(X, Y)
	else:
		main(X, Y, True, outfile_path)

	
