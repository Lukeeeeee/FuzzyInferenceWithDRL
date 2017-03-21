from __future__ import print_function
import numpy as np


class Initializer:


	def __init__(self):
		self.set_parameters(input_nn_parameters)

	def set_parameters(self, input_nn_parameters):
		self.__parameters = {}
		self.__parameters['learning_rate'] = 0.03
		self.__parameters['epoch'] = 1000
		self.__parameters['batch_size'] = 200
		self.__parameters['data_size'] = np.array()
		for index, key in enumerate(input_nn_parameters):
			self.__parameters['index'] = key

	def get_parameters(self):
		return self.__parameters

	parameters = property(set_parameters, get_parameters)