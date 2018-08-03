#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
from os import walk
import cv2

# 视频数据集存放位置
DATA_DIR = 'E:\FutureCamp_ActionRecognitionData_TrainVal/'
# 视频转换为图像，图像存放位置
DATA_IMG_DIR = 'E:\FutureCamp_ActionRecognitionData_TrainVal\IMG/'

# 创建目录
def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    return path

for sub_dir in os.listdir(DATA_DIR):
    class_path = os.path.join(DATA_DIR, sub_dir + '/')
    img_class_dir = mkdir(DATA_IMG_DIR + sub_dir) #在DATA_IMG_DIR目录每个类别创建一个文件夹
    # print(class_path + '\t-' + sub_dir)
    filenames = next(walk(class_path))[2]
    for i, filename in enumerate(filenames): #注意这里的i不能少，不然filename会被解释成tuple而非str
        # print('\t' + filename)
        # 单个视频转图像帧
        vc = cv2.VideoCapture(class_path + filename) #读入视频文件
        img_dir = mkdir(img_class_dir + '/' + filename) #为每个视频创建一个图像文件夹
        # fps = vc.get(cv2.CAP_PROP_FPS)
        # print('fps: ' + str(fps))
        c = 0
        rval = vc.isOpened()
        #timeF = 1  #视频帧计数间隔频率
        while rval:   #循环读取视频帧
            c = c + 1
            rval, frame = vc.read()
        #    if(c%timeF == 0): #每隔timeF帧进行存储操作
        #        cv2.imwrite('smallVideo/smallVideo'+str(c) + '.jpg', frame) #存储为图像
            if rval:
                cv2.imwrite(img_dir + '/' + str(c).zfill(8) + '.jpg', frame) #存储为图像，注意opencv不会自动创建文件夹
                cv2.waitKey(1)
            else:
                break
        vc.release()