
import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define foreground color range (example: red)
    lower = np.array([0, 100, 100])
    upper = np.array([10, 255, 255])

    # Detect foreground color
    mask = cv2.inRange(hsv, lower, upper)

    # Remove foreground
    result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

    cv2.imshow("Original Image", img)
    cv2.imshow("Foreground Subtracted", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
