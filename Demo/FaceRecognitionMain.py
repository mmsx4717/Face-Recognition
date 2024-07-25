import cv2

# 加载人脸检测器和特征提取器
face_cascade = cv2.CascadeClassifier('./CascadeClassifier/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

def face_detect_demo(image):
    # 将图像转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 使用人脸检测器检测人脸
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))   
    # 对每个检测到的人脸进行识别
    for x, y, w, h in faces:
        # 提取人脸区域
        face_roi = gray_image[y:y+h, x:x+w]
        # 提取人脸差别数据
        label, confidence = recognizer.predict(face_roi)
        print(f'模型ID：{label}', f'对比人员差值：{confidence:.2f}')
        # 返回数据
        return confidence, x, y, w, h
    
if __name__ == '__main__':
    # 读取测试图像
    image = cv2.imread('./Data/CompareData/.jpg') #自己图片路径
    # 加载训练数据
    recognizer.read('./Data/TrainModel/model.yml')
    # 提取人脸信息
    confidence, x, y, w, h = face_detect_demo(image)
    # 判断身份
    if confidence < 80:
        print('是本人')
    else:
        print('不是本人')
    # 释放内存
    cv2.destroyAllWindows()