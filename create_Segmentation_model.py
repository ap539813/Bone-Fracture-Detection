# from keras.models import Model
# from keras.layers import Conv2D, MaxPooling2D, MaxPool2D, Conv2DTranspose
# from keras.layers import Dropout, Input, concatenate

import keras.models as models
from utils import jacard_loss
# from keras.regularizers import l2
def my_Unet(model_path):
    model = models.load_model(model_path, custom_objects = {'jacard': jacard_loss})
    return model

def my_simple_encoder_decoder(model_path):
    model = models.load_model(model_path)
    return model

