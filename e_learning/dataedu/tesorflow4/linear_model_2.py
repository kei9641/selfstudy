import tensorflow as tf

x_train = [6, 5, 7, 3, 0, 4, 4, 1, 7, 5, 5, 0]
y_train = [30, 44, 39, 50, 29, 37, 39, 42, 36, 47, 27, 48]

W = tf.Variable(tf.random_normal([1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

# Linear model
hypothesis = x_train * W + b
# cost/loss function 
cost = tf.reduce_mean(tf.square(hypothesis - y_train))
# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0002)
train = optimizer.minimize(cost)
# Launch the graph in a session
sess = tf.Session()
# Initialize global variables in the graph
sess.run(tf.global_variables_initializer())

for step in range(10000):
    sess.run(train)
    if step % 100 == 0:
        print(step, sess.run(cost), sess.run(W), sess.run(b))
