import cv2

# Load the image
img = cv2.imread('Mario.png')
if img is None:
    print("Error: Could not open Mario.png")
    exit()

# Set starting window size coefficients
orig_w, orig_h = img.shape[1], img.shape[0]
scale = 1.0

# Window name
win_name = "Mario Resizer Tool"
cv2.namedWindow(win_name)

print("--- CONTROLS ---")
print("Press '+' to Zoom In")
print("Press '-' to Zoom Out")
print("Press '0' to Reset (100%)")
print("Press 'q' or 'ESC' to Quit")

while True:
    # 1. Calculate matching dimensions
    w = max(10, int(orig_w * scale))
    h = max(10, int(orig_h * scale))
    
    # 2. Resize with OpenCV
    interp = cv2.INTER_AREA if scale < 1.0 else cv2.INTER_LINEAR
    resized = cv2.resize(img, (w, h), interpolation=interp)
    
    # 3. Render window layout
    cv2.imshow(win_name, resized)
    
    # 4. Watch for button presses (waits 10ms)
    key = cv2.waitKey(10) & 0xFF
    
    # Check button conditions
    if key == ord('+') or key == ord('='):  # Plus key
        scale += 0.10
        print(f"Scale: {int(scale * 100)}%")
    elif key == ord('-'):                    # Minus key
        scale = max(0.10, scale - 0.10)
        print(f"Scale: {int(scale * 100)}%")
    elif key == ord('0'):                    # Reset key
        scale = 1.0
        print("Scale: 100%")
    elif key == ord('q') or key == 27:       # Quit keys ('q' or ESC)
        break

cv2.destroyAllWindows()