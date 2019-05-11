# coding:utf-8
import tensorflow as tf
import numpy as np
from PIL import Image
import os
from config import config

image_train_path = config.image_train_path_101
label_train_path = config.label_train_path_101
tfRecord_train = config.tfRecord_train_101
image_test_path = config.image_test_path_101
label_test_path = config.label_test_path_101
tfRecord_test = config.tfRecord_test_101
data_path = config.data_path_101
resize_height = 28
resize_width = 28


# 生成tfrecords文件
def write_tfRecord(tfRecordName, image_path, label_path):
    # 新建一个writer
    writer = tf.python_io.TFRecordWriter(tfRecordName)
    num_pic = 0
    f = open(label_path, 'r')
    contents = f.readlines()
    f.close()
    # for循环遍历每张图和标签
    for content in contents:
        value = content.split()
        img_path = image_path + value[0]
        img = Image.open(img_path)
        img_raw = img.tobytes()
        labels = [0] * 101
        labels[int(value[1])] = 1
        # 把每张图片和标签分装到example中
        example = tf.train.Example(features=tf.train.Features(feature={
            'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw])),
            'label': tf.train.Feature(int64_list=tf.train.Int64List(value=labels))
        }))
        # 把数据序列化为字符串存储
        writer.write(example.SerializeToString())
        num_pic += 1
        print("the number of picture:", num_pic)
    writer.close()
    print("write tfrecord successful")


def generate_tfRecord():
    isExists = os.path.exists(data_path)
    if not isExists:
        os.makedirs(data_path)
        print('The directory was created successfully')
    else:
        print('directory already exists')
    write_tfRecord(tfRecord_train, image_train_path, label_train_path)
    write_tfRecord(tfRecord_test, image_test_path, label_test_path)


# 解析tfrecords文件
def read_tfRecord(tfRecord_path):
    # 生成一个先进先出的队列，文件阅读器会使用它来读取数据
    # shuffle=True : 没轮随机打乱读取顺序
    filename_queue = tf.train.string_input_producer([tfRecord_path], shuffle=True)
    # 新建一个reader
    reader = tf.TFRecordReader()
    # 把读出的每个样本保存在serialized_example中进行解序列化，
    # 标签和图片的键名应该和制作tfrecords的键名相同，其中标签
    _, serialized_example = reader.read(filename_queue)
    features = tf.parse_single_example(serialized_example,  # 一个标量字符串张量
                                       features={  # 一个字典映射功能键FixedLenFeature或VarLenFeature的值
                                           'label': tf.FixedLenFeature([101], tf.int64),
                                           'img_raw': tf.FixedLenFeature([], tf.string)
                                       })
    img = tf.decode_raw(features['img_raw'], tf.uint8)  # 将img_raw字符串转换为8位无符号整型
    img.set_shape([784])  # 将形状变成一行784列
    img = tf.cast(img, tf.float32) * (1. / 255)  # 变成0到1之间的浮点数
    label = tf.cast(features['label'], tf.float32)  # 把标签列表变成浮点数
    return img, label  # 返回图片和标签


def get_tfrecord(num, isTrain=True):
    if isTrain:
        tfRecord_path = tfRecord_train
    else:
        tfRecord_path = tfRecord_test
    img, label = read_tfRecord(tfRecord_path)
    # 随机读取一个batch的数据
    img_batch, label_batch = tf.train.shuffle_batch([img, label],  # 待乱序处理的列表中的样本
                                                    batch_size=num,  # 从队列中提取的新批量大小
                                                    num_threads=8,
                                                    capacity=20000,  # 队列中元素最大数量
                                                    min_after_dequeue=1000)  # 出队后队列中最小数量元素，用于确保元素的混合级别
    return img_batch, label_batch  # 返回的图片和标签为随机抽取的batch_size组


def main():
    generate_tfRecord()


if __name__ == '__main__':
    main()
