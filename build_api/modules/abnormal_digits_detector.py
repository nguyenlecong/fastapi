import cv2
from ultralytics import YOLO


class AbnormalDigitsDetector():
    def __init__(self, weight_path):
        self.model = YOLO(weight_path)
        self.abnormal_class_id = 1

    def detect_abnormal(self, image, conf=0.5, iou=0.6):
        result = self.model.predict(source=image, conf=conf, verbose=False, agnostic_nms=True, iou=iou)[0]
        boxes = result.boxes

        if not boxes:
            return 'Abnormal', 1.0
        
        abnormal_confs = [box.conf.item() for box in boxes if box.cls.int().item() == self.abnormal_class_id]
        if abnormal_confs:
            return 'Abnormal', max(abnormal_confs)
        else:
            return 'Normal', 1 - min(box.conf.item() for box in boxes)
    
    def visualize(self, image, conf=0.5, scale=3, padding=20, iou=0.6):
        viz_image = cv2.copyMakeBorder(image, padding, padding, padding, padding, cv2.BORDER_CONSTANT, value=[0, 0, 0])
        viz_image = cv2.resize(viz_image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

        result = self.model.predict(source=image, conf=conf, verbose=True, agnostic_nms=True, iou=iou)[0]
        boxes = result.boxes
        
        for box in boxes:
            xyxy = box.xyxy.int().tolist()[0]
            x1, y1, x2, y2 = map(lambda e: scale*(e+padding), xyxy)

            conf = box.conf.item()

            class_id = box.cls.int().item()
            class_name = self.model.names[class_id]
            if class_id == 1:
                color = [0, 0, 255]
            else:
                color = [0, 255, 0]

            cv2.rectangle(viz_image, (x1, y1), (x2, y2), color, 2, cv2.LINE_AA)
            cv2.putText(viz_image, class_name, (x1, y1-35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [255,255,255], 2, cv2.LINE_AA)
            cv2.putText(viz_image, f"{conf:.2f}", (x1, y2+45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, [255,255,255], 2, cv2.LINE_AA)
        return viz_image