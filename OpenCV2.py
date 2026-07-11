import cv2
image=cv2.imread('Mario.png')

gray_image = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(gray_image, (224, 224))


cv2.imshow('Grayscale Image', resized_image)
key = cv2.waitKey(0)

if key==ord('s'):
    cv2.imwrite('grayscale_resized_image.png', resized_image)
    print('image saved')
else:
    print('image not saved')
cv2.destroyAllWindows()

print(f'Grayscale Image Dimensions:{resized_image.shape}')