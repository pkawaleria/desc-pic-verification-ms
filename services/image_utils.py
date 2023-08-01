import base64
import io
import tensorflow as tf
from PIL import Image
from keras.src.applications.convnext import preprocess_input

model = tf.keras.applications.InceptionV3(weights='imagenet')
def decode_base64_image(base64_string):
    imgdata = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(imgdata))
    image = image.convert('RGB')
    image = image.resize((299, 299))
    return image

def check_image_content(image):
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.expand_dims(image, axis=0)
    image = preprocess_input(image)

    # Dokonaj predykcji na obrazie
    predictions = model.predict(image)
    decoded_predictions = tf.keras.applications.inception_v3.decode_predictions(predictions)

    # Sprawdź, czy w predykcjach znajdują się nieodpowiednie klasy
    inappropriate_classes = ["nudity", "violence", "gun", "knife", "weapon"]
    for pred in decoded_predictions[0]:
        if any(inapp_class in pred[1] for inapp_class in inappropriate_classes):
            return True

    return False