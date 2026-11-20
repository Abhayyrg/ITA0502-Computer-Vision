
import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define background color range (example: green)
    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    # Detect background color
    mask = cv2.inRange(hsv, lower, upper)

    # Remove background
    result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

    cv2.imshow("Original Image", img)
    cv2.imshow("Background Subtracted", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
