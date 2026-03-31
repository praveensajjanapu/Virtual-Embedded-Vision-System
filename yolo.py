import cv2
from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Start camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO detection
    results = model(frame)
    annotated = results[0].plot()

    # Show output
    cv2.imshow("YOLO Detection", annotated)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
