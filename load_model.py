from libraries import *
import pathlib

def load_custom_model(model_name):

    model_file = model_name

    model_dir = pathlib.Path(model_file)/"saved_model"

    model = tf.saved_model.load(str(model_dir))

    return model

model_name = 'exported-models/my_model'
detection_model = load_custom_model(model_name)