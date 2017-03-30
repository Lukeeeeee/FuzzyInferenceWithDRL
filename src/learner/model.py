
import tensorflow as tf


class Model:

	def __init__(self, sess, initializer):
		self.sess = sess
		self.set_hyperparameters(initializer)

	def get_hyperparameters(self):
		return self.__hyperparameters
	def set_hyperparameters(self, initializer):
		self.__hyperparameters = initializer.get_parameters()
	hyperparameters = property(get_hyperparameters, set_hyperparameters)

	def get_loss(self):
		return self.__loss
	def set_loss(self):
		pass
	loss = property(get_loss, set_loss)

	def get_accuracy(self):
		return self.__accuracy
	def set_accuracy(self):
		pass
	accuracy = property(get_accuracy, set_accuracy)

	def get_precision(self):
		return self.__precision
	def set_precision(self):
		pass
	precision = property(get_precision, set_precision)

	def get_recall_rate(self):
		return self.__recall_rate
	def set_recall_rate(self):
		pass
	recall_rate = property(get_recall_rate, set_recall_rate)

	def get_train_graph(self):
		return self.__train_graph
	def set_train_graph(self):
		

		
		pass;
	train_graph = property(get_train_graph, set_train_graph)

	def get_test_graph(self):
		return self.__test_graph
	def set_test_graph(self):
		pass;
	test_graph = property(get_test_graph, set_train_graph)


	def optimize(self):
		pass
	def train(self):
		pass
	def test(self):
		pass

