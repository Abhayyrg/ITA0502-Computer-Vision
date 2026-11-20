
import cv2

prototxt = "MobileNetSSD_deploy.prototxt"
model = "MobileNetSSD_deploy.caffemodel"

net = cv2.dnn.readNetFromCaffe(prototxt, model)

img = cv2.imread("watch.jpg")

h, w = img.shape[:2]

blob = cv2.dnn.blobFromImage(
    cv2.resize(img, (300, 300)),
    0.007843, (300, 300), 127.5
)

net.setInput(blob)
detections = net.forward()

classes = ["background", "aeroplane", "bicycle",
           "bird", "boat", "bottle", "bus",
           "car", "cat", "chair", "cow",
           "diningtable", "dog", "horse",
           "motorbike", "person", "pottedplant",
           "sheep", "sofa", "train", "tvmonitor"]

found = False

for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    class_id = int(detections[0, 0, i, 1])

    if confidence > 0.5:
        label = classes[class_id]

        if label == "watch":
            found = True

            box = detections[0, 0, i, 3:7] * [
                w, h, w, h
            ]

            x1, y1, x2, y2 = box.astype(int)

            cv2.rectangle(img, (x1, y1), (x2, y2),
                          (0, 255, 0), 2)

            cv2.putText(img, "Watch", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 255, 0), 2)

if not found:
    print("Watch not detected")

cv2.imshow("Watch Recognition", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
