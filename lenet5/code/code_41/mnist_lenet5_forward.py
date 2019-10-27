# coding:utf-8
import tensorflow as tf
IMAGE_SIZE = 28  # 每张图片的分辨率
NUM_CHANNELS = 1  # 灰度图，所以图片通道数为1
CONV1_SIZE = 5  # 第一层卷积核大小为5
CONV1_KERNEL_NUM = 32  # 卷积核个数为32
CONV2_SIZE = 5
CONV2_KERNEL_NUM = 64
FC_SIZE = 512  # 全连接层第一层为512个神经元
LAYER1_NODE = 64*64
LAYER2_NODE = 64*8
OUTPUT_NODE = 41  # 全连接层第二层为10个神经元

def get_weight(shape, regularizer):
    w = tf.Variable(tf.truncated_normal(shape,stddev=0.1))
    if regularizer != None :
        tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w

def get_bias(shape): 
	b = tf.Variable(tf.zeros(shape))  
	return b
# tf.nn.conv2d(输入描述[batch，行分辨率，列分辨率，通道数]，
            # 卷积核描述[行分辨率，列分辨率，通道数，卷积核个数]，
            #  核滑动步长[1，行步长，列步长，1]，
            #  填充模式padding ：same ：全零填充)
def conv2d(x,w):  
	return tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')

# tf.nn.max_pool(输入描述[batch，行分辨率，列分辨率，通道数]，
            #  池化核描述[行分辨率，列分辨率，通道数，卷积核个数]，
            #  池化核滑动步长[1，行步长，列步长，1]，
            #  填充模式padding ：same ：全零填充)
def max_pool_2x2(x):
	return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME') 

def forward(x, train, regularizer):
    # 1、实现第一层卷积
    #  根据先前定义的参数大小，初始化第一层卷积核和偏置项
    conv1_w = get_weight([CONV1_SIZE, CONV1_SIZE, NUM_CHANNELS, CONV1_KERNEL_NUM], regularizer) 
    conv1_b = get_bias([CONV1_KERNEL_NUM])
    # 实现卷积运算，输入参数为x和第一层卷积核参数
    conv1 = conv2d(x, conv1_w)
    # 第一层卷积的输出值作为非线性激活函数的输入值，
    #  首先通过tf.nn.bias_add()对卷积后的输出添加偏置，并通过tf.nn.relu()完成非线性激活
    relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_b)) 
    #  根据先前定义的池化函数，将第一层激活后的输出值进行最大池化。
    pool1 = max_pool_2x2(relu1)
    # 2、实现第二层卷积
    #  初始化第二层卷积层的变量和偏置项，改层每一个卷积核的通道数要与上一次卷积核的个数一致
    conv2_w = get_weight([CONV2_SIZE, CONV2_SIZE, CONV1_KERNEL_NUM, CONV2_KERNEL_NUM],regularizer) 
    conv2_b = get_bias([CONV2_KERNEL_NUM])
    #  实现卷积运算，输入参数为上一层的输出pool1和第二层卷积核参数
    conv2 = conv2d(pool1, conv2_w)
    #  实现第二层非线性激活函数
    relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_b))
    #  根据先前定义的池化函数，将第二层激活后的输出值进行最大池化
    pool2 = max_pool_2x2(relu2)

    # 3、将第二层池化层的输出pool2矩阵转化为全连接层的输入格式即向量形式
    # 根据get_shape()函数得到pool2输出矩阵的维度，并存入list中，其中pool_shape[0]为一个batch值。
    pool_shape = pool2.get_shape().as_list()
    # 从list中一次去除矩阵的长宽及深度，并求三者的成绩，得到矩阵被拉长后的长度
    nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
    # 将pool2转化为一个batch的向量再传入后续的全连接
    reshaped = tf.reshape(pool2, [pool_shape[0], nodes])
    # 4、实现第三层全连接层
    # 初始化全连接层的权重，并加入正则化
    fc1_w = get_weight([nodes, FC_SIZE], regularizer)
    # 初始化全连接层的偏置项
    fc1_b = get_bias([FC_SIZE])
    # 将转化后的reshaped向量与权重fc1_w做矩阵乘法运算，然后再加上偏置，最后在使用relu进行激活
    fc1 = tf.nn.relu(tf.matmul(reshaped, fc1_w) + fc1_b)
    # 若干是训练阶段，则对改层输出使用dropout，也就是随机的将改层输出中的一半神经元置为无效
    #  是为了避免过拟合而设置的，一般值在全连接层使用
    if train: fc1 = tf.nn.dropout(fc1, 0.5)

    # 5、实现第四层全连接层的前向传播过程
    # # 初始化全连接层对应的变量
    # fc2_w = get_weight([FC_SIZE, OUTPUT_NODE], regularizer)
    # fc2_b = get_bias([OUTPUT_NODE])
    # # 将转化后的reshaped向量和权重fc2_w做矩阵乘法运算，然后再加上偏置
    # y = tf.matmul(fc1, fc2_w) + fc2_b

    w1 = get_weight([FC_SIZE, LAYER1_NODE], regularizer)
    b1 = get_bias([LAYER1_NODE])
    y1 = tf.nn.relu(tf.matmul(fc1, w1) + b1)

    w2 = get_weight([LAYER1_NODE, LAYER2_NODE], regularizer)
    b2 = get_bias([LAYER2_NODE])
    y = tf.matmul(y1, w2) + b2

    return y
