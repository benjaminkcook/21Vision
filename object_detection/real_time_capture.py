from ultralytics import YOLO
from logic.main import (
    get_current_running_count,
    on_hit,
    generate_deck_and_dealer_hand,
    convert_to_card,
)
import cv2

model = YOLO(".\\object_detection\\best_20k.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

deck, dealer_hand, dealer_bust = generate_deck_and_dealer_hand()
standing = False
dealer_string = f"Dealer hand: {dealer_hand[0]}"
while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error: Could not read frame.")
        continue  # Continue to the next iteration of the loop

    # Perform object detection on the current frame
    results = model.predict(source=frame, conf=0.5)

    # If there was an object detected, classify it, and write it into the frame
    for result in results:
        if len(result.boxes.cls) > 0:
            detect_objects = result.boxes.cls.numpy()
            object_conf = result.boxes.conf.numpy()
            for i in range(len(detect_objects)):
                box = result.boxes[i]
                confidence = int(object_conf[i] * 100) / 100
                name = result.names[detect_objects[i]]
                # Contains x, y ,w, h positions to draw stuff
                pos_list = box.xywh.numpy()
                x = int(pos_list[0, 0])
                y = int(pos_list[0, 1])
                w = int(pos_list[0, 2])
                h = int(pos_list[0, 3])
                color = (0, 230, 255)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                label = f"{convert_to_card(name)}, Confidence: {confidence}"
                cv2.putText(
                    frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2
                )

                names = [result.names[key] for key in detect_objects]
                cards = set(names)
                cards = list(cards)
                running_count = get_current_running_count(cards)

                # Display Running count at the top right-hand corner
                cv2.putText(
                    frame,
                    f"Running count: {running_count}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2,
                )

    if not standing:
        cv2.putText(
            frame,
            f"Dealer Hand: {dealer_hand[0]}, hidden",
            (10, frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (4, 2, 0),
            2,
        )
    elif standing and not dealer_bust:
        cv2.putText(
            frame,
            dealer_string,
            (10, frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (4, 2, 0),
            2,
        )

    cv2.imshow("21 Vision", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        standing = True
        dealer_string += f", {dealer_hand[-1]}"
        dealer_hand.pop()
    elif key == ord("q"):
        break
    elif key == ord("h"):
        on_hit("", "", "", 0)


cap.release()
cv2.destroyAllWindows()
