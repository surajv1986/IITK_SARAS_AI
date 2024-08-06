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

#setup Paths
POSITIVE_PATH = os.path.join('data', 'positive')
NEGATIVE_PATH = os.path.join('data', 'negative')
ANCHOR_PATH = os.path.join('data', 'anchor')

#Grab all .jpg files inside ANCHOR, POSITIVE & NEGATIVE PATHS
anchor = tf.data.Dataset.list_files(ANCHOR_PATH + '\*.jpg').take(300)
positive = tf.data.Dataset.list_files(POSITIVE_PATH + '\*.jpg').take(300)
negative = tf.data.Dataset.list_files(NEGATIVE_PATH + '\*.jpg').take(300)

dir_test = anchor.as_numpy_iterator()
dir_test.next()


#API to preprocess(resize and scale) the images for the tensor flow model
def preProcessImages(path_to_file):
    b_image = tf.io.read_file(file_path)
    imag = tf.io.decode_jpeg(b_image)
    imag = tf.image.resize(imag, (100, 100))
    imag = imag / 255.0

    return img
