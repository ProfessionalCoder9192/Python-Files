import cv2
import numpy as np

WINDOW_NAME = "Interactive Filtering Lab"

img_bgr = cv2.imread("Mario.png", cv2.IMREAD_COLOR)

if img_bgr is None:
    img_bgr = np.zeros((400, 400, 3), dtype=np.uint8)
    cv2.putText(img_bgr, "Mario.png Not Found", (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    print("Warning: Mario.png could not be loaded. Canvas generated automatically.")

img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)


def nothing(x):
    pass


cv2.namedWindow(WINDOW_NAME)


cv2.createTrackbar("Filter: 0=None,1=Gauss,2=Median", WINDOW_NAME, 1, 2, nothing)
cv2.createTrackbar("Kernel Size", WINDOW_NAME, 3, 15, nothing)
cv2.createTrackbar("Detector: 0=Canny,1=Sobel,2=Laplace", WINDOW_NAME, 0, 2, nothing)
cv2.createTrackbar("Param 1 (Canny Low / Lap k)", WINDOW_NAME, 100, 255, nothing)
cv2.createTrackbar("Param 2 (Canny High)", WINDOW_NAME, 200, 255, nothing)

print("Controls:")
print("  - Adjust window sliders to test filters.")
print("  - Press 'ESC' or 'q' to quit.")

while True:
   
    f_type = cv2.getTrackbarPos("Filter: 0=None,1=Gauss,2=Median", WINDOW_NAME)
    k_size = cv2.getTrackbarPos("Kernel Size", WINDOW_NAME)
    edge_type = cv2.getTrackbarPos("Detector: 0=Canny,1=Sobel,2=Laplace", WINDOW_NAME)
    p1 = cv2.getTrackbarPos("Param 1 (Canny Low / Lap k)", WINDOW_NAME)
    p2 = cv2.getTrackbarPos("Param 2 (Canny High)", WINDOW_NAME)

   
    if k_size % 2 == 0:
        k_size = max(1, k_size - 1)

    
    filtered_img = img_gray.copy()
    if f_type == 1:
        filtered_img = cv2.GaussianBlur(img_gray, (k_size, k_size), 0)
    elif f_type == 2:
        filtered_img = cv2.medianBlur(img_gray, k_size)

    
    if edge_type == 0:
        edge_img = cv2.Canny(filtered_img, p1, p2)
    elif edge_type == 1:
        sobel_64f = cv2.Sobel(filtered_img, cv2.CV_64F, dx=1, dy=0, ksize=3)
        edge_img = cv2.convertScaleAbs(sobel_64f)
    elif edge_type == 2:
        lap_k = max(1, p1 if p1 % 2 != 0 else p1 - 1)
        if lap_k > 31: 
            lap_k = 31
        edge_img = cv2.Laplacian(filtered_img, cv2.CV_8U, ksize=lap_k)

    
    combined_display = np.hstack((img_gray, filtered_img, edge_img))
    cv2.imshow(WINDOW_NAME, combined_display)

    
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break

cv2.destroyAllWindows()
