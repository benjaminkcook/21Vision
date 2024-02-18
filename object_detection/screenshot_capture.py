from ultralytics import YOLO
from logic.main import main as run_logic
import cv2

model = YOLO(".\\object_detection\\best_20k.pt")
camera = cv2.VideoCapture(0)
img_counter = 0
run = True


"""
Sourced from stackoverflow :D

https://stackoverflow.com/questions/75925797/how-do-i-work-with-the-result-of-model-predict-in-yolov8
"""

while run:
    ret, frame = camera.read()

    if not ret:
        print("failed to grab frame")
        break

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_path = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_path, frame)
        outs = model.predict(img_path)
        img_counter += 1
        
        image = cv2.imread(img_path)

        for result in outs:
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
                    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                    label = f"Class {result.names[detect_objects[i]]}, Confidence: {confidence}"
                    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                    cv2.imwrite(img_path, image)

                    names = [result.names[key] for key in detect_objects]
                    if img_counter == 2:
                        dealer_hand = set(names)
                        run = False
                        break
                    else:
                        player_hand = set(names)

camera.release()
run_logic(list(player_hand), list(dealer_hand))