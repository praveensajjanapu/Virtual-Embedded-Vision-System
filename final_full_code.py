import cv2
import time
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Start webcam
cap = cv2.VideoCapture(0)

# FPS variable
prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for better performance
    frame = cv2.resize(frame, (640, 480))

    # YOLO detection
    results = model(frame)
    annotated = results[0].plot()

    # FPS calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time

    # Show FPS on screen
    cv2.putText(annotated, f"FPS: {int(fps)}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show output
    cv2.imshow("YOLO Detection", annotated)

    key = cv2.waitKey(1) & 0xFF

    # Press 's' to save image
    if key == ord('s'):
        cv2.imwrite("output.jpg", annotated)
        print("Image saved as output.jpg")

    # Press ESC to exit
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
