
import cv2

# Read the input image
image = cv2.imread("face.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load smile cascade from OpenCV's built-in folder
cascade_path = (
    cv2.data.haarcascades +
    "haarcascade_smile.xml"
)

smile_cascade = cv2.CascadeClassifier(cascade_path)

# Check whether cascade loaded successfully
if smile_cascade.empty():
    print("Error: Smile cascade could not be loaded!")
    exit()

# Detect smiles
smiles = smile_cascade.detectMultiScale(
    gray,
    scaleFactor=1.8,
    minNeighbors=20,
    minSize=(25, 25)
)

# Draw rectangles around detected smiles
for (x, y, w, h) in smiles:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

print("Number of smiles detected:", len(smiles))

# Display output
cv2.imshow("Smile Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
