import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

#NAME_FILE = "demo/cat.jpg"

model = tf.keras.models.load_model("modelo/model.h5")

def convertir_imagen_para_modelo(nombre_imagen):
    img = image.load_img(nombre_imagen, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    return images

def predecir(nombre_imagen):
    images = convertir_imagen_para_modelo(nombre_imagen)
    classes = model.predict(images, batch_size=10)
    if classes[0] > 0.5:
        #print(NAME_FILE + " is a dog")
        return "DOG"
    else:
        #print(NAME_FILE + " is a cat")
        return "CAT"


if __name__ == "__main__":
    predecir(NAME_FILE)