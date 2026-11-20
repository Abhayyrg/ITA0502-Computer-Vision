
import cv2

img = cv2.imread("image.jpg")

watermark = img.copy()

cv2.putText(watermark, "MY WATERMARK",
            (50, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            2, (255, 255, 255), 3)

result = cv2.addWeighted(img, 0.7, watermark, 0.3, 0)

cv2.imshow("Original Image", img)
cv2.imshow("Watermarked Image", result)

cv2.imwrite("watermarked_image.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
