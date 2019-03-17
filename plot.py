import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from simulation import get_chance_of_positions as get_chance


def plot(n):
	"""
	Saves the plots of the chance of positions from simulation.py

	:param n: the number of steps the simulation will take.
	"""
	num_of_iterations, counter = get_chance(n)

	fig = plt.figure()

	ax = fig.add_subplot(111)
	ax.set_title("Position Color Map (n = {})".format(n))
	ax.set_xlabel("Number of iterations: {}".format(int(num_of_iterations)))

	plt.imshow(counter, cmap=plt.get_cmap('Blues_r'))

	ax.set_aspect('equal')

	divider = make_axes_locatable(ax)
	cax = divider.append_axes("right", size="5%", pad=0.05)

	plt.colorbar(orientation='vertical', cax=cax)
	fig.savefig('plots/plot-{:03}.png'.format(n), dpi=fig.dpi)


def main(max_n=10):
	"""
	The main function for this file. Makes max_n plots of the simulation.

	:param max_n: The number of plots to generate (default 10)
	"""
	for n in range(1, max_n + 1):
		plot(n)


if __name__ == "__main__":
	main()
