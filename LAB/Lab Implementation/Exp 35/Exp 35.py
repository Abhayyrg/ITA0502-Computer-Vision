
import cv2

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    # Get text from user
    text = input("Enter text to display: ")

    # Add text to image
    cv2.putText(img, text, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    # Display image
    cv2.imshow("Text on Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
