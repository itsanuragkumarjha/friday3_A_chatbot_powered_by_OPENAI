import tensorflow as tf
import cv2
import numpy as np

def load_model():
    model = tf.keras.models.load_model('deathstroke4.h5')
    return model

def predict_digit(model, image):
    prediction = model.predict(image)
    digit = prediction.argmax()
    print(prediction)
    return digit