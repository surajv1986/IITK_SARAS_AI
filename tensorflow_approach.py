import cv2
import os
import random
import numpy as np
from matplotlib import pyplot as plt
#import tensorflow functional API dependencies
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Layer, Conv2D, Dense, MaxPooling2D, Input, Flatten
import tensorflow as tf
import uuid
import time
import winsound

#set the frequency and the duration of the beep sound
freq=1000 
dur=2000

#setup Paths
POS_PATH = os.path.join('data', 'positive')
NEG_PATH = os.path.join('data', 'negative')
ANC_PATH = os.path.join('data', 'anchor')

#Avoid Out Of Memory errors by setting GPU Memory Consumption Growth
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, true)

def takePositiveImages():
    count = 0
    while count < 510:
            print("Taking images pls wait...")
            imgname = os.path.join(POS_PATH, '{}.jpg'.format(uuid.uuid1()))
            cv2.imwrite(imgname, frame)
            count+=1
            print(count)
            time.sleep(1)
        
    print("Images taken successfully...")
    winsound.Beep(freq,dur)

def takeAnchorImages():
    count = 0
    while count < 510:
        print("Taking images pls wait...")
        imgname = os.path.join(ANC_PATH, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgname, frame)
        count+=1
        print(count)
        time.sleep(1)
        winsound.Beep(freq,dur)
    
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    #collect anchors
    if (cv2.waitKey(1) & 0xFF == ord('a')):
        takeAnchorImages()

    #collect positive
    if (cv2.waitKey(1) & 0xFF == ord('p')):
        takePositiveImages()
        
    #crop frame to 250 * 250
    frame = frame[120: 120 + 250, 200:200 + 250]
    
    cv2.imshow('Image Collection', frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
