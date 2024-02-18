from ultralytics import YOLO
import cv2

model = YOLO(".\\object_detection\\best_20k.pt")
camera = cv2.VideoCapture(0)
img_counter = 0


"""
Sourced from stackoverflow :D

https://stackoverflow.com/questions/75925797/how-do-i-work-with-the-result-of-model-predict-in-yolov8
"""
while True:
    ret, frame = camera.read()

    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("21 Vision", frame)

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

        for result in outs:
            if len(result.boxes.cls) > 0:
                detect_objects = result.boxes.cls.numpy()
                names = [result.names[key] for key in detect_objects]
                cards = set(names)

camera.release()