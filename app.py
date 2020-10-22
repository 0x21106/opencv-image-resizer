import cv2
import os

allowed_extensions = (".jpg", ".jpeg", ".png")

for image in os.listdir():
    image_type = os.path.splitext(f'{os.getcwd()}\{image}');
    if image_type[1] in allowed_extensions:
        img = cv2.imread(f'{os.getcwd()}\{image}', 1)
        resized = cv2.resize(img, (100, 100))
        cv2.imwrite(f"{image_type[0]}_resized{image_type[1]}", resized)
