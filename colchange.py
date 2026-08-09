import cv2
import numpy as np


img = cv2.imread("Mario.png")
if img is None:
  print("Error: Could not load Mario.png. Ensure the file is in this folder.")
  exit()


b_gain = 1.0
g_gain = 1.0
r_gain = 1.0
intensity = 1.0

print("Controls:")
print("R / r: Increase / Decrease Red")
print("G / g: Increase / Decrease Green")
print("B / b: Increase / Decrease Blue")
print("+ / -: Increase / Decrease Intensity")
print("ESC: Quit")

while True:
 
  b, g, r = cv2.split(img)

 
  b_mod = cv2.multiply(b, np.array([b_gain * intensity], dtype=np.float32))
  g_mod = cv2.multiply(g, np.array([g_gain * intensity], dtype=np.float32))
  r_mod = cv2.multiply(r, np.array([r_gain * intensity], dtype=np.float32))


  processed = cv2.merge([b_mod, g_mod, r_mod])
  processed = np.clip(processed, 0, 255).astype(np.uint8)

 
  cv2.imshow("Mario Color Filter", processed)

 
  key = cv2.waitKey(1) & 0xFF

  if key == 27: 
    break
  elif key == ord("r"):
    r_gain = min(2.0, r_gain + 0.1)
  elif key == ord("R"):
    r_gain = max(0.0, r_gain - 0.1)
  elif key == ord("g"):
    g_gain = min(2.0, g_gain + 0.1)
  elif key == ord("G"):
    g_gain = max(0.0, g_gain - 0.1)
  elif key == ord("b"):
    b_gain = min(2.0, b_gain + 0.1)
  elif key == ord("B"):
    b_gain = max(0.0, b_gain - 0.1)
  elif key == ord("+") or key == ord("="):
    intensity = min(2.0, intensity + 0.1)
  elif key == ord("-") or key == ord("_"):
    intensity = max(0.1, intensity - 0.1)

cv2.destroyAllWindows()
