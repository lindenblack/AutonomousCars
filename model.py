from tensorflow import keras
import numpy as np
import imutils
import cv2
import os


class Model:

    saved_model_s = 'Speed_prediction_model_9907.h5'
    saved_model_a = 'Angle_prediction_model.h5'

    def __init__(self):
        #self.model = keras.models.load_model(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.saved_model))
        self.model_s = keras.models.load_model(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.saved_model_s))
        self.model_a = keras.models.load_model(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.saved_model_a))
        self.model = [self.model_s, self.model_a]
        self.model[0].summary()
        self.model[1].summary()

    def preprocess_speed(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) / 255.0
        image = np.around(image ,2)
        #image = imutils.resize(image, width=80)
        #image = image[int(image.shape[0] / 4):, :, :]
        image = np.reshape(image,(image.shape[0],image.shape[1],1) )
        return image
    
    def preprocess_angle(self,image):
        height, _, _ = image.shape
        #image = image[int(height/2):,:,:]  # remove top half of the image, as it is not relevant for lane following
        #image = cv2.resize(image, (200,66)) # input image size (200,66) Nvidia model
        image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)  # Nvidia model said it is best to use YUV color space
        image = image / 255.0 # normalizing
        # Round everything into the image to 2 decimal places
        image = np.around(image ,2)
        return(image)

    def predict(self, img):
        #print(img.shape)
        image_speed = self.preprocess_speed(img)
        speed = self.model[0].predict(np.array([image_speed]))[0]
        speed = np.round(speed)
        #print(img.shape)
        image_angle = self.preprocess_angle(img)
        #print(image_angle.shape)
        angle = self.model[1].predict(np.array([image_angle]))[0]
        #angle, speed = self.model.predict(np.array([image]))[0]
        # Training data was normalised so convert back to car units
        angle = 80 * np.clip(angle, 0, 1) + 50
        speed = 35 * np.clip(speed, 0, 1)
        return angle, speed

