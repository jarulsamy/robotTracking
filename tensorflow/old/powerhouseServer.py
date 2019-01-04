# Get task number from command line
import tensorflow as tf
import sys


cluster = tf.train.ClusterSpec({"local": ["0.0.0.0:2222"]})
server = tf.train.Server(cluster, job_name="local", task_index=0)


server.start()
server.join()
