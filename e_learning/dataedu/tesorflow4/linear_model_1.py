import tensorflow as tf

x_train = [65, 50, 55, 65, 55, 70, 65, 70]
y_train = [85, 74, 76, 90, 85, 87, 94, 98]

W = tf.Variable(tf.random_normal([1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')
'''
Variable() : 가중치를 찾을 때 사용
random_normal([1]) : 표준 정규 분포를 따르는 하나의 값
name = '' : object의 이름 지정
'''

# Linear model
hypothesis = x_train * W + b
# cost/loss function 
cost = tf.reduce_mean(tf.square(hypothesis - y_train)) # 통계 : MSE(Mean Square Error)
# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0002)
train = optimizer.minimize(cost)
'''
optimizer : 학습할 때 사용
GradientDescentOptimizer(learning_rate=) : 학습률을 변화시키며 W, b를 학습
train : cost를 최적화(minimize())한 결과값을 저장
'''
# Launch the graph in a session
sess = tf.Session()
# Initialize global variables in the graph
sess.run(tf.global_variables_initializer())

for step in range(10000):
    sess.run(train)
    if step % 100 == 0: # 100마다 결과를 확인
        print(step, sess.run(cost), sess.run(W), sess.run(b))

'''
결과값에 NaN이 나오면 학습이 제대로 되지 않음(learning_rate가 밖으로 나감)
'''