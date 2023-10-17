from flask import Flask, render_template, url_for, request, redirect, send_from_directory
import os
import numpy as np
import tensorflow as tf
from keras_preprocessing import image
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input

model=load_model('weights/DenseNet.h5') #Loading our model
img=image.load_img("/Users/navedasif1/Desktop/hemehealth/chest_xray/val/NORMAL/NORMAL2-IM-0360-0001.jpeg",target_size=(224,224))
imagee=image.img_to_array(img) #Converting the X-Ray into pixels
imagee=np.expand_dims(imagee, axis=0)
img_data=preprocess_input(imagee)
prediction=model.predict(img_data)
if prediction[0][0]>prediction[0][1]:  #Printing the prediction of model.
    print(f"{prediction[0][0]} > {prediction[0][1]}")
    print('Person is safe.') 
else:
    print(f"{prediction[0][0]} < {prediction[0][1]}")
    print('Person is affected with Pneumonia.')