from ultralytics import YOLO

model = YOLO("bestest_20k.pt")

results = model.predict(source="0", show=True)

print(results)