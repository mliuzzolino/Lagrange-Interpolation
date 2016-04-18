from __future__ import division
import numpy as np
import sys, os


def introduction():
	print('\n'*2)
	print('\t|------------------------------------------------|')
	print("\t| Welcome to the Lagrange Interpolation Script.  |")
	print("\t| Given N data inputs, this script will generate |")
	print("\t| an N-1 degree Lagrange Polynomial, with which  |")
	print("\t| you can utilize to find interpolated values.   |")
	print("\t|                                                |")
	print("\t| Press q at anytime to quit the program.        |")
	print('\t|------------------------------------------------|')
	print('\n'*2)


def prompt_user(default=True, prompt=None):
	yes_answers = ['y', 'Y', 'yes', 'YES', 'Yes']
	no_answers =  ['n', 'N', 'no',  'NO',  'No']
	quit_answers = ['q', 'Q', 'quit', 'QUIT', 'Quit', 'exit', 'EXIT', 'Exit']

	while True:
		if default:
			user_choice = raw_input("\tWould you like to log the interpolated values (y/n)? ")
		else:
			user_choice = raw_input(prompt)

		if user_choice in yes_answers:
			if default:
				outfile_path = get_outfile_name()
			else:
				outfile_path = None
			return True, outfile_path

		elif user_choice in no_answers:
			return False, False

		elif user_choice in quit_answers:
			print("\n\tExiting program...\n\n")
			sys.exit()
		else:
			print("\n\tERROR: Invalid entry.\n")
			continue


def get_outfile_name():

	filename = raw_input("\n\tEnter filename for output data:\n\t>> ")
	while True:

		# Check if entered filename was only a space. Invalid. Reprompt user.
		if len(filename.strip()) == 0:
			print("\tERROR: You did not enter a filename.\n")
			filename = raw_input("\n\tEnter another filename for output data:\n\t>> ")
			continue

		# Check if file already exists. 
		elif check_file_exists(filename):
			print("\n\tWarning: File already exists.")
			# Ask if user wants to overwrite the file.
			overwrite, _ = prompt_user(False, '\tOverwrite existing file (y/n)? ')
			
			# If user wants to overwrite...
			if overwrite:
				file_path = './data/output/' + filename + '.csv'

			# Else, user wants to save existing file and pick another name
			elif not overwrite:
				filename = raw_input("\n\tEnter another filename for output data file: ")
				continue

		# Else, everything is fine.
		else:
			file_path = './data/output/' + filename.strip() + '.csv'

		# Confirm with user
		print("\n\tThe data will be stored as {}.csv".format(filename))
		filename_ok, _ = prompt_user(False, "\tContinue (y/n)? ")
		if filename_ok:
			break
		else:
			filename = raw_input("\n\tEnter another filename for output data file: ")

	# Final confirm of filename and save location
	print("\n\tOutfile location: {}\n".format(file_path))
	print('\t' + '='*50)

	# Create outfile
	with open(file_path, 'w') as outfile:
		outfile.write("x, y\n")
	
	return file_path
		

def get_user_input(L):

	# Set bounds within which user can choose values
	min_x, max_x = min(L.X), max(L.X)

	while True:
		user_input = raw_input("\n\tEnter value x within [{}, {}]:\n\t>> ".format(min_x, max_x))
		
		if user_input == 'q':
			print("\n\tExiting program...\n\n")
			sys.exit()

		# Ensure user enters appropriate numeric value; e.g., No letters or "weird" input values
		try:
			x_inter = float("{:.3f}".format(float(user_input)))
			
		except:
			print("\n\tERROR: Invalid entry.\n")
			continue

		if x_inter < min_x or x_inter > max_x:
			print("\n\tERROR: Entry outside of [{}, {}]".format(min_x, max_x))
			continue
		else:
			break

	return x_inter


def check_file_exists(filename):

	outfile_dir = "./data/output/"
	term_command = "ls " + outfile_dir + "*.csv"
	raw_outfiles = os.popen(term_command)

	# Determine infiles already processed
	outfiles = []
	for index, outfile in enumerate(raw_outfiles):
		outfiles.append(outfile[len(outfile_dir):-5])

	if filename in outfiles:
		return True
	else:
		return False


def data_logger(inter_x, inter_y, outfile_name):
	with open(outfile_name, 'a') as outfile:
		line = "{},{}\n".format(inter_x, inter_y)
		outfile.write(line)


