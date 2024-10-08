pip install opencv-python

import cv2

# Load the image
image = cv2.imread('shark.png')

# Check if the image was loaded successfully
if image is not None:
    # Get the dimensions of the image
    height, width, channels = image.shape

    print(f"Width: {width} pixels")
    print(f"Height: {height} pixels")
    print(f"Channels: {channels}")
else:
    print("Error: Could not read the image.")
