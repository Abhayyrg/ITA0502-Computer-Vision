
import cv2

# Load input image
image = cv2.imread("face.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load OpenCV's built-in face cascade
cascade_path = (
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

face_cascade = cv2.CascadeClassifier(cascade_path)

# Check whether cascade loaded successfully
if face_cascade.empty():
    print("Error: Face cascade could not be loaded!")
    exit()

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(
        image,
        (x, y),
        (x+w, y+h),
        (0, 255, 0),
        2
    )

# Display result
print("Number of faces detected:", len(faces))

cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
