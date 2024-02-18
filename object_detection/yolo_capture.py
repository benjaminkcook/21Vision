from ultralytics import YOLO

model = YOLO("./object_detection/best_20k.pt")

results = model.predict(source="0", show=True)

print(results)