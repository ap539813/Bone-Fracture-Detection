import base64

# Define the hight and width of the images as required

img_width, img_height = 256,256

input_shape = (img_width, img_height)


theme_image_name = 'assets/bone_fracture.png'

"""### gif from local file"""
file_ = open(theme_image_name, "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()


css_file_path = 'style/style.css'

model_path_unet = 'assets/fracture_segmentation_unet_model.hdf5'
model_path_encoder_decoder = 'assets/fracture_detection_encoder_decoder_model.hdf5'

