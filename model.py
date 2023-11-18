import keras
import numpy as np
from matplotlib.pyplot import imshow
from PIL import Image, ImageOps


base = "C:/Users/NISCHITHA/Desktop/covid/app"
model = keras.models.load_model(f'{base}/CovidTest.h5')

def image_pre(path):
    print(path)
    data = np.ndarray(shape=(1,128, 128, 1), dtype=np.float32)
    size = (128,128)
    image = Image.open(path)
    image = ImageOps.grayscale(image)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    data = image_array.reshape((-1,128,128,1))/255
    return data


def predict(data):
    prediction = model.predict(data)
    return np.round(prediction[0][0])
