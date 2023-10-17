import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
import os
import tensorflow as tf
from keras.preprocessing import image

def load_path(path, part):
    """
    load X-ray dataset
    """
    dataset = []
    for folder in os.listdir(path):
        folder = path + '/' + str(folder)
        if os.path.isdir(folder):
            for body in os.listdir(folder):
                if body == part:
                    body_part = body
                    path_p = folder + '/' + str(body)
                    for id_p in os.listdir(path_p):
                        patient_id = id_p
                        path_id = path_p + '/' + str(id_p)
                        for lab in os.listdir(path_id):
                            if lab.split('_')[-1] == 'positive':
                                label = 'fractured'
                            elif lab.split('_')[-1] == 'negative':
                                label = 'normal'
                            path_l = path_id + '/' + str(lab)
                            for img in os.listdir(path_l):
                                img_path = path_l + '/' + str(img)
                                dataset.append(
                                    {
                                        'body_part': body_part,
                                        'patient_id': patient_id,
                                        'label': label,
                                        'image_path': img_path
                                    }
                                )
    return dataset

def get_true_labels(path, part):
    """
    load X-ray dataset
    """
    true_labels=[]
    dataset = []
    for folder in os.listdir(path):
        folder = path + '/' + str(folder)
        if os.path.isdir(folder):
            for body in os.listdir(folder):
                if body == part:
                    body_part = body
                    path_p = folder + '/' + str(body)
                    for id_p in os.listdir(path_p):
                        patient_id = id_p
                        path_id = path_p + '/' + str(id_p)
                        for lab in os.listdir(path_id):
                            if lab.split('_')[-1] == 'positive':
                                label = 'fractured'
                            elif lab.split('_')[-1] == 'negative':
                                label = 'normal'
                            path_l = path_id + '/' + str(lab)
                            for img in os.listdir(path_l):
                                if label=='fractured':
                                    true_labels.append(0)
                                else:
                                    true_labels.append(1)
                                img_path = path_l + '/' + str(img)
                                dataset.append(
                                    {
                                        'body_part': body_part,
                                        'patient_id': patient_id,
                                        'label': label,
                                        'image_path': img_path
                                    }
                                )
    return true_labels

true_labels=get_true_labels("/Users/navedasif1/Desktop/hemehealth/Dataset", "Elbow")

print(len(true_labels))

# load the models when import "predictions.py"
model_elbow_frac = tf.keras.models.load_model("weights/ResNet50_Elbow_frac.h5")
model_hand_frac = tf.keras.models.load_model("weights/ResNet50_Hand_frac.h5")
model_shoulder_frac = tf.keras.models.load_model("weights/ResNet50_Shoulder_frac.h5")
model_parts = tf.keras.models.load_model("weights/ResNet50_BodyParts.h5")

# categories for each result by index

#   0-Elbow     1-Hand      2-Shoulder
categories_parts = ["Elbow", "Hand", "Shoulder"]

#   0-fractured     1-normal
categories_fracture = ['fractured', 'normal']


# get image and model name, the default model is "Parts"
# Parts - bone type predict model of 3 classes
# otherwise - fracture predict for each part
def predict(img, model="Parts"):
    size = 224
    if model == 'Parts':
        chosen_model = model_parts
    else:
        if model == 'Elbow':
            chosen_model = model_elbow_frac
        elif model == 'Hand':
            chosen_model = model_hand_frac
        elif model == 'Shoulder':
            chosen_model = model_shoulder_frac

    # load image with 224px224p (the training model image size, rgb)
    temp_img = image.load_img(img, target_size=(size, size))
    x = image.img_to_array(temp_img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    prediction = np.argmax(chosen_model.predict(images), axis=1)
    return prediction
    # chose the category and get the string prediction
    # if model == 'Parts':
    #     prediction_str = categories_parts[prediction.item()]
    # else:
    #     prediction_str = categories_fracture[prediction.item()]

    # return prediction_str
data=load_path("/Users/navedasif1/Desktop/hemehealth/Dataset", "Elbow")
predictions=[]

for i in data:
    img_path=i['image_path']
    prediction=predict(img_path,"Elbow")
    predictions.append(prediction.item())
confusion = confusion_matrix(true_labels, predictions)
print(confusion)


