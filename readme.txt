.
├── pretreatment/ ：图像处理以及web访问接口代码
│   ├── data/ ：测试样本
│   ├── stitp/ ：项目所有代码
│   │   ├── stitp/src/main/java/cn.edu.njupt/configure/SystemVariables.java/ ：系统的一些环境变量；
│   │   └── src/main/webapp/js/index.js/ ：web的请求路径
│   │   ├── stitp/src/main/java/cn.edu.njupt/controller/ ：系统访问路径控制层
│   ├── stitp/src/main/java/cn.edu.njupt/utils/opencvUtils：opencv处理的工具类
├── lenet5/ ：数字识别系统的代码及模型
│   ├── code/ ：神经网络源代码目录，程序运行步骤详见document目录下文档；
│   │   ├── code_21/ ：识别0-20的cnn网络；
│   │   ├── code_41/ ：识别0-40的cnn网络；
│   │   └──code_101/ ：识别0-100的cnn网络；
│   ├── config/ ：系统配置文件
│   │   ├── config.py/ ：系统运行路径配置；
│   │   └──requirements.txt ：安装必要Python包时的pip配置文件；
│   ├── data/ ：训练好的数据集
│   │   ├── data_21/ ：手写数字0-20的数据集；
│   │   ├── data_41/ ：手写数字0-40的数据集；
│   │   └── data_101/ ：手写数字0-100的数据集；
│   ├── log/ ：系统运行日志文件
│   ├── mnist_database/ ：手写数字图片数据集
│   ├── model/ ：训练好的模型
│   │   ├── model_21/ ：手写数字0-20的训练模型；
│   │   ├── model_41/ ：手写数字0-40的训练模型；
│   │   └── model_101/ ：手写数字0-100的训练模型；
│   ├── test/ ：相关测试代码
│   ├── test_pic/ ：相关测试图片
│   │   ├── pic_21/ ：识别0-20的cnn网络测试图片；
│   │   ├── pic_41/ ：识别0-40的cnn网络测试图片；
│   │   └── pic_101/ ：识别0-100的cnn网络测试图片；
│   │   └── pic_send/ ：请求系统识别的试卷分数图片；
│   ├── utils/ ：相关工具类
│   ├── requestServer.py ：系统服务器启动类；
├── document/ ：相关文档资料
│   ├── paper/ ：论文资料
│   │   ├── initial stage reports/ ：项目初期的报告；
│   │   ├── mid-term stage reports/ ：项目中期的报告；
│   │   ├── final stage reports/ ：项目结题阶段的报告；
│   │   ├── monthly stage reports/ ：所有月度报告；
│   │   └── support material/ ：支撑材料、参考论文（PDF版）；
│   ├── presentation/ ：中期与结题整理的ppt材料；
│   └── usage.txt ：实验环境搭建以及源代码运行说明
└── readme.txt ：此文档本身；

