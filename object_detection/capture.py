from ultralytics import YOLO
import cv2

model = YOLO(".\\object_detection\\best_20k.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error: Could not read frame.")
        continue  # Continue to the next iteration of the loop

    # Perform object detection on the current frame
    results = model.predict(source=frame, conf=0.7)

    # Extract bounding box coordinates and confidence scores
    for result in results:
        if len(result.boxes.cls) > 0:
            detect_objects = result.boxes.cls.numpy()
            names = [result.names[key] for key in detect_objects]
            cards = set(names)

    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
