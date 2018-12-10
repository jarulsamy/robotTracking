# Get task number from command line
import tensorflow as tf
import sys
task_number = int(sys.argv[1])


cluster = tf.train.ClusterSpec({"local": ["10.0.0.3:2222"]})
server = tf.train.Server(cluster, job_name="local", task_index=task_number)

print("Starting server #{}".format(task_number))

server.start()
server.join()
