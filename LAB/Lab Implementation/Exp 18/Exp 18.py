
import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

h, w = img.shape[:2]

# Crop ROI
roi = img[50:200, 50:200]

# Copy ROI
copy = roi.copy()

# Resize ROI if required
copy = cv2.resize(copy, (w // 3, h // 3))

# Paste ROI at a valid position
rh, rw = copy.shape[:2]
img[0:rh, 0:rw] = copy

cv2.imshow("Original Image", cv2.imread("image.jpg"))
cv2.imshow("Cropped ROI", roi)
cv2.imshow("Final Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
