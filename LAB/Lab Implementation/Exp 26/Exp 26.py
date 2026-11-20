
import cv2

def reverse_video(input_video, output_video):
    cap = cv2.VideoCapture(input_video)

    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    if not frames:
        print("Unable to read video")
        return

    frames.reverse()

    height, width = frames[0].shape[:2]
    fps = 25

    writer = cv2.VideoWriter(
        output_video,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (width, height)
    )

    for frame in frames:
        writer.write(frame)

    writer.release()
    print("Reverse video created successfully")

reverse_video("input.mp4", "reverse.mp4")
