import cv2
import numpy as np

# 1. Load the image
image = cv2.imread('Mario.png')

if image is None:
    print("Error: Mario.png not found. Please check the file path.")
else:
    # 2. Brighten the image
    # alpha controls contrast (1.0 is default), beta controls brightness
    alpha = 1.0
    beta = 50 
    brightened_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # 3. Rotate the image
    height, width = brightened_image.shape[:2]
    center = (width // 2, height // 2)
    angle = 45 # Rotation angle in degrees
    
    # Get rotation matrix and rotate
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale=1.0)
    rotated_image = cv2.warpAffine(brightened_image, rotation_matrix, (width, height))

    # 4. Crop the image
    # Define the coordinates for the region of interest [start_y:end_y, start_x:end_x]
    start_y, end_y = 100, 400
    start_x, end_x = 150, 450
    cropped_image = rotated_image[start_y:end_y, start_x:end_x]

    # 5. Display and save the results
    cv2.imshow('Original Image', image)
    cv2.imshow('Brightened Image', brightened_image)
    cv2.imshow('Rotated Image', rotated_image)
    cv2.imshow('Final Cropped Image', cropped_image)

    # Save the final cropped image
    cv2.imwrite('Mario_processed.png', cropped_image)

    # Wait for key press to close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
