# Python Module to create path and move lfw images to data/negative folder
import os
import random
import numpy as np
from matplotlib import pyplot as plt
#import tensorflow functional API dependencies
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Layer, Conv2D, Dense, MaxPooling2D, Input, Flatten
import tensorflow as tf


#Avoid Out Of Memory errors by setting GPU Memory Consumption Growth
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, true)

#setup Paths
POS_PATH = os.path.join('data', 'positive')
NEG_PATH = os.path.join('data', 'negative')
ANC_PATH = os.path.join('data', 'anchor')

#Make the directories
#os.makedirs(POS_PATH)
#os.makedirs(NEG_PATH)
#os.makedirs(ANC_PATH)
# Get the current working directory
cwd = os.getcwd()

# Join the CWD with 'lfw' to get the correct path
lfw_path = os.path.join(cwd, 'lfw')
print(lfw_path)


for directory in os.listdir(lfw_path):
    dir_path = os.path.join(lfw_path, directory)
    print(dir_path)
    if not os.path.exists(dir_path):
        print(f"Error: {dir_path} does not exist")
    elif not os.path.isdir(dir_path):
        print(f"Error: {dir_path} is not a directory")
    else:
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):  # Check if it's a file
                NEW_PATH = os.path.join(NEG_PATH, file)
                os.replace(file_path, NEW_PATH)
                print(f"File {file} copied to {NEG_PATH}")
            else:
                print('not a file')
