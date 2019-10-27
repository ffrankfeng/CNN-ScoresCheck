#coding:utf-8

import tensorflow as tf
from code.code_21 import mnist_generateds, mnist_lenet5_forward
import os
import numpy as np
from config import config
BATCH_SIZE = 300#一个batch的数量
LEARNING_RATE_BASE =  0.005 #初始学习率
LEARNING_RATE_DECAY = 0.99 #学习率衰减率
REGULARIZER = 0.0001 #

STEPS = 2000 #最大迭代次数
MOVING_AVERAGE_DECAY = 0.99 #滑动平均衰减率
MODEL_SAVE_PATH = config.MODEL_SAVE_PATH_41
MODEL_NAME= config.MODEL_NAME_41
train_num_examples = 8154#2

def backward():
    #1、给x，y_占位
    x = tf.placeholder(tf.float32, [
	BATCH_SIZE,#每次喂入的图片数量
	mnist_lenet5_forward.IMAGE_SIZE,#图片的行分辨率
	mnist_lenet5_forward.IMAGE_SIZE,#图片的列分辨率
	mnist_lenet5_forward.NUM_CHANNELS]) #通道数
    y_ = tf.placeholder(tf.float32, [None, mnist_lenet5_forward.OUTPUT_NODE])
    #2、调用前向传播过程，得到维度为10的tensor
    y = mnist_lenet5_forward.forward(x, True, REGULARIZER)
    #3、求含有正则化的损失值
    #声明一个全局计数器，输入0
    global_step = tf.Variable(0, trainable=False)

    #对网络最后一层的输出y做softmax，求取输出属于莫一类的概率，结果为一个num_classes大小的向量，
    #再将此向量和实际标签值做交叉熵，返回一个向量值
    ce = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    #通过tf.reduce_mean()函数对得到的向量求均值，得到loss
    cem = tf.reduce_mean(ce)
    #添加正则化中的losses到loss中
    loss = cem + tf.add_n(tf.get_collection('losses')) 


    #4、实现指数衰减学习率
    learning_rate = tf.train.exponential_decay( 
        LEARNING_RATE_BASE,#初始学习率
        global_step,
        train_num_examples / BATCH_SIZE,
		LEARNING_RATE_DECAY,
        staircase=True) #阶梯形衰减

    #构造一个实现梯度下降算法法优化器，再通过使用minimize更新存储要训练的变量的列表来减少loss
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

    #实现滑动平均模型
    ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    ema_op = ema.apply(tf.trainable_variables())
    #将train_step和ema_op两个训练操作绑定到train_op上
    with tf.control_dependencies([train_step, ema_op]): 
        train_op = tf.no_op(name='train')

    #实例化一个保存和恢复变量的saver，并创建一个会话
    saver = tf.train.Saver()
    img_batch, label_batch = mnist_generateds.get_tfrecord(BATCH_SIZE, isTrain=True)#3

    with tf.Session() as sess:
        #计算图中的变量，并用sess.run实现初始化
        init_op = tf.global_variables_initializer() 
        sess.run(init_op)
        #通过checkpoint文件定位到最新保存的模型，如文件存在，则加载最新的模型
        ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH) 
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
         # 开启线程协调器
        coord = tf.train.Coordinator()  # 4
        # 这个函数将会启动输入队列的线程，填充训练样本到队列中，以便出队操作可以从队列中拿到样本。
        # 这种情况下最好配合使用一个tf.train.Coordinator，这样可以在发生错误的情况下正确的关闭这些线程。
        # 参数说明：sess：运行队列操作的会话
        # coordinate：协调启动的线程
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)  # 5
        for i in range(STEPS):
            xs, ys = sess.run([img_batch, label_batch])  # 6

            #读取一个batch数据，将输入数据xs转成与网络输入相同形状的矩阵
            #xs, ys = mnist.train.next_batch(BATCH_SIZE)
            reshaped_xs = np.reshape(xs, (
                BATCH_SIZE,
                mnist_lenet5_forward.IMAGE_SIZE,
                mnist_lenet5_forward.IMAGE_SIZE,
                mnist_lenet5_forward.NUM_CHANNELS))
            #喂入训练图像和标签，开始训练
            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: reshaped_xs, y_: ys})
            if i % 100 == 0: 
                print("After %d training step(s), loss on training batch is %g." % (step, loss_value))
                saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=global_step)
            # 关闭线程协调器
        coord.request_stop()  # 7
        coord.join(threads)  # 8
def main():
    backward()

if __name__ == '__main__':
    main()


