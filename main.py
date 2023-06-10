# Importing the required libraries
import cv2
import easyocr
import matplotlib.pyplot as plt

# Reading the Image
img_path = 'sign board.jpg'

img = cv2.imread(img_path)

# Text detector

detector = easyocr.Reader(['en'],gpu=False)

text_ = detector.readtext(img)

threshold = 0.25

# draw the bounding box and type text

for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t

    if score>threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (255, 0, 0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 5)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.tight_layout()
plt.axis('off')
plt.show()