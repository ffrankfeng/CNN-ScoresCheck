# coding:utf-8

import tensorflow as tf
import numpy as np
from PIL import Image
import mnist_lenet5_backward as mnist_backward
import mnist_lenet5_forward as mnist_forward


def restore_model(testPicArr):
    with tf.Graph().as_default() as tg:
        x = tf.placeholder(tf.float32, [
            1,
            mnist_forward.IMAGE_SIZE,
            mnist_forward.IMAGE_SIZE,
            mnist_forward.NUM_CHANNELS])
        y = mnist_forward.forward(x, False, None)
        preValue = tf.argmax(y, 1)
        variable_averages = tf.train.ExponentialMovingAverage(mnist_backward.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)

        with tf.Session() as sess:
            ckpt = tf.train.get_checkpoint_state(mnist_backward.MODEL_SAVE_PATH)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess, ckpt.model_checkpoint_path)
                # reshaped_x = np.reshape(mnist.test.images, (
                #     mnist.test.num_examples,
                #     mnist_lenet5_forward.IMAGE_SIZE,
                #     mnist_lenet5_forward.IMAGE_SIZE,
                #     mnist_lenet5_forward.NUM_CHANNELS))
                # accuracy_score = sess.run(accuracy, feed_dict={x: reshaped_x, y_: mnist.test.labels})

                testPicArr =np.resize(testPicArr,(1,28,28,1))
                preValue = sess.run(preValue, feed_dict={x: testPicArr})
                return preValue
            else:
                print("No checkpoint file found")
                return -1


def pre_pic(picName):
    img = Image.open(picName)
    reIm = img.resize((28, 28), Image.ANTIALIAS)
    im_arr = np.array(reIm.convert('L'))
    threshold = 50
    for i in range(28):
        for j in range(28):
            im_arr[i][j] = 255 - im_arr[i][j]
            if (im_arr[i][j] < threshold):
                im_arr[i][j] = 0
            else:
                im_arr[i][j] = 255
    #print(im_arr)
    nm_arr = im_arr.reshape([1, 784])
    nm_arr = nm_arr.astype(np.float32)
    img = np.multiply(nm_arr, 1.0 / 255.0)

    return nm_arr  # img


def application():
    # while True:
    # testPic = input("the path of test picture:")
    # preValue = restore_model(testPic)
    # print("The prediction number is:", preValue)
    for i in range(20):
        #testPic = "C:\\Users\\asus\\Desktop\\stitp\\核分系统\pic\\"+str(i)+".png"  # input("the path of test picture:")
        #testPic="D:\\demo\\testpic28\\"+str(i)+".jpg"
        testPic="C:/Users/asus/Desktop/train/"+str(i+1)+".jpg"
        testPicArr = pre_pic(testPic)
        preValue = restore_model(testPicArr)
        #print("The prediction number is:", preValue)
        print(int(preValue))


def main():
    application()


if __name__ == '__main__':
    main()
