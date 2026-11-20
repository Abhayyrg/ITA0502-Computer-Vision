
import cv2
import numpy as np

def create_image():
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Create white image
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Box dimensions
    bh = height // 10
    bw = width // 10

    # Draw colored boxes
    cv2.rectangle(img, (0, 0), (bw, bh), (0, 0, 0), -1)
    cv2.rectangle(img, (width-bw, 0), (width-1, bh), (255, 0, 0), -1)
    cv2.rectangle(img, (0, height-bh), (bw, height-1), (0, 255, 0), -1)
    cv2.rectangle(img, (width-bw, height-bh),
                  (width-1, height-1), (0, 0, 255), -1)

    cv2.imshow("Four Colored Boxes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_image()
