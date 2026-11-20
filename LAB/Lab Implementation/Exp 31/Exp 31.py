
import cv2

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Get threshold value
    threshold = int(input("Enter threshold value (0-255): "))

    # Apply thresholding
    ret, segmented = cv2.threshold(
        gray, threshold, 255, cv2.THRESH_BINARY
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Segmented Image", segmented)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
