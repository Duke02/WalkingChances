import argparse

class Options:
	
	options = None
	
	@staticmethod
	def generate_options():
		arg_parser = argparse.ArgumentParser()
		arg_parser.add_argument('-N', '--num-of-rounds',
						type = int,
						required = False,
						default = 10**5,
						help = "The number of rounds to run in each simulation. Should be a big number. Default is 1E5")
		arg_parser.add_argument('-n', '--num-of-sims',
						type = int,
						required = False,
						default = 10,
						help = "The number of simulations (and plots) to run. Default is 10.")
		return arg_parser.parse_args()

	@staticmethod
	def get_options():
		if Options.options is None:
			Options.options = Options.generate_options()
		return Options.options

