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
            object_conf = result.boxes.conf.numpy()
            for i in range(len(detect_objects)):
                box = result.boxes[i]
                confidence = round(object_conf[i], 2)
                # Contains x, y ,w, h positions to draw stuff
                pos_list = box.xywh.numpy()
                x = int(pos_list[0, 0])
                y = int(pos_list[0, 1])
                w = int(pos_list[0, 2])
                h = int(pos_list[0, 3])
                color = (0, 255, 0)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                label = f"Class {result.names[detect_objects[i]]}, Confidence: {confidence}"
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                names = [result.names[key] for key in detect_objects]
                cards = set(names)
    cv2.imshow("21 Vision", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
