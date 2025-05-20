import cv2

from modules.abnormal_digits_detector import AbnormalDigitsDetector

abnormal_digits_detector = AbnormalDigitsDetector('models/abnormal_digits_detection_v2.pt')

def predict_image(image):
    label, conf_score = abnormal_digits_detector.detect_abnormal(image)

    if True:
        viz_image = abnormal_digits_detector.visualize(image)
        # cv2.imwrite('test.jpg', viz_image)
        return label, conf_score, viz_image
        
    return label, conf_score, None