"""
A particle starts at (0, 0) and moves in one unit independent
steps with equal probabilities of 1/4 in each of the four
directions: north, south, east, and west. Let S equal
the east-west position and T the north-south position
after n steps.
"""

from random import choice

import numpy as np

from options import Options

# Directions (K -> V is initial of direction -> (dx, dy)
directions = {
	'S': (0, -1),
	'N': (0, 1),
	'E': (1, 0),
	'W': (-1, 0)
	}


def get_direction():
	"""
	Get a random direction. Each direction has a 25% chance of occurring.
	
	:returns: the chosen directions changes in x and y
	"""
	dirs = "NSEW"
	return directions[choice(dirs)]


def change_position(curr_pos, change_in_pos):
	"""
	Updates the current location based on the change in position.
	
	:returns: the update position (x, y)
	"""
	return curr_pos[0] + change_in_pos[0], curr_pos[1] + change_in_pos[1]


def increment_counter(counter, end_pos):
	"""
	Increments the provided counter at the given location.
	
	:param counter: an numpy ndarray with the number of all ending locations in the simulation.
	:param end_pos: the ending position of the last round of the simulation.
	:returns: the updated counter.
	"""
	counter[end_pos[1], end_pos[0]] += 1
	return counter


def get_chance_of_positions(n):
	"""
	Gets the approximated chance the particle ends at a given location.
	
	Starting location is in the center of the output.
	
	:param n: The number of steps the simulation is to take.
	:returns: the number of iterations and an ndarray with the approximated chance the particle would be at each location.
	"""
	# The starting position starts at n, n so that we can pass in the location
	# into the counter without worrying about negative numbers.
	starting_pos = (n, n)

	options = Options.get_options()

	total_num_of_sims = options.num_of_rounds

	counter = np.zeros(shape=(2 * n + 1, 2 * n + 1))

	for j in range(total_num_of_sims):
		curr_pos = starting_pos
		for i in range(n):
			change_in_pos = get_direction()
			curr_pos = change_position(curr_pos, change_in_pos)
		counter = increment_counter(counter, curr_pos)

	chances = np.round(counter / total_num_of_sims, decimals=n + 1)
	return total_num_of_sims, chances
