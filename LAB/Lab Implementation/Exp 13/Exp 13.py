
import cv2
import numpy as np

img = cv2.imread("image.jpg")

rows, cols = img.shape[:2]

src = np.float32([[50, 50], [200, 50], [50, 200]])
dst = np.float32([[10, 100], [200, 50], [100, 250]])

matrix = cv2.getAffineTransform(src, dst)

result = cv2.warpAffine(img, matrix, (cols, rows))

cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
