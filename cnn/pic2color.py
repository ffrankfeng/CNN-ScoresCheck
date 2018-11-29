from PIL import Image
import numpy as np
from skimage import io,data,color
# f = open("D:/PythonIDE/pythonProgram/AI-Practice-Tensorflow-Notes-master/lenet5/mnist_data_jpg/mnist_train_jpg_2000.txt","r")
# lines = f.readlines()#读取全部内容
# path="D:/PythonIDE/pythonProgram/AI-Practice-Tensorflow-Notes-master/lenet5/mnist_data_jpg/mnist_train_jpg_2000/"
# path1="D:/PythonIDE/pythonProgram/AI-Practice-Tensorflow-Notes-master/lenet5/mnist_data_jpg/1mnist_train_jpg_2000/"
# f = open("C:/Users/asus/Desktop/mnist_train_jpg_60000.txt","r")
# lines = f.readlines()#读取全部内容
# path="C:/Users/asus/Desktop/train_pic/"
# path1="C:/Users/asus/Desktop/train_pic1/"
# for line in lines :
#     print(line.split()[0])
# I = Image.open(path+line.split()[0])
# I = Image.open("D:/PythonIDE/pythonProgram/reptile/train/0_22.png")
# L = I.convert('L')
# L.save("D:/PythonIDE/pythonProgram/reptile/123.jpg")
infile='D:/PythonIDE/pythonProgram/reptile/train/0_22.jpg'
outfile='D:/PythonIDE/pythonProgram/reptile/123.jpg'
im = Image.open(infile).convert('L') #灰度化
out = im.resize((80,80),Image.ANTIALIAS) #重新定义图片尺寸大小
out.save(outfile) #存储图片
    # # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
    # img = io.imread(path+line.split()[0], as_grey=False)
    # img_gray = color.rgb2gray(img)
    # rows, cols = img_gray.shape
    # for i in range(rows):
    #     for j in range(cols):
    #         if img_gray[i, j] <= 0.5:
    #             img_gray[i, j] = 1
    #         else:
    #             img_gray[i, j] = 0
    # # io.imshow(img_gray)
    # # io.show()
    # io.imsave(path1 + line.split()[0]+"",img_gray)
    # #print(im_arr)
    # # photo = L.point(nm_arr, '1')
    # # img_gray.save(path1 + line.split()[0])