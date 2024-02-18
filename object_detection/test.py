from ultralytics import YOLO

model = YOLO("best_20k.pt")

results = model.predict(source="0", show=True)

print(results)