import cv2
import numpy as np
import skimage.exposure


def antialiasing_edges(unique_filename="",premium=False):
	if not premium:
		img = cv2.imread(f"temp_img/process_trans/{unique_filename}", cv2.IMREAD_UNCHANGED)
		cv2.imwrite(f"static/{unique_filename}", img)
		return
	# load image with alpha channel
	img = cv2.imread(f"temp_img/process_trans/{unique_filename}", cv2.IMREAD_UNCHANGED)
	# input_image_alphachann = np.full((img.shape[0],img.shape[1]), 128, dtype=np.uint8)

	# img = np.dstack((img, input_image_alphachann))
	# extract only bgr channels
	bgr = img[:, :, 0:3]

	# extract alpha channel
	a = img[:, :, 3]

	# blur alpha channel
	ab = cv2.GaussianBlur(a, (0,0), sigmaX=2, sigmaY=2, borderType = cv2.BORDER_DEFAULT)

	# stretch so that 255 -> 255 and 127.5 -> 0
	aa = skimage.exposure.rescale_intensity(ab, in_range=(127.5,255), out_range=(0,255))

	# replace alpha channel in input with new alpha channel
	out = img.copy()
	out[:, :, 3] = aa

	# save output
	cv2.imwrite(f"static/{unique_filename}", out)

	# Display various images to see the steps
	# NOTE: In and Out show heavy aliasing. This seems to be an artifact of imshow(), which did not display transparency for me. However, the saved image looks fine

