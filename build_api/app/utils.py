import cv2
import numpy as np
from fastapi import UploadFile


def read_imagefile(file: UploadFile) -> np.ndarray:
    file_bytes = np.frombuffer(file.file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    return image
