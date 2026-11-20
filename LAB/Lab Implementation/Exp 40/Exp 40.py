
import cv2
import pytesseract

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Open QuickTime video
cap = cv2.VideoCapture("video.mov")

if not cap.isOpened():
    print("Unable to open video!")
else:
    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Process every 30th frame
        if frame_count % 30 == 0:

            # Convert to grayscale
            gray = cv2.cvtColor(
                frame, cv2.COLOR_BGR2GRAY
            )

            # Apply thresholding
            _, thresh = cv2.threshold(
                gray, 150, 255, cv2.THRESH_BINARY
            )

            # Extract text using OCR
            text = pytesseract.image_to_string(thresh)

            if text.strip():
                print("Extracted Text:")
                print(text)

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

    print("Text extraction completed!")
