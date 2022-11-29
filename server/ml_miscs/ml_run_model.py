import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import numpy as np
import cv2
from glob import glob
from tqdm import tqdm
import tensorflow as tf
from tensorflow.keras.utils import CustomObjectScope
from ml_miscs.metrics import dice_loss, dice_coef, iou


""" Global parameters """
H = 512
W = 512



def background_eraser(path=""):
	""" Seeding """
	np.random.seed(42)
	tf.random.set_seed(42)
	directory = os.getcwd()
	print("...",directory)



	""" Loading model: DeepLabV3+ """
	with CustomObjectScope({'iou': iou, 'dice_coef': dice_coef, 'dice_loss': dice_loss}):
		model = tf.keras.models.load_model(f"ml_miscs/model.h5")
	# model.summary()




	""" Read the image """
	name = path[::]
	path = 'temp_img/uploads/'+path
	print(path)
	print("......",os.getcwd())

	image = cv2.imread(path, cv2.IMREAD_COLOR)
	image = image.astype(np.uint8)

	h, w, _ = image.shape
	x = cv2.resize(image, (W, H))
	x = x/255.0
	x = x.astype(np.float32)
	x = np.expand_dims(x, axis=0)

	""" Prediction """
	y = model.predict(x)[0]
	y = cv2.resize(y, (w, h))
	y = np.expand_dims(y, axis=-1)
	y = y > 0.5

	photo_mask = y
	background_mask = np.abs(1-y)

	masked_photo = image * photo_mask
	background_mask = np.concatenate([background_mask, background_mask, background_mask], axis=-1)
	background_mask = background_mask * [255,255,255]
	final_photo = masked_photo + background_mask
	final_photo = final_photo.astype(np.uint8)

	# return final_photo


	cv2.imwrite(f"temp_img/process/{name}", final_photo)

	# print("success",f"static/{name}")