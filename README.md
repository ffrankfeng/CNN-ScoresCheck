# CNN-ScoresCheck
卷积神经网络，多位数字识别，
python3 tensorflow
这个一个用于学生考试试卷分数核对矫正的应用

封装为后台服务器。

server入口：

​					requestServer.py ,需要配置redis数据库。

client入口：

​					clientDemo.py,直接运行即可。

内部封装了3个神经网络，分别识别0-20、0-40、0-100的手写数字。

代码在code_21、code_41、code_101文件夹下：

识别主程序入口：

​					mnist_app.py，可直接执行main方法。识别测试图片。





注意点：
	1、路径配置文件，redis ip和port配置在config文件夹下，请配置完成后再运行项目。
	2、model文件夹下有我训练好的模型，数据集在mnist_data_jpg，由于文件较大，暂未上传，如有需要可联系我。