
import cv2

# Read the input image
image = cv2.imread("face.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load eye cascade from OpenCV's built-in folder
cascade_path = (
    cv2.data.haarcascades +
    "haarcascade_eye.xml"
)

eye_cascade = cv2.CascadeClassifier(cascade_path)

# Check whether cascade loaded successfully
if eye_cascade.empty():
    print("Error: Eye cascade could not be loaded!")
    exit()

# Detect eyes
eyes = eye_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(15, 15)
)

# Draw rectangles around detected eyes
for (x, y, w, h) in eyes:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

print("Number of eyes detected:", len(eyes))

# Display output
cv2.imshow("Eye Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
