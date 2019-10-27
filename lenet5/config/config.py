# coding:utf-8

# 项目根路径
PROJECT_PATH="D:/PythonIDE/pythonProgram/AI-Practice-Tensorflow-Notes-master/lenet5/"

# redis ip
REDIS_IP = "10.166.33.86"
REDIS_PORT = 6379

# code_101
image_train_path_101 = './mnist_database/mnist_train_png_20000/'
label_train_path_101 = './mnist_database/mnist_train_png_20000.txt'
tfRecord_train_101 = PROJECT_PATH+'data/data_101/data/mnist_train.tfrecords'
image_test_path_101 = './mnist_database/mnist_test_png_5000/'
label_test_path_101 = './mnist_database/mnist_test_png_5000.txt'
tfRecord_test_101 = PROJECT_PATH+'data/data_101/data/mnist_test.tfrecords'
data_path_101 = './data'

MODEL_SAVE_PATH_101=PROJECT_PATH+"/model/model_101/model/"
MODEL_NAME_101="../mnist_model"

# code_41
image_train_path_41 = './mnist_database/mnist_train_png_20000/'
label_train_path_41 = './mnist_database/mnist_train_png_20000.txt'
tfRecord_train_41 = PROJECT_PATH+'/data/data_41/data/mnist_train.tfrecords'
image_test_path_41 = './mnist_database/mnist_train_png_20000/'
label_test_path_41 = './mnist_database/mnist_train_png_20000.txt'
tfRecord_test_41 = PROJECT_PATH+'data/data_41/data/mnist_test.tfrecords'
data_path_41 = '../data'

MODEL_SAVE_PATH_41=PROJECT_PATH+"model/model_41/model/"
MODEL_NAME_41="../mnist_model"

# code_21
image_train_path_21 = './mnist_database/mnist_train_jpg_2000/'
label_train_path_21 = './mnist_database/mnist_train_jpg_2000.txt'
tfRecord_train_21 = PROJECT_PATH+'./data/data_21/data/mnist_train.tfrecords'
image_test_path_21 = './mnist_database/mnist_test_jpg_2000/'
label_test_path_21 = './mnist_database/mnist_test_jpg_2000.txt'
tfRecord_test_21 = PROJECT_PATH+'./data/data_21/data/mnist_test.tfrecords'
data_path_21 = './data'

MODEL_SAVE_PATH_21 =PROJECT_PATH+"model/model_21/model/"
MODEL_NAME_21="../mnist_model"

# 服务器类配置
logPath = PROJECT_PATH+"log/"
requestCache = "tasks:task"
resultSavePath = "RegResult"
paramSavePath = "ParamResult"