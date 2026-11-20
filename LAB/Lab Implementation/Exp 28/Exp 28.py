
import cv2

cap = cv2.VideoCapture("vehicles.mp4")

hog = cv2.HOGDescriptor()
hog.setSVMDetector(
    cv2.HOGDescriptor_getDefaultPeopleDetector()
)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    boxes, weights = hog.detectMultiScale(
        frame,
        winStride=(8, 8),
        padding=(8, 8),
        scale=1.05
    )

    for (x, y, w, h) in boxes:
        cv2.rectangle(
            frame, (x, y), (x+w, y+h),
            (0, 255, 0), 2
        )

        cv2.putText(
            frame, "Object",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6, (0, 255, 0), 2
        )

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
