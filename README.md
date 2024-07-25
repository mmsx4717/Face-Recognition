# 人脸识别程序

此项目程序可以进行简单的图片类人脸识别，利用openCV和Python，本程序用的都是相对路径，替换好自己的文件可以直接运行。

Demo文件下有两个py文件，FaceRecognitionMain为人脸识别程序，TrainModelMain为训练人脸模型文件。

Data文件下有三个子文件，分别为CompareData、TrainData、TrainModel，作用分别为存放待测试人脸图片文件、存放待训练人脸文件、存放训练模型。

CascadeClassifier存放openCV人脸检测器，本程序用的是默认（default）检测器，可以根据个人需求去替换检测器，检测器在openCV官网下载。

**注：**带测试图片命名要为数字；或者自行建立一个ID列表（int型），替换图片名字用来表示模型ID。

# Face recognition program

This project program can carry out simple picture face recognition, using openCV and Python, this program uses relative paths, and can be run directly after replacing their own files.

There are two py files in the demo file, FaceRecognitionMain is the face recognition program, and TrainModelMain is the training face model file.

There are three sub-files under the data file, namely CompareData, TrainData, and TrainModel, which are used to store the face image file to be tested, the face file to be trained, and the training model.

CascadeClassifier stores the openCV face detector, this program uses the default detector, and the detector can be replaced according to personal needs, and the detector can be downloaded from the openCV official website.

**Note:** The name of the picture with the test should be a number; Or create your own ID list (int type) and replace the image name to represent the model ID.