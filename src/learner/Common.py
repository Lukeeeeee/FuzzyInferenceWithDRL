import tensorflow as tf


class NetworkCommon(object):

    @staticmethod
    def create_variable_summary(var, name_scope):
        """Attach a lot of summaries to a Tensor (for TensorBoard visualization)."""
        with tf.name_scope('summaries' + name_scope):
            mean = tf.reduce_mean(var)
            tf.summary.scalar('mean', mean)
            with tf.name_scope('stddev'):
                stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
            tf.summary.scalar('stddev', stddev)
            tf.summary.scalar('max', tf.reduce_max(var))
            tf.summary.scalar('min', tf.reduce_min(var))
            tf.summary.histogram('histogram', var)

    @staticmethod
    def return_file_writer(sess, log_file_dir):
        writer = tf.summary.FileWriter(log_file_dir, sess.graph)
        return writer

    REPLAY_BUFFER_SIZE = 1000000
    REPLAY_START_SIZE = 10000
    BATCH_SIZE = 100  # todo erase this one
    GAMMA = 0.99

    # Critic Network

    CRITIC_LAYER1_SIZE = 400
    CRITIC_LAYER2_SIZE = 300
    CRITIC_LEARNING_RATE = 1e-3
    CRITIC_TAU = 0.001
    CRITIC_L2 = 0.01

    # Actor Network

    ACTOR_LAYER1_SIZE = 400
    ACTOR_LAYER2_SIZE = 300
    ACTOR_LEARNING_RATE = 1e-4
    ACTOR_TAU = 0.001
    ACTOR_BATCH_SIZE = 64
    ACTOR_L2 = 0.01
