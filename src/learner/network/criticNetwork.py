import tensorflow as tf

from network import Network
from src.learner.common import NetworkCommon as com

LAYER1_SIZE = com.CRITIC_LAYER1_SIZE
LAYER2_SIZE = com.CRITIC_LAYER2_SIZE
LEARNING_RATE = com.CRITIC_LEARNING_RATE
TAU = com.CRITIC_TAU
L2 = com.CRITIC_L2


class CriticNetwork(Network):
    """docstring for CriticNetwork"""

    def __init__(self, sess, state_dim, action_dim):
        super(CriticNetwork, self).__init__(sess)

        self.time_step = 0
        # self.sess = sess
        # create q network
        self.state_input, \
        self.action_input, \
        self.q_value_output, \
        self.net, \
        self.is_training = self.create_q_network(state_dim, action_dim)

        # create target q network (the same structure with q network)
        self.target_state_input, \
        self.target_action_input, \
        self.target_q_value_output, \
        self.target_update, \
        self.target_is_training = self.create_target_q_network(state_dim, action_dim, self.net)

        self.create_training_method()

        # initialization
        self.sess.run(tf.global_variables_initializer())

        self.update_target()

    def create_training_method(self):
        # Define training optimizer
        self.y_input = tf.placeholder("float", [None, 1])
        weight_decay = tf.add_n([L2 * tf.nn.l2_loss(var) for var in self.net])
        self.cost = tf.reduce_mean(tf.square(self.y_input - self.q_value_output)) + weight_decay
        self.optimizer = tf.train.AdamOptimizer(LEARNING_RATE).minimize(self.cost)
        self.action_gradients = tf.gradients(self.q_value_output, self.action_input)

    def create_q_network(self, state_dim, action_dim):
        # the layer size could be changed
        layer1_size = LAYER1_SIZE
        layer2_size = LAYER2_SIZE

        state_input = tf.placeholder("float", [None, state_dim])
        action_input = tf.placeholder("float", [None, action_dim])
        is_training = tf.placeholder(tf.bool)

        W1 = self.variable([state_dim, layer1_size], state_dim)
        b1 = self.variable([layer1_size], state_dim)
        W2 = self.variable([layer1_size, layer2_size], layer1_size + action_dim)
        W2_action = self.variable([action_dim, layer2_size], layer1_size + action_dim)
        b2 = self.variable([layer2_size], layer1_size + action_dim)
        W3 = tf.Variable(tf.random_uniform([layer2_size, 1], -3e-3, 3e-3))
        b3 = tf.Variable(tf.random_uniform([1], -3e-3, 3e-3))

        layer0_bn = self.batch_norm_layer(state_input, training_phase=is_training, scope_bn='q_batch_norm_0',
                                          activation=tf.identity)

        layer1 = tf.nn.relu(tf.matmul(layer0_bn, W1) + b1)
        layer2 = tf.nn.relu(tf.matmul(layer1, W2) + tf.matmul(action_input, W2_action) + b2)
        q_value_output = tf.identity(tf.matmul(layer2, W3) + b3)

        return state_input, action_input, q_value_output, [W1, b1, W2, W2_action, b2, W3, b3], is_training

    def create_target_q_network(self, state_dim, action_dim, net):
        state_input = tf.placeholder("float", [None, state_dim])
        action_input = tf.placeholder("float", [None, action_dim])
        is_training = tf.placeholder(tf.bool)

        ema = tf.train.ExponentialMovingAverage(decay=1 - TAU)
        target_update = ema.apply(net)
        target_net = [ema.average(x) for x in net]
        layer0_bn = self.batch_norm_layer(state_input, training_phase=is_training, scope_bn='target_q_batch_norm_0',
                                          activation=tf.identity)

        layer1 = tf.nn.relu(tf.matmul(layer0_bn, target_net[0]) + target_net[1])
        layer2 = tf.nn.relu(tf.matmul(layer1, target_net[2]) + tf.matmul(action_input, target_net[3]) + target_net[4])
        q_value_output = tf.identity(tf.matmul(layer2, target_net[5]) + target_net[6])

        return state_input, action_input, q_value_output, target_update, is_training

    def update_target(self):
        self.sess.run(self.target_update)

    def train(self, y_batch, state_batch, action_batch):
        self.time_step += 1
        _, cost = self.sess.run([self.optimizer, self.cost], feed_dict={
            self.y_input: y_batch,
            self.state_input: state_batch,
            self.action_input: action_batch,
            self.is_training: True
        })
        return cost

    def gradients(self, state_batch, action_batch):
        return self.sess.run(self.action_gradients, feed_dict={
            self.state_input: state_batch,
            self.action_input: action_batch,
            self.is_training: False
        })[0]

    def target_q(self, state_batch, action_batch):
        return self.sess.run(self.target_q_value_output, feed_dict={
            self.target_state_input: state_batch,
            self.target_action_input: action_batch,
            self.target_is_training: False
        })

    def q_value(self, state_batch, action_batch):
        return self.sess.run(self.q_value_output, feed_dict={
            self.state_input: state_batch,
            self.action_input: action_batch,
            self.is_training: False})
