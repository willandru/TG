import cv2
import numpy as np

# Load the image
img = cv2.imread('frame_extraido.png')
assert img is not None, "Image could not be read."

# Get image dimensions
height, width = img.shape[:2]

# Calculate the center of the image
center_x, center_y = width // 2, height // 2

# Define the size of the crop (30 pixels on each side from the center)
crop_size = 30

# Calculate the coordinates of the top-left corner of the crop
x_start = center_x - crop_size
y_start = center_y - crop_size

# Crop the image (60x60 pixels from the center)
cropped_img = img[y_start:y_start + 2 * crop_size, x_start:x_start + 2 * crop_size]

# Save the cropped image as PNG
cv2.imwrite('cropped_image.png', cropped_img)

# Display the cropped image
cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
