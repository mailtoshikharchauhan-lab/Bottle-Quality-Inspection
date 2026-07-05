from ultralytics import YOLO


class BottleDetector:
    def __init__(self, model_path):

        print("=" * 50)
        print("Loading YOLO Model...")
        print("=" * 50)

        self.model = YOLO(model_path)
        self.class_names = self.model.names

        print("Model Loaded Successfully!")
        print("=" * 50)

    def detect(self, frame):

        results = self.model.predict(
            source=frame,
            conf=0.25,
            iou=0.45,
            verbose=False
        )

        detections = []

        for result in results:

            if result.boxes is None:
                continue

            for box in result.boxes:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                confidence = float(box.conf[0])

                class_id = int(box.cls[0])

                class_name = self.class_names[class_id]

                detections.append({
                    "class": class_name,
                    "confidence": confidence,
                    "bbox": (x1, y1, x2, y2)
                })

        return detections