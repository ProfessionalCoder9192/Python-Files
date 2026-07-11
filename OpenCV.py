import cv2
image=cv2.imread('Mario.png')
cv2.namedWindow('Mario Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Mario Image', 800, 500)

cv2.imshow('Mario Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f'Image Dimensions:{image.shape}')